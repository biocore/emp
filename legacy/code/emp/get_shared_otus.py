from __future__ import division
from biom.parse import parse_biom_table
from numpy import inf
from qiime.util import qiime_open
import os
from glob import glob

__author__ = "Luke Ursell"
__copyright__ = "Copyright 2011, The QIIME Project"
__credits__ = ["Luke Ursell, Yoshiki Baeza"]
__license__ = "GPL"
__version__ = "1.5.0-dev"
__maintainer__ = "Luke Ursell"
__email__ = "lkursell@gmail.com"
__status__ = "Development"


def get_biom_tables(otu_table_dir):
    """Pass in a directory containing biom tables, either .biom or .biom.gz
    Returns a list of biom table objects"""

    otu_tables_fp = glob("%s/*biom*" % otu_table_dir) # look for both .biom and .biom.gz
    biom_table_objects = []
    for otu_table in otu_tables_fp:
        biom_table = parse_biom_table(qiime_open(otu_table)) # qiime_open will open .biom and .biom.gz files
        biom_table_objects.append(biom_table)
    return biom_table_objects

def get_shared_otus(biom_tables,min_count,percentage):
    """ Moves through a list of biom tables, returns OTUs that have at least some minimum count
    that are present in a minimum percentage of samples across ALL of the biom tables

    Pass:
    biom_tables = a list of biom_table objects 
    min_count = the minimum count for each sample required to be counted (int)
    percentage = an int from 0.0 = 1.0, defines the minimum percentage of total samples across all
        otu tables that must contain that otu at a given minimum count (above) to be counted

    Returns:
    A list of output lines to be written, i.e. ['OTU_ID\tMin_count\tPercentage\n', '1\t2\t1.0\n', '3\t2\t0.666666666667\n']"""

    # create dictionaries to put the taxa ids and counts
    d_ids_counts = {}
    
    # counts samples to calculate percentage of samples later
    sample_counter = 0

    for biom_table in biom_tables:
        #print biom_table
        # get ids, vals, and taxonomy string from otu table
        obs_ids = []
        obs_vals = []
        obs_metadata = []
        for o_val, o_id, o_md in biom_table.iterObservations():
            #print o_val, o_id, o_md
            obs_vals.append(o_val)
            obs_metadata.append(o_md)
            obs_ids.append(o_id)

        sample_counter += int(len(biom_table.SampleIds))
        #print "samplecounter",sample_counter
        
        # walk through all counts/samples, update dict of d_ids_counts if val is greater/equal to min_count
        for i,id in enumerate(obs_ids):
            if id not in d_ids_counts:
                d_ids_counts[id] = 0 
            for  val in obs_vals[i]:
                if int(val) >= int(min_count):
                    d_ids_counts[id] += 1
   
    # calc min percentage based on input parameter
    min_sample_percentage = float(percentage * sample_counter)
    
    # pull out otus that meet minimum count and sample percentage over ALL tables
    otus = [taxa for taxa,count in d_ids_counts.items() if count >= min_sample_percentage]

    output_lines = []
    # if otu list is empty
    if not otus:
        output_lines.append("No taxa are shared")

    # if otu list is NOT empty
    if otus:
        output_lines.append("OTU_ID" + '\t' "Min_count" + '\t' + "Percentage" + '\n')
        for otu in otus:
            actual_percentage = d_ids_counts[otu] / sample_counter
            output_result = str(otu) + '\t' + str(min_count) + '\t' + str(actual_percentage) + '\n'     
            output_lines.append(output_result)

    return output_lines

def write_shared_otus_results(results_fp,output_lines):
    """Write output lines to results_fp

    Pass: absolute filepath of results.txt file to be written, and output_lines from get_shared_otus
    Returns: results file with output lines"""
    
    results_file = open(results_fp,'w')
    for line in output_lines:
        results_file.writelines(line)
    results_file.close()





