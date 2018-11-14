## methods – Release 2

Computational methods for Release 2 and the EMP500 project are described here. For laboratory methods, see [`protocols`](https://github.com/biocore/emp/tree/master/protocols).

### 0 Metadata

The metadata workflow—from individual study metadata files, general sample information, and prep information to mapping files, sample information files, and prep information files—is summarized by these IPython notebooks:

* `emp500_s1_merge_sample_info.ipynb` Merge individual study metadata Excel files, add general prep information (including plate and well numbers for the initial DNA extraction), generate sample information file and basic mapping file. Outputs:
    - `emp500_sample_information.tsv`
    - `emp500_basic_map.tsv`
* `emp500_s2_add_prep_info_sample_names.ipynb` Add prep information (16S, 18S, ITS) and sample information (sample names, study information, EMPO categories, etc.). Outputs:
    - `emp500_prep_information_general.xlsx`
    - `emp500_prep_information_*.xlsx` (prep info files for each of Round 1 runs)
* `emp500_s3_make_mapping_files_prep_info.ipynb` Generate mapping files and prep information files.
* `emp500_s4_project_summary.ipynb` Generate project summary and list of samples (for labels).
* `emp500_s5_labels.ipynb` Generate label spreadsheet with QR codes (not encoded).

### 1 Amplicon sequencing

#### 1.1 Sequence file demultiplexing

Illumina HiSeq sequence files were demultiplexed using Qiita.

#### 1.2 QIIME 2 workflow

Demultiplexed amplicon sequence files were run through [QIIME 2](http://qiime2.org), which wraps many popular amplicon analysis tools, including Deblur, UniFrac, and Emperor.

Initial processing was done using these these QIIME 2 commands:

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

### 2 Shotgun sequencing

#### 2.1 Sequence file demultiplexing

Shotgun sequence files from Illumina were demultiplexed using bcl2fastq and custom sample sheets, with demultiplexed files placed in directories designated for each PI–study combination. 

#### 2.2 Oecophylla workflow

Demultiplexed shotgun sequence files are run through [Oecophylla](https://github.com/biocore/oecophylla), which is a Snakemake wrapper for a suite of metagenomic analysis and assembly tools.

### 3 Metabolomics

(to be provided)
