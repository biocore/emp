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

def alpha_diversity_by_sample_type(adiv_fs, mapping_f,
                                   mapping_category='Sample_Type'):
    mapping_dict, mapping_comments = parse_mapping_file_to_dict(mapping_f)
    sample_type_map = {}
    #sample_type_counts = defaultdict(int)
    for samp_id in mapping_dict:
        sample_type_map[samp_id] = mapping_dict[samp_id][mapping_category]
        #sample_type_counts[sample_type_map[samp_id]] += 1

    sample_type_to_adiv = defaultdict(list)
    for adiv_f in adiv_fs:
        adiv_data = [line.strip().split('\t')
                     for line in adiv_f if line.strip()][1:]

        for samp_id, adiv in adiv_data:
            try:
                sample_type = sample_type_map[samp_id]
            except KeyError:
                sample_type = 'Unknown'
            # TODO do we need to normalize this? how?
            #adiv = float(adiv) / sample_type_counts[sample_type]
            adiv = float(adiv)
            sample_type_to_adiv[sample_type].append(adiv)

    plotting_data = [(median(v), '%s (n=%d)' % (k, len(v)), v) for k, v in
                     sample_type_to_adiv.items() if k != 'Unknown']
    plotting_data.sort()

    plot_fig = generate_box_plots([dist[2] for dist in
            plotting_data], x_tick_labels=[dist[1] for dist in plotting_data],
            x_label=mapping_category, y_label='Alpha Diversity',
            title='Alpha Diversity by %s' % mapping_category)
    tight_layout()
    return plotting_data, plot_fig
