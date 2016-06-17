#!/bin/bash
#
#-----------------------------------------------------------------------------
# Copyright (c) 2016--, Evguenia Kopylova.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------

gg_alpha_diversity_dp=$1
si_alpha_diversity_dp=$2
compute_sample_div_script_fp=$3
iqr_offset=$4
keep_unique_samples="$5"
metrics=('PD_whole_tree' 'chao1' 'observed_otus' 'shannon')
sampling_depths=('1000' '10000' '100000' '1000000')

printf "\t"
for metric in "${metrics[@]}"
do
	printf $metric"\t"
done
printf "\n"
for depth in "${sampling_depths[@]}"
do
	printf $depth"\t"
	for metric in "${metrics[@]}"
	do
		if [[ ! -s $gg_alpha_diversity_dp/"alpha_div_even${depth}.txt" ]]; then
			printf "N/A\t"
			continue
		fi
		if [[ ! -s $si_alpha_diversity_dp/"alpha_div_even${depth}.txt" ]]; then
			printf "N/A\t"
			continue
		fi
		outlier=$(python $compute_sample_div_script_fp $gg_alpha_diversity_dp/"alpha_div_even${depth}.txt" $si_alpha_diversity_dp/"alpha_div_even${depth}.txt" $metric ${iqr_offset} "${keep_unique_samples}")
		printf "$outlier%%"
		printf "\t"
	done
	printf "\n"
done