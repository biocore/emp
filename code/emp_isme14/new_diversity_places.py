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

"""Contains functions used in the alpha_diversity_by_sample_type.py script."""

from collections import defaultdict
from operator import itemgetter
from os import makedirs
from os.path import join
from tempfile import NamedTemporaryFile

from numpy import median
from pylab import savefig, tight_layout

from biom.parse import parse_biom_table

from cogent import DNA, LoadSeqs
from cogent.app.blast import blast_seqs, Blastall
from cogent.app.formatdb import build_blast_db_from_fasta_path
from cogent.parse.blast import BlastResult
from cogent.parse.fasta import MinimalFastaParser
from cogent.util.misc import remove_files

from qiime.parse import parse_mapping_file_to_dict
from qiime.pycogent_backports.distribution_plots import generate_box_plots
from qiime.util import (parse_command_line_parameters, get_options_lookup,
                        make_option)

def generate_new_diversity_plots(otu_table_fs, gg_f, mapping_f,
                                 mapping_category='Sample_Type'):
    mapping_dict, mapping_comments = parse_mapping_file_to_dict(mapping_f)
    sample_type_map = {}
    for samp_id in mapping_dict:
        sample_type_map[samp_id] = mapping_dict[samp_id][mapping_category]

    gg_otus = [seq_id.split()[0] for seq_id, s in MinimalFastaParser(gg_f)]

    # Track by sample ID, which allows multiple OTU tables (even with
    # overlapping sample IDs) to be supported.
    success_counts = defaultdict(int)
    failure_counts = defaultdict(int)
    new_otus = defaultdict(list)
    for otu_table_f in otu_table_fs:
        otu_table = parse_biom_table(otu_table_f)
        novel_otus = set(otu_table.ObservationIds) - set(gg_otus)

        for counts, otu_id, md in otu_table.iterObservations():
            if otu_id in novel_otus:
                for samp_id, count in zip(otu_table.SampleIds, counts):
                    failure_counts[samp_id] += count
                    if count > 0:
                        new_otus[samp_id].append(otu_id)
            else:
                for samp_id, count in zip(otu_table.SampleIds, counts):
                    success_counts[samp_id] += count

    percent_failures_result = defaultdict(list)
    num_new_otus_result = defaultdict(list)
    for samp_id in set(success_counts.keys() + failure_counts.keys()):
        samp_type = sample_type_map[samp_id]
        failure_count = failure_counts[samp_id]
        success_count = success_counts[samp_id]
        percent_failures = (failure_count /
                            (success_count + failure_count)) * 100.0
        percent_failures_result[samp_type].append(percent_failures)
        num_new_otus_result[samp_type].append(len(set(new_otus[samp_id])))

    # TODO remove this duplicate code
    percent_failures_data = [(median(v), '%s (n=%d)' % (k, len(v)), v)
                             for k, v in percent_failures_result.items()]
    percent_failures_data.sort()
    percent_failures_plot = generate_box_plots(
            [e[2] for e in percent_failures_data],
            x_tick_labels=[e[1] for e in percent_failures_data],
            x_label=mapping_category,
            y_label='% Novel Seqs',
            title='%% Novel Seqs by %s' % mapping_category)
    percent_failures_plot.tight_layout()

    num_new_otus_data = [(median(v), '%s (n=%d)' % (k, len(v)), v)
                         for k, v in num_new_otus_result.items()]
    num_new_otus_data.sort()
    num_new_otus_plot = generate_box_plots(
            [e[2] for e in num_new_otus_data],
            x_tick_labels=[e[1] for e in num_new_otus_data],
            x_label=mapping_category,
            y_label='Number of Novel OTUs',
            title='Number of Novel OTUs by %s' % mapping_category)
    num_new_otus_plot.tight_layout()

    return percent_failures_data, percent_failures_plot, num_new_otus_data, \
           num_new_otus_plot

# Not sure if we'll need the following code...
#def summarize_unclassified(ts_f):
#    """MUST be absolute abundances for this to work!"""
#
#    for line in ts_f:
#        line = line.strip()
#        if line:
#            elements = line.split('\t')
#            taxon = elements[0]
#            abundances = elements[1:]
#            if taxon.strip().split(';')[-1] == 'Other':
#                percent_unclassified += sum(map(float, abundances)) / \
#                                        len(abundances)
#    return percent_unclassified
