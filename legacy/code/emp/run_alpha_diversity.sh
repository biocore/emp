#!/bin/bash
#
#-----------------------------------------------------------------------------
# Copyright (c) 2016--, Evguenia Kopylova.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------

# directory with rarefied BIOM tables
input_rarefied_biom_dp=$1
# tree
tree_fp=$2
# output directory path
output_dp=$3
# alpha diversity metrics (comma separated list)
alpha_metrics=$4
# qsub command
qsub_cmd="-l nodes=1:ppn=1 -l walltime=10:00:00 -l mem=400gb -l pmem=400gb"

mkdir -p $output_dp

for file in ${input_rarefied_biom_dp}/*.biom
do
    input_biom_fp=$file
    biom_base=$(basename "$input_biom_fp" .biom)
    if [ ! -s $output_dp/${biom_base}.txt ]; then
        echo "alpha_diversity.py -i $input_biom_fp -o $output_dp/${biom_base}.txt -m $alpha_metrics -t $tree_fp" | qsub $qsub_cmd -N alpha_${biom_base}
        sleep 5
    fi
done