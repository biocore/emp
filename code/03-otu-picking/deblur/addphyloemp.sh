#!/bin/bash
# add phylogeny to all emp tables

DATADIR=/home/amam7564/data/emp/process
SCRIPTDIR=/home/amam7564/data/emp/scripts

cd $DATADIR
for ctable in *.table.txt
do
	# remove the .table.txt
	n1=${ctable%.*}
	n2=${n1%.*}
	echo "adding phylogeny to $n2"
	$SCRIPTDIR/AddPhylogeny $n2
	echo "done"
done
