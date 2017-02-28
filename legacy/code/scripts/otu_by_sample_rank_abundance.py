#!/usr/bin/env python
# File created on 21 Aug 2012
from __future__ import division

__author__ = "Greg Caporaso"
__copyright__ = "Copyright 2011, The QIIME project"
__credits__ = ["Greg Caporaso"]
__license__ = "GPL"
__version__ = "1.5.0-dev"
__maintainer__ = "Greg Caporaso"
__email__ = "gregcaporaso@gmail.com"
__status__ = "Development"

from glob import glob
from biom.parse import parse_biom_table
from qiime.util import (parse_command_line_parameters, 
                        make_option, 
                        qiime_open)

script_info = {}
script_info['brief_description'] = ""
script_info['script_description'] = "Summarize the number of samples an OTU shows up in across one or more input OTU tables"
script_info['script_usage'] = [("","","%prog -i \"/Users/caporaso/Dropbox/analysis/isme14/per_study_otu_tables/otu_table_mc2_103[14].biom.gz\"")]
script_info['output_description']= ""
script_info['required_options'] = [
 make_option('-i','--input_glob',type="string",help='the input glob string to match otu tables'),\
]
script_info['optional_options'] = []
script_info['version'] = __version__



def main():
    option_parser, opts, args =\
       parse_command_line_parameters(**script_info)

    input_fps = glob(opts.input_glob)
    d = {}
    for input_fp in input_fps:
        t = parse_biom_table(qiime_open(input_fp))
        for obs_values, obs_id, _ in t.iterObservations():
            if obs_id not in d:
                d[obs_id] = set()
            for i,c in enumerate(obs_values):
                if c > 0:
                    d[obs_id].add(t.SampleIds[i])
    
    for k,v in d.items():
        print '%s\t%s' % (k,'\t'.join(v))


if __name__ == "__main__":
    main()