#!/bin/bash

# Prepare the EMP deblurred biom table using the current deblur release

# the sequence length to trim to
LENGTH=150

DATADIR=/projects/emp/02-adapter-clean-up
LOCDIR=/home/amam7564/data/emp/deblur
FNAME=filtered_seqs.fna

cd $LOCDIR
mkdir all
for cdir in $DATADIR/*
do
	studyname=$(basename $cdir)
	echo "processing study $studyname"
	sfile=$cdir/$FNAME
	cp $sfile .
	# deblur keeping the temp. files, so we can combine the per sample fasta files to one directory
	deblur workflow --seqs-fp $FNAME --output-dir deblur -w -t $LENGTH -O 32 --min-reads 1
	cp deblur/all.biom all/$studyname.biom
	cp deblur/all.seqs.fa all/$studyname.seqs.fa

	rm -r deblur
	rm $FNAME
	echo "done processing $studyname"
done

# merge to a single biom table
TABLES=`ls -m all/*.biom`
TABLES_NO_SPACE="$(echo -e "${TABLES}" | tr -d '[:space:]')"
merge_otu_tables -i $TABLES_NO_SPACE -o all.biom
