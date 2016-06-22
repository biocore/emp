#!/bin/bash
#
#-----------------------------------------------------------------------------
# Copyright (c) 2016--, Evguenia Kopylova.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------

# BIOM table
input_biom_fp=$1
# output directory path
output_dp=$2
# comma separated list of depths
rarefaction_depths_string="$3"
# qsub command
qsub_cmd="-l nodes=1:ppn=1 -l walltime=10:00:00 -l mem=300gb -l pmem=300gb"

mkdir -p $output_dp
IFS=',' read -r -a rarefaction_depths <<< "$3"

for depth in "${rarefaction_depths[@]}"
do
    biom_base=$(basename "$input_biom_fp" .biom)
    if [ ! -s $output_dp/${biom_base}_$depth.biom ]; then
        echo "single_rarefaction.py -i $input_biom_fp -o $output_dp/${biom_base}_$depth.biom -d $depth" | qsub $qsub_cmd -N rarefaction_$depth
        sleep 5
    fi
done

