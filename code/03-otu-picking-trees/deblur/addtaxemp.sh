#!/bin/bash
# add taxonomy to all emp tables

DATADIR=/home/amam7564/data/emp/process
SCRIPTDIR=/home/amam7564/data/emp/scripts

cd $DATADIR
for ctable in *.table.txt
do
	# remove the .table.txt
	n1=${ctable%.*}
	n2=${n1%.*}
	if [ -f $n2.withtax.biom ]; then
		echo "file $n2.withtax.biom exists"
		continue
	fi
	echo "adding taxonomy to $n2"
	$SCRIPTDIR/scripts/TableToTaxBiom.sh $n2
	echo "done"
done
