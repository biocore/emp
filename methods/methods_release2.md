## methods – Release 2

Computational methods for Release 2 and the EMP500 project are described here. For laboratory methods, see [`protocols`](https://github.com/biocore/emp/tree/master/protocols).

### 1 Sample collection and processing

#### 1.1 Solicitation of samples and EMPO

We had funding to do metagenomic sequencing on ~500 samples. We solicited samples from the EMP consortium spanning a wide range of microbial environments. To achieve even coverage across microbial environments, we devised sample ontology of sample types (microbial environments), which would eventually become the [EMP ontology (EMPO)](http://www.earthmicrobiome.org/protocols-and-standards/empo/). Around 800 samples were ultimately collected, which allows for reshaping of the dataset to deal with poorly performing samples.

#### 1.2 Metadata

Metadata were requested to comply with MIMS and Qiita standards; please refer to the EMP500 [metadata guide](http://press.igsb.anl.gov/earthmicrobiome/protocols-and-standards/metadata-guide/). Excel templates were provided corresponding to 15 MIxS environmental packages. The completed spreadsheets were collected from collaborators and checked for completeness and standardized. Individual metadata files are merged, then EMPO and other sample metadata were added, and finally prep information and mapping files were generated.

#### 1.3 Replicates

Samples were either collected fresh or requisitioned from existing bulk samples. Aliquots (10) of each raw sample were requested. This allows for minimal freeze-thaw cycles and multiple downstream processing protocols in the future. Instructions were provided in the EMP500 [sample submission guide](http://www.earthmicrobiome.org/in-progress/emp500-sample-submission-guide/). QR barcodes were added subsequently as described in [`protocols`](https://github.com/biocore/emp/tree/master/protocols).

#### 1.4 Processing rounds

Because samples were collected in sets of 10 aliquots, individual aliquots can be processed on-demand as more material is needed.

##### DNA Extraction Round 1

One aliquot was used for DNA extractions performed at UCSD in June/July 2016 (Plates 1-5) and December 2016 (Plates 6-7), and at PNNL in September 2016 (Plates 8-9). Plate and well information is contained in the metadata files under the following columns: plate_no_round1, well_no_round1, well_id_round1, well_row_round1, well_column_round1.

##### Metabolite Extraction Round 1

One aliquot was used for metabolite extractions performed at UCSD in July 2016 (Plates 2-5). Data were collected in April 2017. Sample IDs for metabolomics are contained in the metadata files under the following column: metab_id_2017.

##### DNA Extraction Round 2

Two aliquots (for most samples) were used for DNA extractions performated at UCSD in February 2018 (corresponding to Round 1 Plates 1-7).

### 2 Amplicon sequencing

#### 2.1 Sequence file demultiplexing

(Do we have a script for this or just manual?)

#### 2.2 QIIME 2 workflow

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

### 3 Shotgun sequencing

#### 3.1 Sequence file demultiplexing

Shotgun sequence files from Illumina were demultiplexed using bcl2fastq and custom sample sheets, with demultiplexed files placed in directories designated for each PI–study combination. 

#### 3.2 Oecophylla workflow

Demultiplexed shotgun sequence files are run through [Oecophylla](https://github.com/biocore/oecophylla), which is a Snakemake wrapper for a suite of metagenomic analysis and assembly tools.

```bash
OECOPHYLLA COMMANDS HERE
```

### 4 Metabolomics

(See notes from Fernando.)
