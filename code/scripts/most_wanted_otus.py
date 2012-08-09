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

from os.path import join

from qiime.util import (parse_command_line_parameters, get_options_lookup,
                        make_option)

from emp_isme14.most_wanted_otus import generate_most_wanted_list

options_lookup = get_options_lookup()

script_info = {}
script_info['brief_description'] = ""
script_info['script_description'] = ""
script_info['script_usage'] = [("", "", "")]
script_info['output_description'] = ""

script_info['required_options'] = [
    options_lookup['otu_table_as_primary_input'],
    make_option('-p', '--rep_set_fp', type='existing_filepath',
                help=''),
    make_option('-r', '--gg_fp', type='existing_filepath',
                help='the greengenes rep set fasta filepath'),
    make_option('-t', '--nt_fp', type='existing_filepath',
                help='the NCBI nt db filepath, MUST already be '
                'blast-formatted with formatdb'),
    options_lookup['mapping_fp'],
    options_lookup['output_dir']
]
script_info['optional_options'] = [
    make_option('-c', '--mapping_category', type='string',
        help='[default: %default]', default='Sample_Type'),
    make_option('-n', '--top_n', type='int', help='[default: %default]',
        default=100),
    make_option('--min_abundance', type='int', help='[default: %default]',
        default=100),
    make_option('--max_abundance', type='int', help='[default: %default]',
        default=500),
    make_option('--min_categories', type='int', help='[default: %default]',
        default=4),
    make_option('--max_gg_similarity', type='float',
        help='[default: %default]', default=0.80),
    options_lookup['jobs_to_start']
]
script_info['version'] = __version__

def main():
    option_parser, opts, args = parse_command_line_parameters(**script_info)

    generate_most_wanted_list(
            opts.otu_table_fp, opts.rep_set_fp, opts.gg_fp, opts.nt_fp,
            opts.mapping_fp, opts.mapping_category, opts.top_n,
            opts.min_abundance, opts.max_abundance, opts.min_categories,
            opts.max_gg_similarity, opts.jobs_to_start, opts.output_dir)


if __name__ == "__main__":
    main()
