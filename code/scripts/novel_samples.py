#!/usr/bin/env python
from __future__ import division

__author__ = "Jai Ram Rideout"
__copyright__ = "Copyright 2013, The QIIME Project"
__credits__ = ["Jai Ram Rideout"]
__license__ = "GPL"
__version__ = "1.7.0-dev"
__maintainer__ = "Jai Ram Rideout"
__email__ = "jai.rideout@gmail.com"
__status__ = "Development"

from csv import writer

from qiime.util import (get_options_lookup, make_option,
                        parse_command_line_parameters, qiime_open)

from emp.novel_samples import compute_sample_novelty

options_lookup = get_options_lookup()

script_info = {}
script_info['brief_description'] = ""
script_info['script_description'] = ""
script_info['script_usage'] = [('Sample novelty', 'The following command '
'computes the novelty of all samples in the input BIOM tables. A TSV file is '
'created with sample ID, number of novel OTUs, and percent novel sequences. '
'The samples are ordered by descending number of novel OTUs (second column).',
'%prog -i table1.biom,table2.biom -r rep_set.fna -o novel_samples_out.txt')]
script_info['output_description'] = ""

script_info['required_options'] = [
    make_option('-i','--otu_table_fps',type='existing_filepaths',
        help='paths to the input OTU tables (i.e., the output from '
        'make_otu_table.py). These can either be gzipped or uncompressed'),
    make_option('-r','--rep_set_fp',type='existing_filepath',
        help='path to representative set of sequences in the reference '
        'database used in open-reference OTU picking to create the tables '
        'provided via -i/--otu_table_fps. For example, this might be the '
        'Greengenes 97% rep set fasta file'),
    options_lookup['output_fp']
]
script_info['optional_options'] = []
script_info['version'] = __version__

def main():
    option_parser, opts, args = parse_command_line_parameters(**script_info)

    sample_novelty_data = compute_sample_novelty(
            [qiime_open(otu_table_fp) for otu_table_fp in opts.otu_table_fps],
            qiime_open(opts.rep_set_fp), opts.verbose)

    with open(opts.output_fp, 'w') as out_f:
        header = ['SampleID', 'Number of novel OTUs',
                  'Percent novel sequences']
        table_writer = writer(out_f, delimiter='\t', lineterminator='\n')
        table_writer.writerow(header)
        table_writer.writerows(sample_novelty_data)


if __name__ == "__main__":
    main()
