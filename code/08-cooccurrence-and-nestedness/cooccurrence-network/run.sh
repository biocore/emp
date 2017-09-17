#!/usr/bin/env bash

# Copyright 2016 IBM Corp. 
# Robert J. Prill <rjprill@us.ibm.com>
#
# Runs a series of step starting from a BIOM file and ending
# with the OTU co-occurrence network.

source /macqiime/configs/bash_profile.txt

# ##################################################

BIOM=emp_deblur_90bp.subset_2k.rare_5000.biom
MAP=emp_qiime_mapping_subset_2k.txt
OUTDIR='output'

# ##################################################
# convert BIOM file to TSV file, row metadata file, column metadata file

if [ ! -d "$OUTDIR" ]; then
  mkdir -p $OUTDIR
fi

echo "running biom summarize-table"
biom summarize-table \
-i data/$BIOM \
-o $OUTDIR/$BIOM.SUMMARY.txt

echo "converting biom to biom.json format"
biom convert \
-i data/$BIOM \
-o $OUTDIR/$BIOM.json \
--table-type="OTU table" \
--to-json

echo "converting biom.json to tsv"
script/biom_json_to_tsv.rb \
$OUTDIR/$BIOM.json \
$OUTDIR

echo "computing OTU co-occurrence network"
script/otu_cooccurrence_network.R

echo "$OUTDIR/otu-co-occurrence-network-z20.txt can be visualized in Cytoscape"
echo "$OUTDIR/row_metadata.txt can be used to color nodes by attributes in Cytoscape"

