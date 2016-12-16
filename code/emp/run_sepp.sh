#!/bin/bash  

# USAGE: run_sepp.sh [input fragments file] [output prefix]
# Assumes SEPP is installed and run_sepp.py is part of the PATH

# Should point to a fast tmp location which may be removed after the run
tmpssd=`mktemp -d`
#tmpssd=/scratch/$USER/$PBS_JOBID

# Should point to a (semi) permanent tmp for keeping the important parts of the results 
#tmp=/oasis/scratch/$USER/temp_project/sepp/$PBS_JOBID
#mkdir $tmp
tmp=`mktemp -d`


# Input sequence file
f=$1
#bp=150; f=emp.$bp.min25.deblur.withtax.onlytree.fna

# SEPP placement and alignment subset sizes
p=5000
a=1000

# Name of the output file prefix (inlcuding directory if needed)
name=$2
#name=emp$bp.${p}_${a}_rxbl

# Reference tree
t='reference-gg-raxml-bl.tre'
# Reference alignment
alg='gg_13_5_ssu_align_99_pfiltered.fasta'
# RAxML info file generated when creating the reference RAxML tree
rxi='RAxML_info-reference-gg-raxml-bl.info'

run_sepp.py -P $p -A $a -t $t -a $alg -r $rxi -f $f -x 16 -cp $tmpssd/chpoint-$name -o $name -d $tmp/ -p $tmpssd 1>sepp-$name-out.log 2>sepp-$name-err.log

cp -r $tmpssd $tmp;

cp $tmp/${name}_placement.json .

~/.sepp/bundled-v3.1/guppy tog ${name}_placement.json

~/.sepp/bundled-v3.1/guppy tog --xml ${name}_placement.json
