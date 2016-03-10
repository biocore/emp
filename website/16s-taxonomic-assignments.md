Standard EMP Protocol for Mapping 16S rRNA V4 Data to Reference Sequence Databases Using QIIME
==============================================================================================

### Version: 5 Jun 2012

Updates 9 Mar 2016:

-   QIIME command is now pick\_closed\_reference\_otus.py.
-   See this [paper](https://peerj.com/articles/545/) for more
    information on the pros and cons of open and closed reference OTU
    picking.

Quality filtering and demultiplexing
------------------------------------

Input sequences and Phred scores are provided to
split\_libraries\_fastq.py, and demultiplexed/quality filtered using its
default parameters. On a per-read basis, quality filtering works as
follows:

1.  Identify the first quality score below Q3 and truncate the read just
    prior to that position.
2.  Determine if the truncated sequence is at least 75% of the length of
    the input sequence: if yes, retain the truncated read; if no,
    discard the read.
3.  Determine if the truncated sequence has any N (i.e., ambiguous base
    call) characters: if yes, discard the read; if no, retain the read.

Closed-reference OTU picking
----------------------------

97% OTUs are picked in the initial EMP analyses using a closed-reference
OTU picking protocol against the Greengenes database pre-clustered at
97% identify (this Greengenes reference collection build is available
here:
<http://greengenes.lbl.gov/Download/Sequence_Data/Fasta_data_files/Caporaso_Reference_OTUs/gg_otus_4feb2011.tgz>.
This is done using pick\_closed\_reference\_otus.py. This process works
as follows. Reads are pre-sorted by abundance in QIIME so the most
frequently occurring sequences will be chosen as OTU centroid sequences.
Each read is then searched against the Greengenes reference sequences
using reference-based uclust version 1.2.22. The call to uclust issued
by QIIME looks like:
`uclust --id 0.97 --w 12 --stepwords 20 --usersort --maxaccepts 20 --libonly --stable_sort --maxrejects 500`
Reads which hit a sequence in the reference collection at greater than
or equal to 97% identity are assigned to an OTU defined by the reference
sequence they match. Reads which fail to hit a reference sequence at at
least 97% identity are discarded. Taxonomy is assigned to each OTU based
on the reference sequence defining that OTU, and the Greengenes
reference tree (also provided in the reference collection build linked
above) can then be used for pylogenetic diversity analyses.
Closed-reference OTU picking has pros and cons, and future EMP runs will
apply the open-reference OTU picking process described here:
<http://qiime.org/tutorials/open_reference_illumina_processing.html#option-2-subsampled-open-reference-otu-picking>
The pros of closed-reference OTU picking are that it is fully
parallelizable, which is important for data sets of this scale, and that
the OTUs are defined by trusted reference sequences. It additionally
serves as a quality control filter: erroneous reads will likely be
discarded as not hitting the reference data set. The primary con of
closed-reference OTU picking is that sequences that are not already
known (i.e., represented in the reference data set) will be excluded.
