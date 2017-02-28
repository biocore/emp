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

from qiime.util import (parse_command_line_parameters, get_options_lookup,
                        make_option)

from emp.alpha_diversity_by_sample_type import (
        alpha_diversity_by_sample_type)

options_lookup = get_options_lookup()

script_info = {}
script_info['brief_description'] = ""
script_info['script_description'] = ""
script_info['script_usage'] = [("Summarize alpha diversity by environment",
"Create a plot (in PDF format) with boxplots for each environment type. Each "
"boxplot contains all alpha diversity measures (observed species) for all "
"samples in the environment type.", "%prog -i os_1.txt,os_2.txt -m map.txt "
"-c Environment -o os_by_environment.pdf")]
script_info['output_description'] = ""

script_info['required_options'] = [
    make_option('-i', '--alpha_div_fps', type='existing_filepaths',
                help='alpha diversity filepaths for a SINGLE metric, i.e. the '
                'output of alpha_diversity.py. All files should have the '
                'same single metric. Overlapping sample IDs between the '
                'files are allowed and will simply be added onto their '
                'respective sample type'),
    options_lookup['mapping_fp'],
    options_lookup['output_fp']
]
script_info['optional_options'] = [
    make_option('-c', '--mapping_category', type='string',
                help='', default='Sample_Type'),
    make_option('-n', '--min_num_samples', type='int',
                help='', default=11),
    make_option('-e', '--category_values_to_exclude', type='string',
                help='comma-separated list of values within '
                '--mapping_category to exclude from the plots', default='NA')
]
script_info['version'] = __version__

def main():
    option_parser, opts, args = parse_command_line_parameters(**script_info)

    adiv_fs = [open(adiv_fp, 'U') for adiv_fp in opts.alpha_div_fps]

    plotting_data, plot_fig = alpha_diversity_by_sample_type(
            adiv_fs, open(opts.mapping_fp, 'U'), opts.mapping_category,
            opts.min_num_samples, opts.category_values_to_exclude.split(','))
    plot_fig.savefig(opts.output_fp)


if __name__ == "__main__":
    main()
