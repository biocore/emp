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
from qiime.workflow import call_commands_serially, no_status_updates

from emp_isme14.most_wanted_otus import generate_most_wanted_list

options_lookup = get_options_lookup()

script_info = {}
script_info['brief_description'] = ""
script_info['script_description'] = ""
script_info['script_usage'] = [("", "", "")]
script_info['output_description'] = ""

script_info['required_options'] = [
    make_option('-i','--otu_table_fps',type="existing_filepaths",
        help='paths to the input OTU tables (i.e., the output from '
        'make_otu_table.py). IMPORTANT: each OTU table will be filtered '
        'separately to include OTUs at the specified abundances since we '
        '(computationally) cannot merge the OTU tables before they have been '
        'filtered and collapsed by the mapping category. Thus, this method of '
        'picking most wanted OTUs is not perfect because the OTU will need to '
        'show up in the specified abundance range in at least one per-study '
        'OTU table to even be considered a most wanted candidate.'),
    make_option('-p', '--rep_set_fp', type='existing_filepath',
                help='path to the master representative set fasta file '
                'accompanying the OTU tables. This doesn\'t need to include '
                'GG OTUs (they will be filtered out), but will need all other '
                'rep seqs that are referenced in any of the input OTU tables. '
                'This rep set MUST be a *set*, i.e. no duplicate entries'),
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
        help='[default: %default]', default='SAMPLE_TYPE'),
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
    make_option('--e_value', type='float',
        help='[default: %default]', default=1e-3),
    make_option('--word_size', type='int', help='[default: %default]',
        default=30),
    make_option('--merged_otu_table_fp', type='existing_filepath',
                help='the merged master otu table after being summarized by '
                '--mapping_category. Useful to not have to rerun the entire '
                'analysis from the start if you already have this file. All '
                'workflow steps will be skipped until the filtering of the '
                'merged summarized otu table using --min_categories.',
                default=None),
    make_option('--suppress_taxonomic_output', action='store_true',
        help='Suppress the inclusion of taxonomy strings in the output '
        'tables. If the input OTU tables do not have taxonomic information, '
        'you must enable this option. [default: %default]', default=False),
    make_option('-w', '--print_only', action='store_true',
        help='Print the commands but don\'t call them -- useful for debugging '
        '[default: %default]', default=False),
    make_option('-f', '--force', action='store_true',
        help='Force overwrite of existing output directory (note: existing '
        'files in output_dir will not be removed) [default: %default]',
        default=False),
    options_lookup['jobs_to_start']
]
script_info['version'] = __version__

def main():
    option_parser, opts, args = parse_command_line_parameters(**script_info)

    if opts.print_only:
        command_handler = print_commands
    else:
        command_handler = call_commands_serially

    if opts.verbose:
        status_update_callback = print_to_stdout
    else:
        status_update_callback = no_status_updates

    generate_most_wanted_list(opts.output_dir, opts.otu_table_fps,
            opts.rep_set_fp, opts.gg_fp, opts.nt_fp, opts.mapping_fp,
            opts.mapping_category, opts.top_n, opts.min_abundance,
            opts.max_abundance, opts.min_categories, opts.max_gg_similarity,
            opts.e_value, opts.word_size, opts.merged_otu_table_fp,
            opts.suppress_taxonomic_output, opts.jobs_to_start,
            command_handler, status_update_callback, opts.force)


if __name__ == "__main__":
    main()
