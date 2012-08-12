#!/usr/bin/env python
from __future__ import division

__author__ = "Jai Ram Rideout"
__copyright__ = "Copyright 2012, The QIIME project"
__credits__ = ["Jai Ram Rideout", "Greg Caporaso"]
__license__ = "GPL"
__version__ = "1.5.0-dev"
__maintainer__ = "Jai Ram Rideout"
__email__ = "jai.rideout@gmail.com"
__status__ = "Development"

"""Contains functions used in the most_wanted_otus.py script."""

from collections import defaultdict
from operator import itemgetter
from os import makedirs
from os.path import basename, join, normpath, splitext
from tempfile import NamedTemporaryFile

from pylab import axes, figure, pie, savefig

from biom.parse import parse_biom_table

from cogent import DNA, LoadSeqs
from cogent.app.blast import blast_seqs, Blastall
from cogent.app.formatdb import build_blast_db_from_fasta_path
from cogent.parse.blast import BlastResult
from cogent.parse.fasta import MinimalFastaParser
from cogent.util.misc import remove_files

from qiime.parse import parse_mapping_file_to_dict
from qiime.util import (add_filename_suffix, parse_command_line_parameters,
        get_options_lookup, make_option, qiime_system_call)
from qiime.workflow import generate_log_fp, WorkflowError, WorkflowLogger

def generate_most_wanted_list(output_dir, otu_table_fps, rep_set_fp, gg_fp,
        nt_fp, mapping_fp, mapping_category, top_n, min_abundance,
        max_abundance, min_categories, max_gg_similarity, e_value,
        word_size, jobs_to_start, command_handler, status_update_callback,
        force):
    try:
        makedirs(output_dir)
    except OSError:
        if not force:
            raise WorkflowError("Output directory '%s' already exists. Please "
                    "choose a different directory, or force overwrite with -f."
                    % output_dir)

    logger = WorkflowLogger(generate_log_fp(output_dir))
    commands, blast_results_fp, rep_set_cands_failures_fp, \
        master_otu_table_ms_fp = _get_most_wanted_filtering_commands(
            output_dir, otu_table_fps,
            rep_set_fp, gg_fp, nt_fp, min_abundance, max_abundance,
            min_categories, max_gg_similarity, e_value, word_size,
            jobs_to_start)

    # Execute the commands, but keep the logger open because
    # we're going to write additional status updates as we process the data.
    command_handler(commands, status_update_callback, logger,
                    close_logger_on_success=False)
    commands = []

    # We'll sort the BLAST results by percent identity (ascending) and pick the
    # top n.
    logger.write("Reading in BLAST results, sorting by percent identity, "
                 "and picking the top %d OTUs.\n\n" % top_n)
    top_n_mw = _get_top_n_blast_results(open(blast_results_fp, 'U'), top_n)

    # Read in our filtered down candidate seqs file and latest filtered and
    # collapsed OTU table. We'll need to compute some stats on these to include
    # in our report.
    logger.write("Reading in filtered candidate sequences and latest filtered "
                 "and collapsed OTU table.\n\n")
    mw_seqs = _get_rep_set_lookup(open(rep_set_cands_failures_fp, 'U'))
    master_otu_table_ms = parse_biom_table(open(master_otu_table_ms_fp, 'U'))

    # Write results out to tsv and HTML table.
    logger.write("Writing most wanted OTUs results to TSV and HTML "
                 "tables.\n\n")
    output_img_dir = join(output_dir, 'img')
    try:
        makedirs(output_img_dir)
    except OSError:
        # It already exists, which is okay since we already know we are in
        # 'force' mode from above.
        pass

    tsv_lines, html_lines, plot_fps = _format_top_n_results_table(top_n_mw,
            mw_seqs, master_otu_table_ms, output_img_dir, mapping_category)

    mw_tsv_f = open(join(output_dir,
                    'top_%d_most_wanted_otus.txt' % top_n), 'w')
    mw_tsv_f.write(tsv_lines)
    mw_tsv_f.close()

    mw_html_f = open(join(output_dir,
                    'top_%d_most_wanted_otus.html' % top_n), 'w')
    mw_html_f.write(html_lines)
    mw_html_f.close()
    logger.close()

