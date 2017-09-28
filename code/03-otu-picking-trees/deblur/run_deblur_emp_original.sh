# Prepare the EMP deblurred tables
# requires QIIME 1.9
# Note: Set the directories in the debluremp.sh, debluremp.90.sh, addtaxemp.sh

# deblur the data for length 100,150
# (best to submit to some queue)
./debluremp.sh

# deblur the data for length 90
# (best to submit to some queue)
./debluremp.90.sh

# note everything is created in emp/process/

# all deblurred samples are in all150/ (length 150) and all100/ (length 100)
# also have a biom table for each studyid: XXX.100.clean.table.txt or 150


# create the tables:
scripts/CreateTable.py -l -s -d all100 -o emp.all.100.clean
scripts/CreateTable.py -l -s -d all100 -o emp.all.min25.100.clean -m 25
scripts/CreateTable.py -l -s -d all150 -o emp.all.150.clean
scripts/CreateTable.py -l -s -d all150 -o emp.all.min25.150.clean -m 25

# add taxonomy to tables using qiime RDP
scripts/addtaxnew.sh emp.all.100.clean
scripts/addtaxnew.sh emp.all.min25.100.clean
scripts/addtaxnew.sh emp.all.150.clean
scripts/addtaxnew.sh emp.all.min25.150.clean

# add taxonomy to per study tables
./addtaxemp.sh


# create the phylogenetic trees (de-novo)
./addphyloemp.sh

# Filter the biom table to keep only features present in the tree
scripts/filterbiombytree.py -t emp.90.min25.deblur.tre -i emp.all90.min25.withtax.biom -o emp.90.min25.deblur.onlytree.biom
scripts/filterbiombytree.py -t emp.100.min25.deblur.tre -i emp.all100.min25.withtax.biom -o emp.100.min25.deblur.onlytree.biom
scripts/filterbiombytree.py -t emp.150.min25.deblur.tre -i emp.all150.min25.withtax.biom -o emp.150.min25.deblur.onlytree.biom
