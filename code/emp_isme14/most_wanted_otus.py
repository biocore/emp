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
from os.path import basename, join, splitext
from tempfile import NamedTemporaryFile

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

def generate_most_wanted_list(otu_table_fp, rep_set_fp, gg_fp, nt_fp,
        mapping_fp, mapping_category, top_n, min_abundance, max_abundance,
        min_categories, max_gg_similarity, jobs_to_start, output_dir):
    try:
        makedirs(output_dir)
    except OSError:
        pass

    # First filter to keep only new (non-GG) OTUs.
    print "Filtering out all GG reference OTUs.\n"
    novel_otu_table_fp = join(output_dir, add_filename_suffix(otu_table_fp,
        '_novel'))
    stdout, stderr, ret_val = qiime_system_call(
        'filter_otus_from_otu_table.py -i %s -o %s -e %s' %
        (otu_table_fp, novel_otu_table_fp, gg_fp))
    print stdout
    print stderr
    if ret_val != 0:
        exit(1)

    # Next filter to keep only abundant otus in the specified range (looking
    # only at extremely abundant OTUs has the problem of yielding too many
    # that are similar to stuff in the nt database).
    print "Filtering out all OTUs that do not fall within the specified " + \
          "abundance threshold.\n"
    novel_abund_otu_table_fp = join(output_dir, add_filename_suffix(novel_otu_table_fp,
            '_min%d_max%d' % (min_abundance, max_abundance)))
    stdout, stderr, ret_val = qiime_system_call(
        'filter_otus_from_otu_table.py -i %s -o %s -n %d -x %d' %
        (novel_otu_table_fp, novel_abund_otu_table_fp, min_abundance,
         max_abundance))
    print stdout
    print stderr
    if ret_val != 0:
        exit(1)

    # Next, collapse by mapping_category.
    print "Collapsing OTU table by %s.\n" % mapping_category
    otu_table_by_samp_type_fp = join(output_dir, add_filename_suffix(novel_abund_otu_table_fp,
            '_%s' % mapping_category))
    stdout, stderr, ret_val = qiime_system_call(
        'summarize_otu_by_cat.py -c %s -o %s -m %s -i %s' %
        (novel_abund_otu_table_fp, otu_table_by_samp_type_fp, mapping_category,
         mapping_fp))
    print stdout
    print stderr
    if ret_val != 0:
        exit(1)

    # Filter to contain only otus in the specified minimum number of sample
    # types.
    print "Filtering OTU table to include only OTUs that appear in at " + \
          "least %d sample groups.\n" % min_categories
    otu_table_by_samp_type_ms_fp = join(output_dir, add_filename_suffix(
            otu_table_by_samp_type_fp, '_ms%d' % min_categories))
    stdout, stderr, ret_val = qiime_system_call(
        'filter_otus_from_otu_table.py -i %s -o %s -s %d' %
        (otu_table_by_samp_type_fp, otu_table_by_samp_type_ms_fp,
         min_categories))
    print stdout
    print stderr
    if ret_val != 0:
        exit(1)

    # Now that we have a filtered down OTU table of good candidate OTUs, filter
    # the corresponding representative set to include only these candidate
    # sequences.
    print "Filtering representative set to include only the latest " + \
          "candidate OTUs.\n"
    candidate_rep_set_fp = join(output_dir, add_filename_suffix(
            rep_set_fp, '_most_wanted_candidates'))
    stdout, stderr, ret_val = qiime_system_call(
        'filter_fasta.py -f %s -o %s -b %s' %
        (rep_set_fp, candidate_rep_set_fp, otu_table_by_samp_type_ms_fp))
    print stdout
    print stderr
    if ret_val != 0:
        exit(1)

    # Filter to contain only otus that don't hit GG at a certain similarity
    # threshold.
    print "Running uclust to get list of sequences that don't hit the " + \
          "maximum GG similarity threshold.\n"
    uclust_output_dir = join(output_dir, 'most_wanted_candidates_%s_%s'
            % (basename(gg_fp), str(max_gg_similarity)))
    stdout, stderr, ret_val = qiime_system_call(
        'parallel_pick_otus_uclust_ref.py -i %s -o %s -r %s -s %s -O %d'
        % (candidate_rep_set_fp, uclust_output_dir, gg_fp,
           str(max_gg_similarity), jobs_to_start))
    print stdout
    print stderr
    if ret_val != 0:
        exit(1)

    print "Filtering candidate sequences to only include uclust failures.\n"
    cand_gg_dis_rep_set_fp = join(output_dir,
            add_filename_suffix(candidate_rep_set_fp,
                                '_failures'))
    stdout, stderr, ret_val = qiime_system_call(
        'filter_fasta.py -f %s -s %s -o %s' % (candidate_rep_set_fp,
        join(uclust_output_dir,
        splitext(basename(candidate_rep_set_fp))[0] + '_failures.txt'),
        cand_gg_dis_rep_set_fp))
    print stdout
    print stderr
    if ret_val != 0:
        exit(1)

    # BLAST the failures against nt.
    print "BLASTing candidate sequences against nt database.\n"
    blast_output_dir = join(output_dir, 'blast_output')
    blast_cmd = 'parallel_blast.py -i %s -o %s -r %s -D -e 1e-3 -O %d' % (cand_gg_dis_rep_set_fp, blast_output_dir, nt_fp, jobs_to_start)
    print blast_cmd
    stdout, stderr, ret_val = qiime_system_call(blast_cmd)
    print stdout
    print stderr
    if ret_val != 0:
        exit(1)

    # Read in our filtered down candidate seqs file and latest filtered and
    # collapsed OTU table. We'll need to compute some stats on these to include
    # in our report.
    print "Collating results and formatting for output.\n"
    mw_seqs = {}
    for seq_id, seq in MinimalFastaParser(open(cand_gg_dis_rep_set_fp, 'U')):
        seq_id = seq_id.strip().split()[0]
        mw_seqs[seq_id] = seq
    otu_table_by_samp_type_ms = parse_biom_table(
            open(otu_table_by_samp_type_ms_fp, 'U'))

    # We'll sort the BLAST results by percent identity (ascending) and pick the
    # top n.
    blast_results = open(join(blast_output_dir,
        splitext(basename(cand_gg_dis_rep_set_fp))[0] + '_blast_out.txt'), 'U')
    top_n_mw = []
    processed_header = False
    for line in blast_results:
        # Skip header.
        if not processed_header:
            processed_header = True
            continue
        line = line.strip().split('\t')
        top_n_mw.append((line[0], line[1], float(line[2])))
    top_n_mw = sorted(top_n_mw, key=itemgetter(2))[:top_n]

    # Write results out to tsv and HTML table.
    mw_tsv_f = open(join(output_dir,
                    'top_%d_most_wanted_otus.txt' % top_n), 'w')
    mw_html_f = open(join(output_dir,
                    'top_%d_most_wanted_otus.html' % top_n), 'w')
    tsv_header = 'OTU ID\tSequence\tGreengenes taxonomy\t' + \
                 'NCBI nt closest match\tNCBI nt % identity'
    mw_tsv_f.write(tsv_header + '\n')

    tsv_header += '\tAbundance by %s' % mapping_category
    html_header = ''
    for col in tsv_header.split('\t'):
        html_header += '<th>%s</th>' % col
    mw_html_f.write('<table><tr>' + html_header + '</tr>')

    for otu_id, subject_id, percent_identity in top_n_mw:
        # Grab all necessary information to be included in our report.
        seq = mw_seqs[otu_id]
        tax = otu_table_by_samp_type_ms.ObservationMetadata[
            otu_table_by_samp_type_ms.getObservationIndex(otu_id)]['taxonomy']
        gb_id = subject_id.split('|')[3]
        ncbi_link = 'http://www.ncbi.nlm.nih.gov/nuccore/%s' % gb_id

        # Compute the abundance of each most wanted OTU in each sample
        # grouping and create a pie chart to go in the HTML table.
        samp_types = otu_table_by_samp_type_ms.SampleIds
        counts = otu_table_by_samp_type_ms.observationData(otu_id)
        if len(counts) != len(samp_types):
            raise ValueError("The number of observation counts does not match "
                             "the number of samples in the OTU table.")
        # Piechart code modified from matplotlib example:
        # http://matplotlib.sourceforge.net/examples/pylab_examples/pie_demo.html

        # Make a square figure and axes.
        figure(1, figsize=(6,6))
        ax = axes([0.1, 0.1, 0.8, 0.8])

        # Will auto-normalize the counts.
        pie(counts, labels=samp_types, autopct='%1.1f%%', shadow=True)

        output_img_dir = join(output_dir, 'img')
        try:
            makedirs(output_img_dir)
        except OSError:
            pass

        pie_chart_fp = join(output_img_dir, 'abundance_by_%s_%s.png' %
                            (mapping_category, otu_id))
        savefig(pie_chart_fp)

        mw_tsv_f.write('%s\t%s\t%s\t%s\t%s\n' %
                       (otu_id, seq, tax, gb_id, percent_identity))

        mw_html_f.write('<tr><td>%s</td><td>%s</td><td>%s</td>'
                '<td><a href="%s" target="_blank">%s</a></td><td>%s</td><td>'
                '<img src="%s" /></td></tr>' % (otu_id, seq, tax, ncbi_link,
                gb_id, percent_identity, pie_chart_fp))
    mw_html_f.write('</table>')
    mw_tsv_f.close()
    mw_html_f.close()