def _get_most_wanted_filtering_commands(output_dir, otu_table_fps, rep_set_fp,
        gg_fp, nt_fp, mapping_fp, mapping_category, min_abundance,
        max_abundance, min_categories, max_gg_similarity, e_value, word_size,
        jobs_to_start):
    commands = []
    otu_tables_to_merge = []

    for otu_table_fp in otu_table_fps:
        # First filter to keep only new (non-GG) OTUs.
        novel_otu_table_fp = join(output_dir, add_filename_suffix(otu_table_fp,
                                                                  '_novel'))
        commands.append([('Filtering out all GG reference OTUs',
                'filter_otus_from_otu_table.py -i %s -o %s -e %s' %
                (otu_table_fp, novel_otu_table_fp, gg_fp))])

        # Next filter to keep only abundant otus in the specified range
        # (looking only at extremely abundant OTUs has the problem of yielding
        # too many that are similar to stuff in the nt database).
        novel_abund_otu_table_fp = join(output_dir,
                add_filename_suffix(novel_otu_table_fp, '_min%d_max%d' %
                (min_abundance, max_abundance)))
        commands.append([('Filtering out all OTUs that do not fall within the '
                'specified abundance threshold',
                'filter_otus_from_otu_table.py -i %s -o %s -n %d -x %d' %
                (novel_otu_table_fp, novel_abund_otu_table_fp, min_abundance,
                 max_abundance))])

        # Next, collapse by mapping_category.
        otu_table_by_samp_type_fp = join(output_dir,
                add_filename_suffix(novel_abund_otu_table_fp, '_%s' %
                mapping_category))
        commands.append([('Collapsing OTU table by %s' % mapping_category,
                'summarize_otu_by_cat.py -c %s -o %s -m %s -i %s' %
                (novel_abund_otu_table_fp, otu_table_by_samp_type_fp,
                 mapping_category, mapping_fp))])
        otu_tables_to_merge.append(otu_table_by_samp_type_fp)

    # Merge all collapsed OTU tables.
    master_otu_table_fp = join(output_dir,
            'master_otu_table_novel_min%d_max%d_%s.biom' %
            (min_abundance, max_abundance, mapping_category))
    commands.append([('Merging collapsed OTU tables',
            'merge_otu_tables.py -i %s -o %s' %
            (','.join(otu_tables_to_merge), master_otu_table_fp))])

    # Filter to contain only otus in the specified minimum number of sample
    # types.
    master_otu_table_ms_fp = join(output_dir, add_filename_suffix(
            master_otu_table_fp, '_ms%d' % min_categories))
    commands.append([('Filtering OTU table to include only OTUs that appear '
            'in at least %d sample groups' % min_categories,
            'filter_otus_from_otu_table.py -i %s -o %s -s %d' %
            (master_otu_table_fp, master_otu_table_ms_fp, min_categories))])

    # Now that we have a filtered down OTU table of good candidate OTUs, filter
    # the corresponding representative set to include only these candidate
    # sequences.
    rep_set_cands_fp = join(output_dir,
            add_filename_suffix(rep_set_fp, '_candidates'))
    commands.append([('Filtering representative set to include only the '
            'latest candidate OTUs',
            'filter_fasta.py -f %s -o %s -b %s' %
            (rep_set_fp, rep_set_cands_fp, master_otu_table_ms_fp))])

    # Find the otus that don't hit GG at a certain maximum similarity
    # threshold.
    uclust_output_dir = join(output_dir, 'most_wanted_candidates_%s_%s' %
            (basename(gg_fp), str(max_gg_similarity)))
    commands.append([('Running uclust to get list of sequences that don\'t '
            'hit the maximum GG similarity threshold',
            'parallel_pick_otus_uclust_ref.py -i %s -o %s -r %s -s %s -O %d' %
            (rep_set_cands_fp, uclust_output_dir, gg_fp,
             str(max_gg_similarity), jobs_to_start))])

    # Filter the rep set to only include the failures from uclust.
    rep_set_cands_failures_fp = join(output_dir,
            add_filename_suffix(rep_set_cands_fp, '_failures'))
    commands.append([('Filtering candidate sequences to only include uclust '
            'failures',
            'filter_fasta.py -f %s -s %s -o %s' %
            (rep_set_cands_fp, join(uclust_output_dir,
             splitext(basename(rep_set_cands_fp))[0] + '_failures.txt'),
             rep_set_cands_failures_fp))])

    # BLAST the failures against nt.
    blast_output_dir = join(output_dir, 'blast_output')
    commands.append([('BLASTing filtered candidate sequences against nt '
            'database',
            'parallel_blast.py -i %s -o %s -r %s -D -e %f -w %d -O %d' %
            (rep_set_cands_failures_fp, blast_output_dir, nt_fp, e_value,
             word_size, jobs_to_start))])

    blast_results_fp = join(blast_output_dir,
            splitext(basename(rep_set_cands_failures_fp))[0] +
                              '_blast_out.txt')

    return commands, blast_results_fp, rep_set_cands_failures_fp, \
           master_otu_table_ms_fp

