#!/bin/bash

# amnonscript
# create a phylogenetic tree for a deblurred biom table fasta file
# input:
# $1 - text biom table name (without the .table.txt)


# align the sequences using the core set
echo "Creating tree for $1"
echo "alignening sequences"
align_seqs.py -i $1.seqs.fa -o $1.pynast_aligned_seqs --template_fp /home/amam7564/data/gg/core_set_aligned.fasta.imputed
echo "filtering alignment"
filter_alignment.py -o $1.pynast_aligned_seqs -i $1.pynast_aligned_seqs/$1.seqs_aligned.fasta
# and make the phylogenetic tree
echo "creating the tree"
make_phylogeny.py -i $1.pynast_aligned_seqs/$1.seqs_aligned_pfiltered.fasta -o $1.tre
echo "tree created in $1.tre"
