## methods – Release 2

Computational methods for Release 2 and the EMP500 project are described here. For laboratory methods, please see `protocols`.

### Amplicon sequencing

#### Sequence file demultiplexing

(Do we have a script for this or just manual?)

#### QIIME 2 workflow

Demultiplexed amplicon sequence files are run through [QIIME 2](http://qiime2.org), which wraps many popular amplicon analysis tools, including Deblur, UniFrac, and Emperor.

Initial processing is done using these these QIIME 2 commands:

```bash
# calling ASVs
qiime deblur denoise-16S \
  --i-demultiplexed-seqs SEQUENCES.qza \
  --p-trim-length 150 \
  --output-dir DIRECTORY

# merging feature tables (1..N)
qiime feature-table merge \
  --i-tables DIRECTORY/table-1.qza \
  --i-tables DIRECTORY/table-2.qza \
  --o-merged-table DIRECTORY/table.qza
  
# merging representative sequences (1..N)
qiime feature-table merge-seqs \
  --i-data DIRECTORY/rep-seqs-1.qza \
  --i-data DIRECTORY/rep-seqs-2.qza \
  --o-merged-data DIRECTORY/rep-seqs.qza

# summarizing feature table
qiime feature-table summarize \
  --i-table DIRECTORY/table.qza \
  --m-sample-metadata-file METADATA.tsv \
  --o-visualization DIRECTORY/table.qzv

# summarizing representative sequences
qiime feature-table tabulate-seqs \
  --i-data DIRECTORY/rep-seqs.qza \
  --o-visualization DIRECTORY/rep-seqs.qzv
```

### Shotgun sequencing

#### Sequence file demultiplexing

Shotgun sequence files from Illumina are demultiplexed using bcl2fastq and custom sample sheets, which direct demultiplexed files to directories designated for each PI–study combination. 

* `emp500_s6_sample_sheets.ipynb` - fix sample sheets for four trial shotgun sequencing runs

#### Oecophylla workflow

Demultiplexed shotgun sequence files are run through [Oecophylla](https://github.com/biocore/oecophylla), which is a Snakemake wrapper for a suite of metagenomic analysis and assembly tools.

```bash
OECOPHYLLA COMMANDS HERE
```

### Metabolomics

(See notes from Fernando.)
