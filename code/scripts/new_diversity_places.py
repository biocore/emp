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

from glob import glob
from os import makedirs
from os.path import join
from pickle import dump
from qiime.util import (add_filename_suffix, parse_command_line_parameters,
        get_options_lookup, make_option, qiime_system_call)

from emp.new_diversity_places import generate_new_diversity_plots

options_lookup = get_options_lookup()

script_info = {}
script_info['brief_description'] = ""
script_info['script_description'] = ""
script_info['script_usage'] = [("Generate plots for new diversity", "The "
"following command generates two plots that compare new, or novel, OTUs in "
"samples grouped by the mapping category 'Environment'. The plot '"
"num_novel_otus_by_Environment.pdf compares the number of unique novel OTUs "
"in each environment, and 'percent_novel_seqs_by_Environment.pdf' "
"compares the percentage of novel sequences (i.e. sequences that were not "
"that were assigned to a GG reference OTU) in each environment.",
"%prog -i otu_table1.biom,otu_table2.biom -g ref_seqs.fasta -m map.txt -c "
"Environment -o new_diversity_out")]
script_info['output_description'] = ""

script_info['required_options'] = [
    make_option('-i','--otu_table_fps',type="existing_filepaths",
        help='paths to the input OTU tables (i.e., the output from '
        'make_otu_table.py)'),
    make_option('-g','--gg_fasta_fp',type="existing_filepath",
                help='ref db otus were picked against'),
    options_lookup['mapping_fp'],
    options_lookup['output_dir']
]
script_info['optional_options'] = [
    make_option('-c', '--mapping_category', type='string',
                help='', default='SAMPLE_TYPE'),
    make_option('-n', '--min_num_samples', type='int',
                help='', default=11),
    make_option('-e', '--category_values_to_exclude', type='string',
                help='comma-separated list of values within '
                '--mapping_category to exclude from the plots', default='NA')
#    make_option('-l', '--taxonomic_levels', type='string',
#                help='for summarize_taxa.py\'s output files (L2, L3, ...)',
#                default='Kindom,Phylum,Class,Order,Family')
]
script_info['version'] = __version__

def main():
    option_parser, opts, args = parse_command_line_parameters(**script_info)

    output_dir = opts.output_dir
    mapping_category = opts.mapping_category

    try:
        makedirs(output_dir)
    except OSError:
        pass

    percent_failures_data, percent_failures_plot, num_new_otus_data, \
           num_new_otus_plot = generate_new_diversity_plots(
            [open(otu_table_fp, 'U') for otu_table_fp in opts.otu_table_fps],
            open(opts.gg_fasta_fp, 'U'), open(opts.mapping_fp, 'U'),
            mapping_category, opts.min_num_samples,
            opts.category_values_to_exclude.split(','), opts.verbose)

    # Save plots as PDFs.
    percent_failures_plot.savefig(join(output_dir,
                                  'percent_novel_seqs_by_%s.pdf' %
                                  mapping_category))
    num_new_otus_plot.savefig(join(output_dir,
                              'num_novel_otus_by_%s.pdf' %
                              mapping_category))

    # Pickle plot raw data in case we need to load up the data again into new
    # plots and interactively tweak them (it'll take too long to rerun the
    # whole script for these tweaks).
    dump(percent_failures_data, open(join(output_dir,
            'percent_novel_seqs_by_%s.p' % mapping_category), 'wb'))
    dump(num_new_otus_data, open(join(output_dir,
            'num_novel_otus_by_%s.p' % mapping_category), 'wb'))

# Not sure if we'll need the following code...
#    # Filter otu table to include only new otus.
#    novel_otu_table_fp = add_filename_suffix(opts.otu_table_fp, '_novel')
#    stdout, stderr, ret_val = qiime_system_call(
#        'filter_otus_from_otu_table.py -i %s -o %s -e %s' % (opts.otu_table_fp,
#            novel_otu_table_fp, opts.gg_fasta_fp))
#    print stdout
#    print stderr
#    if ret_val != 0:
#        exit(1)
#
#    # Summarize taxa, making sure to report absolute abundances so that we can
#    # report raw numbers of classified versus unclassified.
#    stdout, stderr, ret_val = qiime_system_call(
#        'summarize_taxa.py -i %s -o %s -a' % (novel_otu_table_fp, output_dir))
#    print stdout
#    print stderr
#    if ret_val != 0:
#        exit(1)
#    
#    # Determine the abundance of unclassifiable otus at each level.
#    unclassified_report_f = open(join(output_dir, 'unclassified_report.txt'))
#    unclassified_report_f.write('Taxonomic rank\t% unclassified OTUs\n')
#
#    ts_fps = glob(join(output_dir, '%s_L*.txt' % novel_otu_table_fp))
#    tax_levels = opts.taxonomic_levels.split(',')
#
#    if len(ts_fps) != len(tax_levels):
#        raise ValueError("The number of taxa summary files does not match the "
#                "number of taxonomic levels passed with --taxonomic_levels.")
#    for tax_level, ts_fp in zip(tax_levels, ts_fps):
#        percent_unclassified = summarize_unclassified(open(ts_fp, 'U'))
#        unclassified_report_f.write('%s\t%.2f\n' %
#                                    (tax_level, percent_unclassified))
#    unclassified_report_f.close()


if __name__ == "__main__":
    main()
