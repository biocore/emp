#!/bin/bash
# amnonscript
# add taxonomy to the output of deblurring
# input
# $1 - the biom table name (without .biom)

# prepare the rdp classifier
echo "preparing the rdp classifier..."
module load rdp_classifier_2.2
export RDP_JAR_PATH=/opt/rdp_classifier/2.2/rdp_classifier-2.2.jar
# get RDP taxonomy for each sequence
echo "assigning taxonomy in directory: " taxbiom "-$1"
assign_taxonomy.py -i $1.seqs.fa -m rdp -o taxbiom-$1
# add header line to output:
echo "Copying header files"
#cp ~/data/other/taxheader.txt taxbiom-$1/withheader.txt
printf "#OTUID\ttaxonomy\tconfidence\n" > taxbiom-$1/withheader.txt
cat taxbiom-$1/$1.seqs_tax_assignments.txt >> taxbiom-$1/withheader.txt
# add the taxonomy data to the biom table
echo "Adding the taxonomy to biom table: " $1 ".withtax.biom"
biom add-metadata -i $1.biom -o $1.withtax.biom --observation-metadata-fp taxbiom-$1/withheader.txt --observation-header OTUID,taxonomy --sc-separated taxonomy
