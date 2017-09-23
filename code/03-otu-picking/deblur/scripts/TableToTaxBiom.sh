#!/bin/bash
# amnonscript
# split the unassigned reads file to phix reads and non phix reads
# input:
# $1 - name of the unassigned.fa file
# output:
# $1.phix.fa - the phix reads
# $1.nonphix.fa - the non-phix reads

# convert to biom table:
echo "converting " $1 " to biom table: " $1 ".biom"
biom convert -i $1.table.txt -o $1.biom --table-type "OTU table" --to-json
# prepare the rdp classifier
echo "preparing the rdp classifier..."
module load rdp_classifier_2.2
export RDP_JAR_PATH=/opt/rdp_classifier/2.2/rdp_classifier-2.2.jar
# get RDP taxonomy for each sequence
echo "assigning taxonomy in directory: " taxbiom "-$1"
assign_taxonomy.py -i $1.seq.fa -m rdp -o taxbiom-$1
# add header line to output:
echo "Copying header files"
cp ~/data/other/taxheader.txt taxbiom-$1/withheader.txt
cat taxbiom-$1/$1.seq_tax_assignments.txt >> taxbiom-$1/withheader.txt
# add the taxonomy data to the biom table
echo "Adding the taxonomy to biom table: " $1 ".withtax.biom"
biom add-metadata -i $1.biom -o $1.withtax.biom --observation-metadata-fp taxbiom-$1/withheader.txt --observation-header OTUID,taxonomy --sc-separated taxonomy
# and convert to json
echo "Converting to json: " $1 ".withtax.json.biom"
biom convert -i $1.withtax.biom -o $1.withtax.json.biom --header-key "taxonomy" --table-type "OTU table" --to-json
# and txt
echo "Converting to txt table: " $1 ".withtax.txt.biom"
biom convert -i $1.withtax.biom -o $1.withtax.txt.biom --header-key "taxonomy" --table-type "OTU table" --to-tsv