def _get_top_n_blast_results(blast_results_f, top_n):
    """blast_results should only contain a single hit per query sequence"""
    result = []
    for line in blast_results_f:
        # Skip headers and comments.
        line = line.strip()
        if line and not line.startswith('#'):
            line = line.split('\t')
            result.append((line[0], line[1], float(line[2])))
    return sorted(result, key=itemgetter(2))[:top_n]

def _get_rep_set_lookup(rep_set_f):
    result = {}
    for seq_id, seq in MinimalFastaParser(rep_set_f):
        seq_id = seq_id.strip().split()[0]
        result[seq_id] = seq
    return result

def _format_top_n_results_table(top_n_mw, mw_seqs, master_otu_table_ms,
                                output_img_dir, mapping_category):
    tsv_lines = ''
    html_lines = ''
    plot_fps = []

    tsv_header = 'OTU ID\tSequence\tGreengenes taxonomy\t' + \
                 'NCBI nt closest match\tNCBI nt % identity'
    tsv_lines += tsv_header + '\n'
    tsv_header += '\tAbundance by %s' % mapping_category
    html_header = ''
    for col in tsv_header.split('\t'):
        html_header += '<th>%s</th>' % col
    html_lines += '<table><tr>' + html_header + '</tr>'

    for otu_id, subject_id, percent_identity in top_n_mw:
        # Grab all necessary information to be included in our report.
        seq = mw_seqs[otu_id]

        # Splitting code taken from
        # http://code.activestate.com/recipes/496784-split-string-into-n-
        #   size-pieces/
        split_seq = [seq[i:i+20] for i in range(0, len(seq), 20)]

        tax = master_otu_table_ms.ObservationMetadata[
            master_otu_table_ms.getObservationIndex(otu_id)]['taxonomy']
        gb_id = subject_id.split('|')[3]
        ncbi_link = 'http://www.ncbi.nlm.nih.gov/nuccore/%s' % gb_id

        # Compute the abundance of each most wanted OTU in each sample
        # grouping and create a pie chart to go in the HTML table.
        samp_types = master_otu_table_ms.SampleIds
        counts = master_otu_table_ms.observationData(otu_id)
        if len(counts) != len(samp_types):
            raise WorkflowError("The number of observation counts does not "
                                "match the number of samples in the OTU "
                                "table.")

        # Piechart code modified from matplotlib example:
        # http://matplotlib.sourceforge.net/examples/pylab_examples/
        #   pie_demo.html
        figure(figsize=(6,6))
        ax = axes([0.1, 0.1, 0.8, 0.8])

        # Will auto-normalize the counts.
        pie(counts, labels=samp_types, autopct='%1.1f%%', shadow=True)

        # We need a relative path to the image.
        pie_chart_filename = 'abundance_by_%s_%s.png' % (mapping_category,
                                                         otu_id)
        pie_chart_rel_fp = join(basename(normpath(output_img_dir)),
                pie_chart_filename)
        pie_chart_abs_fp = join(output_img_dir, pie_chart_filename)
        savefig(pie_chart_abs_fp)
        plot_fps.append(pie_chart_abs_fp)

        tsv_lines += '%s\t%s\t%s\t%s\t%s\n' % (otu_id, seq, tax, gb_id,
                                               percent_identity)

        html_lines += ('<tr><td>%s</td><td>%s</td><td>%s</td>'
            '<td><a href="%s" target="_blank">%s</a></td><td>%s</td><td>'
            '<img src="%s" width="300" height="300" /></td></tr>' % (otu_id,
            '\n'.join(split_seq), tax, ncbi_link, gb_id, percent_identity,
            pie_chart_rel_fp))
    html_lines += '</table>'

    return tsv_lines, html_lines, plot_fps
