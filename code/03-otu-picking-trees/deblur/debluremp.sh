#!/bin/bash
# deblur all emp studies (from per study post split-libraries files)
# NOTE: requires qiime 1.9 split_sequence_file_on_sample_ids.py command
# NOTE: set directories as required at beginning of script

DATADIR=/projects/emp/02-adapter-clean-up
LOCDIR=/home/amam7564/data/emp/process
SCRIPTDIR=/home/amam7564/data/emp/scripts
FNAME=filtered_seqs.fna

cd $LOCDIR
mkdir all100
mkdir all150
for cdir in $DATADIR/*
do
	studyname=$(basename $cdir)
	echo "processing study $studyname"
	sfile=$cdir/$FNAME
	cp $sfile .
	split_sequence_file_on_sample_ids.py -i $FNAME -o splitdir
	$SCRIPTDIR/CleanIndelDirParallel.py splitdir -l 150 -e 0.02 -n 25 -m 0.005 -d 1,0.06,0.02,0.02,0.01,0.005,0.005,0.005,0.001,0.001,0.001,0.0005
	cp splitdir/*.ref.fa all150
	$SCRIPTDIR/CreateTable.py -l -s -d splitdir -o $studyname.150.clean
	$SCRIPTDIR/CleanIndelDirParallel.py splitdir -l 100 -e 0.02 -n 25 -m 0.005 -d 1,0.06,0.02,0.02,0.01,0.005,0.005,0.005,0.001,0.001,0.001,0.0005
	cp splitdir/*.ref.fa all100
	$SCRIPTDIR/scripts/CreateTable.py -l -s -d splitdir -o $studyname.100.clean
	rm -r splitdir
	rm $FNAME
	echo "done processing $studyname"
done
