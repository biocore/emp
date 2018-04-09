## methods – Release 2

Computational methods for Release 2 and the EMP500 project are described here. For laboratory methods, see [`protocols`](https://github.com/biocore/emp/tree/master/protocols).

### 1 Sample collection and processing

#### 1.1 Solicitation of samples and EMPO

We had funding to do metagenomic sequencing on ~500 samples. We solicited samples from the EMP consortium spanning a wide range of microbial environments. To achieve even coverage across microbial environments, we devised sample ontology of sample types (microbial environments), which would eventually become the EMP ontology ([EMPO](http://www.earthmicrobiome.org/protocols-and-standards/empo/)). Around 800 samples were ultimately collected, which allows for reshaping of the dataset to deal with poorly performing samples.

#### 1.3 Metadata

Metadata were requested to comply with MIMS and Qiita standards (please refer to the EMP500 [metadata guide](http://press.igsb.anl.gov/earthmicrobiome/protocols-and-standards/metadata-guide/)). Excel templates were provided corresponding to 15 MIxS environmental packages. The completed spreadsheets were collected from collaborators and checked for completeness and standardized. Individual metadata files are merged in notebook "s1", EMPO and other sample metadata are added in notebook "s2", and prep information and mapping files are added in notebook "s3", below.

#### 1.2 Replicates

Samples were either collected fresh or requisitioned from existing bulk samples. Aliquots (10) of each raw sample were requested. This allows for minimal freeze-thaw cycles and multiple downstream processing protocols in the future. Instructions were provided in the EMP500 [sample submission guide](http://www.earthmicrobiome.org/in-progress/emp500-sample-submission-guide/). QR barcodes were added subsequently as described in [`protocols`](https://github.com/biocore/emp/tree/master/protocols). Code for generating these codes and other label information in an Excel spreadsheet is in notebooks "s4" and "s5" below.

#### 1.4 Processing rounds

Replicate 1 was used for xxx.

Replicates 2 and 3 were used for xxx.

### 2 Metadata

The metadata workflow -- from individual study metadata files, general sample information, and prep information -- to mapping files, sample information files, and prep information files -- is summarized by these IPython notebooks:

* `emp500_s1_merge_sample_info.ipynb` - merge individual study metadata files, add general prep information (including plate and well numbers for the initial DNA extraction), generate sample information file
* `emp500_s2_add_prep_info_sample_names.ipynb` - add prep information (16S, 18S, ITS) and sample information (sample names, study information, EMPO categories, etc.)
* `emp500_s3_make_mapping_files_prep_info.ipynb` - generate mapping files and prep information files
* `emp500_s4_project_summary.ipynb` - generate project summary and list of samples (for labels)
* `emp500_s5_labels.ipynb` - generate label spreadsheet with QR codes (not encoded)

### 3 Processing rounds - DNA/metabolite extraction and sequencing/mass spec

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
