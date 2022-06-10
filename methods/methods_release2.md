## methods – 16S Release 2 and Multi-omics (EMP500)

<div style="float: right; margin-left: 30px;"><img title="The EMP logo was designed by Eamonn Maguire of Antarctic Design." style="float: right;margin-left: 30px;" src="https://upload.wikimedia.org/wikipedia/en/4/4f/EMP-green-small.png" align=right /></div>

Computational methods for EMP 16S Release 2 and the EMP Multi-omics project (EMP500) are described here. For laboratory methods, see [`protocols`](https://github.com/biocore/emp/tree/master/protocols).

<!--made with https://luciopaiva.com/markdown-toc/ -->

# Table of contents

  - [0 Metadata](#0-metadata)
  - [1 Amplicon sequencing](#1-amplicon-sequencing)
    - [1.1 16S rRNA gene data](#11-16s-rna-gene-data)
    - [1.2 18S rRNA gene data](#12-18s-rna-gene-data)
    - [1.3 Fungal ITS data](#13-fungal-its-data)
  - [2 Shotgun sequencing](#2-shotgun-sequencing)
    - [2.1 Short-read analysis](#21-short-read-analysis)
      - [2.1.1 Sequence file demultiplexing](#211-sequence-file-demultiplexing)
      - [2.1.2 Adapter trimming and poly-G removal](#212-adapter-trimming-and-poly-g-removal)
      - [2.1.3 Qiita read alignment to the Woltka reference database](#213-qiita-read-alignment-to-woltka-reference-database)
      - [2.1.4 Woltka gOTU feature-table generation](#214-woltka-gotu-feature-table-generation)
    - [2.2 Metagenomic assembly and binning](#22-metagenomic-assembly-and-binning)
      - [2.2.1 Assembly and co-assembly of EMP500 samples within each environment](#221-assembly-and-co-assembly-of-emp500-samples-within-each-environment)
      - [2.2.2 Binning of assemblies to generate MAGs for each environment](#222-binning-of-assemblies-to-generate-mags-for-each-environment)
      - [2.2.3 Functional annotation of assemblies](#223-functional-annotation-of-assemblies)
      - [2.2.4 Taxonomic profiling of MAGs](#224-taxonomic-profiling-of-mags)
  - [3 Metabolomics data analysis](#3-metabolomics-data-analysis)
    - [3.1 Non targeted mass spectrometry analysis by LC-MS](#31-non-targeted-mass-spectrometry-analysis-by-lc-ms)
      - [3.1.1 Data conversion and desposition](#311-data-conversion-and-desposition)
      - [3.1.2 Data analysis and annotation](#312-data-analysis-and-annotation)
          - [3.1.2.1 Feature based molecular networking workflow](#3121-feature-based-molecular-networking-workflow)
          - [3.1.2.2 Classical molecular networking workflow](#3122-classical-molecular-networking-workflow)
    - [3.2 Non-targeted mass spectrometry analysis by GC-MS](#32-non-targeted-mass-spectrometry-analysis-by-gc-ms)
      - [3.2.1 Data conversion and deposition](#321-gc-data-conversion-and-deposition)
      - [3.2.2 Data analysis and annotation](#322-data-analysis-and-annotation)
          - [3.2.2.1 PNNL GC-MS pipeline](#3221-pnnl-gc-ms-pipeline)
          - [3.2.2.2 GNPS GC-MS pipeline](#3222-gnps-gc-ms-pipeline)
  - [4 Analysis of differential abundance](#4-analysis-of-differential-abundance)
    - [4.1 Estimating log-fold changes across environments](#41-log-fold-changes-across-environments)
    - [4.2 Visualizing broad-level patterns for metabolites](#42-broad-level-patterns-metabolites)
    - [4.3 Comparison of normalized abundances for metabolites](#43-normalized-abundance-analysis-metabolites)
  - [5 Analysis of co-occurrences](#5-analysis-of-cooccurrences)
    - [5.1 Estimation of log conditional probabilities (co-occurrence ranks)](#51-log-conditional-probabilities)
    - [5.2 Correlation with log-fold changes and sample beta-diversity](#52-correlation-with-other-results)


### 0 Metadata

The metadata workflow takes individual study metadata files, general sample information, and prep information, then converts this to mapping files, sample information files, and prep information files.

Note: files with the words "manual" or "prepandas" in the title are curated manually and are not output by a notebook or script.

Processing is done by these IPython notebooks:

* `emp500_s1_merge_sample_info.ipynb` Merge individual study metadata Excel files, add general prep information (including plate and well numbers for the initial DNA extraction), generate sample information file and basic mapping file. 
    - Inputs: `emp500_sample_information_manual.xlsx`, `STUDY_XX_METADATA.xlsx` (sample metadata for each individual study)
    - Outputs: `emp500_sample_information.tsv`, `emp500_full_map.tsv`, `emp500_basic_map.tsv`
* `emp500_s2_add_prep_info_sample_names.ipynb` Add prep information (16S, 18S, ITS) and sample information (sample names, study information, EMPO categories, etc.).
    - Inputs: `emp500_sample_information_manual.xlsx`, `emp500_prep_information_general_prepandas.xlsx`, `emp500_prep_information_*_prepandas.xlsx` (prep info files for each of Round 1 runs)
    - Outputs: `emp500_prep_information_general.xlsx`, `emp500_prep_information_*.xlsx` (prep info files for each of Round 1 runs)
* `emp500_s3_make_mapping_files_prep_info.ipynb` Generate mapping files and prep information files.
    - Inputs: `emp500_sample_information.tsv`, `emp500_prep_information_general.xlsx`, `emp500_prep_information_*.xlsx `
    - Outputs: `emp500_*_prep_info_*.tsv`, `emp500_*_mapping_file_*.tsv`
* `emp500_s4_project_summary.ipynb` Generate project summary and list of samples (for labels).
    - Inputs: `emp500_basic_map.tsv`
    - Outputs: `emp500_project_summary.csv`, `emp500_sample_names.csv`
* `emp500_s5_labels.ipynb` Generate label spreadsheet with QR codes (not encoded).
    - Inputs: `emp500_project_summary.csv`, `emp500_per_study_indexes.xlsx`
    - Outputs: `emp500_labels.xlsx`, `emp500_labels_extra.xlsx`, `emp500_gsheet.xlsx`, `emp500_gsheet_extra.xlsx`, `emp500_box_labels.xlsx`
    
  
### 1 Amplicon sequencing

Demultiplexing, feature-table generation, fragment insertion, and taxonomic profiling were performed in Qiita on a per-sequencing lane basis. Final feature-tables were generated using the meta-analysis functionality in Qiita to combine multiple preps per data type.

### 1.1 16S rRNA gene data

#### Demultiplexing:
* Process: Split libraries FASTQ
* Parameters: Multiplexed FASTQ, Golay 12 base pair reverse complement mapping file barcodes with reverse complement barcodes

#### Sequence trimming, denoising, feature-table generation, and fragment insertion:
* Process: Trimming
* Parameters: 150 base pair
* Process: Deblur + SEPP
* Parameters: Default settings (i.e., Fragment insertion into the GreenGenes 13_8 release phylogeny)

#### Taxonomic profiling
* Process: Feature-classifier sklearn 
* Parameters: Using the GreenGenes 13_8 release as a reference

#### OTU clustering
* Process: Closed-reference OTU picking 
* Parameters: 97% sequence similarity threshold, using the GreenGenes 13_8 release as a reference


### 1.2 18S rRNA gene data

#### Demultiplexing:
* Process: Split libraries FASTQ
* Parameters: Multiplexed FASTQ, Golay 12 base pair reverse complement mapping file barcodes

#### Sequence trimming, denoising, feature-table generation, and fragment insertion:
* Process: Trimming
* Parameters: 150 base pair
* Process: Deblur
* Parameters: Default settings

#### Taxonomic profiling
* Process: Feature-classifier sklearn 
* Parameters: Using the SILVA 138.1 release as a reference

#### OTU clustering
* Process: Closed-reference OTU picking 
* Parameters: 97% sequence similarity threshold, using the SILVA 119 release as a reference


### 1.3 Fungal ITS data

#### Demultiplexing:
* Process: Split libraries FASTQ
** Parameters: Multiplexed FASTQ, Golay 12 base pair reverse complement mapping file barcodes

#### Sequence trimming, denoising, feature-table generation, and fragment insertion:
* Process: Trimming
* Parameters: 150 base pair

* Process: Deblur
* Parameters: Default settings

#### Taxonomic profiling
* Process: Feature-classifier sklearn 
* Parameters: Using the UNITE 8 release as a reference

#### OTU clustering
* Process: Closed-reference OTU picking 
* Parameters: 97% sequence similarity threshold, using the UNITE 8 release as a reference


### 2 Shotgun sequencing

Demultiplexing and adapter trimming were performed prior to processing in Qiita. Read alignment to the Web of Life Toolkit Analysis (Woltka) was performed in Qiita on a per-sequencing lane basis. Each read alignment was processed in Woltka to produce a genome-OTU (gOTU) feature-table, allowing for use of the Woltka phylogeny and taxonomy for downstream analyses. The final Woltka gOTU feature-table was generated by merging across preps using QIIME2. In parallel, metagenomic assemblies and metagenome assembled genomes (MAGs) were constructed for each of 35 major environments represented among the samples.

#### 2.1 Short-read analysis

#### 2.1.1 Sequence file demultiplexing

Shotgun sequence files from Illumina were demultiplexed using bcl2fastq and custom sample sheets, with demultiplexed files placed in directories designated for each PI–study combination.

#### 2.1.2 Adapter trimming and poly-G removal

Adapter trimming and poly-G removal were performed on per-sample FASTQ files using Atropos 1.1.25:

`atropos \
   -a GATCGGAAGAGCACACGTCTGAACTCCAGTCAC \
   -A AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT \
   -pe1 forward.fastq.gz \
   -pe2 reverse.fastq.gz \
   -o forward_trimmed.fastq.gz \
   -p reverse_trimmed.fastq.gz \
   --nextseq-trim 30 \
   --match-read-wildcards \
   -e 0.1 \
   -q 15 \
   --insert-match-error-rate 0.2 \
   --minimum-length 100 \
   --pair-filter any \
   --report-file report.txt \
   --report-formats txt \
   -T 16`

#### 2.1.3 Qiita read alignment to the Woltka reference database

* Process: Shogun v1.0.7
* Parameters: bowtie2 as aligner tool, Web of Life (WoL) as reference database

Bowtie2 2.3.2 parameters:

`bowtie2 \
  -1 forward_trimmed.fastq.gz \
  -2 reverse_trimmed.fastq.gz
  -p {PPN} \
  -x {database_WoL} \
  -q \
  -S trimmed_aligned.sam --seed 42 \
  --very-sensitive \
  -k 16 \
  --np 1 \
  --mp "1,1" \
  --rdg "0,1" \
  --rfg "0,1" \
  --score-min \
  "L,0,-0.05" \
  --no-head \
  --no-unal`

#### 2.1.4 Woltka gOTU feature-table generation

`woltka classify \
  --input trimmed_aligned.sam.xz \
  --demux \
  --output woltka_gotu_table.biom`
  
`qiime tools import \
  --type FeatureTable[Frequency] \
  --input-path woltka_gotu_table.biom \
  --output-path woltka_gotu_table.qza`
  
`qiime feature-table merge \
  --i-tables woltka_gotu_table.qza \
  --i-tables woltka_gotu_table_2.qza \
  --p-overlap-method 'sum' \
  --o-merged-table woltka_gotu_table_merged.qza`

#### 2.2 Metagenomic assembly and binning

#### 2.2.1 Assembly and co-assembly of EMP500 samples within each environment

* To determine which of the EMP500 environments could be co-assembled, MASH, atool employing the MinHash dimensionality reduction technique [(Ondov, Treangen et al. 2016)](https://doi.org/10.1186/s13059-016-0997-x) was used to evaluate the pairwise distances between the metagenomic data sets. 
* Sequence‭-based grouping ‬was done by ‭Markov Clustering (MCL) [(Van Dongen and Abreu-Goodger 2012)](https://doi.org/10.1007/978-1-61779-361-5_15) of Mash. 
* A combination of MASH distances and a Markov cluster algorithm which identifies orthology groups (OGs) in reciprocal best matches (RBM), was employed to evaluate the samples that could be grouped for co-assembly. 
* Mash sketches were initially created using a sketch size of 10,000 and k-mer size of 32 and the sketches were combined using the “paste” option. 
* A pairwise distance matrix was constructed using the “dist” option and the distance matrix was used in downstream analyses. 
* Samples which had distance values below 0.1 were then co-assembled [(Karthikeyan, Rodriguez-R et al. 2020)](https://doi.org/10.1111/1462-2920.14966). ‬‬
* Co-assembly was carried out using metaSPades v3.15.0 with the “--only-assembler” mode and the following k-mers: 21,33,55,77,99,127. Quality of the assemblies were evaluated using MetaQUAST [(Mikheenko, Saveliev et al. 2016)](https://doi.org/10.1093/bioinformatics/btv697).  

#### 2.2.2 Binning of assemblies to generate MAGs for each environment

* Binning was carried out using MaxBin v2.2.7 [(Wu, Simmons et al. 2016)](https://doi.org/10.1093/bioinformatics/btv638) and MetaBAT v2.12.1 [(Kang, Froula et al. 2015)](https://doi.org/10.7717/peerj.1165). 
* For each co-assembly both the tools were employed for binning and the resulting bins were hen de-replicated at 95% gANI (genome-aggregate average nucleotide identity) to remove redundancy using FastANI v1.1 [(Jain, Rodriguez-R et al. 2018)](https://doi.org/10.1038/s41467-018-07641-9). 
* Only scaffolds larger than 1000bp were used for MAG generation. Completeness and contamination were estimated using CheckM (Parks, Imelfort et al. 2015). MAG (Metagenome-assembled genome) quality was determined as [Completeness – 5 * (Contamination)]. 
* All MAGs with quality score > 50 were used in downstream analyses. High‐quality MAGs were defined as Completeness > 75% and Contamination < 5%, and medium‐quality MAGs were defined by Completeness > 50% and Contamination < 10%. 
* MAG refining was carried out using RefineM v0.0.23 [(Parks, Rinke et al. 2017)](https://doi.org/10.1038/s41564-017-0012-7). Divergent taxonomic assignments from the MAG scaffolds were identified using the “call_genes” option and then searching them against the reference database available at https://data.ace.uq.edu.au/public/misc_downloads/refinem/ using the “taxon_profile” option. Potentially contaminating scaffolds were then removed from the bins using the “filter_bins” option. 

#### 2.2.3 Functional annotation of assemblies

* protein-coding gene predictions were performed using Prodigal v2.6.3
* annotation of gene predictions was performed using Diamond v2.0.5
* carbohydrate-active-enzyme (CAZy) prediction was performed using dbCAN2 v2.0.11
* secondary metabolite gene cluster prediction was performed using antiSMASH v5

#### 2.2.4 Taxonomic profiling of MAGs

* Taxonomic classification of MAGs was performed using GTDB-Tk v1.3.0 release95 [(Chaumeil, Mussig et al. 2020)](https://academic.oup.com/bioinformatics/article/36/6/1925/5626182) using the “gtdbtk classify_wf” option.


# 3 Metabolomics data analysis


## 3.1 Non targeted mass spectrometry analysis by LC-MS

For detailed information on the sample preparation and LC-MS/MS-based non-targeted mass spectrometry acquisition see the following page: [https://github.com/biocore/emp/blob/master/protocols/MetabolomicsLC.md](https://github.com/lfnothias/emp/blob/master/protocols/MetabolomicsLC.md).

**IMPORTANT**: The processing and annotations below were performed to study the entire EMP dataset. These results could be used to investigate a specific study that is part of the EMP, but this is not recommended. Instead, this processing would have to be performed and optimized for each study. Contact Louis-Felix Nothias [(lnothiasscaglia@health.ucsd.edu)](lnothiasscaglia@health.ucsd.edu) for more informations. 

The data were processed and annotated by Louis-Felix Nothias [(lnothiasscaglia@health.ucsd.edu)](lnothiasscaglia@health.ucsd.edu) from the [Dorrestein Lab at University of California San Diego](https://dorresteinlab.ucsd.edu/).

## 3.1.1 Data conversion and desposition
The mass spectrometry data were centroided and converted from the proprietary format (.raw) to the m/z extensible markup language format (.mzML) using [ProteoWizard](http://proteowizard.sourceforge.net/download.html) (ver. 3.0.19, MSConvert tool). Citation: [(Chambers et al. _Nature Biotech._, 2012)](https://www.nature.com/articles/nbt.2377).
 
The data were visualized and inspected with the [OpenMS TOPPAS tool](https://github.com/OpenMS/OpenMS) (ver 2.4.0). Citation: [Rost et al. Nat. Methods, 2016](https://www.nature.com/articles/nmeth.3959)

The mass spectrometry method and data (.RAW and .mzML) were deposited on the MassIVE public repository and are available under the dataset accession number MSV000083475 at this page: [`https://massive.ucsd.edu/ProteoSAFe/dataset.jsp?task=3de2b5de5c274ca6b689977d08d84195`](https://massive.ucsd.edu/ProteoSAFe/dataset.jsp?task=3de2b5de5c274ca6b689977d08d84195).

- The .RAW files are accessible via FTP here: [`ftp://massive.ucsd.edu/MSV000083475/peak/mzML/`](ftp://massive.ucsd.edu/MSV000083475/peak/mzML/).

- The .mzML files are accessible via FTP here: [`ftp://massive.ucsd.edu/MSV000083475/raw/RAW/`](ftp://massive.ucsd.edu/MSV000083475/raw/RAW/).


## 3.1.2 Data Analysis and Annotation

Two different LC-MS data processing/annotation workflows were used:

- **Feature-Based Molecular Networking** (FBMN): quantitative and accurate.
	- The **feature quantification table** of FBMN is available from the MassIVE deposition and the filtered feature quantification table at [`emp/data/metabolomics/FBMN/`](../data/metabolomics/).

- **Classical Molecular Networking** (CMN): qualitative and sensitive.
	- The **MS/MS feature table** of CMN is available directly from the GNPS job and the filtered MS/MS feature tables from [`emp/data/metabolomics/CMN/`](../data/metabolomics/).

- **Metabolite feature metadata table** for CMN and FBMN**
- The **Metabolite feature metadata tables**are available at [`emp/data/metabolomics/`](../data/metabolomics/). Each metabolite feature metadata table summarizes the results of all the LC-MS/MS annotation tools used and can be mapped to the feature quantification tables of CMN and FBMN, respectively. The sub-folders contain the results of each annotation tool.

A discussion on how to use these results files and how they were generated is available at [`emp/data/metabolomics/`](../data/metabolomics).

The script that were used to process/generate the feature quantification table and feature metadata table are available at 
[https://github.com/lfnothias/emp_metabolomics](https://github.com/lfnothias/emp_metabolomics).

Below are provided informations on each annotation tools used, and the links to the jobs/results.

### 3.1.2.1 Feature Based Molecular Networking workflow

#### [FBMN] Feature detection and alignement with MZmine
The mzML files were then processed with a custom build of MZmine toolbox (*vers.2.37corr17.7kaimerge2* at [https://github.com/robinschmid/mzmine2/releases](https://github.com/robinschmid/mzmine2/releases)) that includes advanced modules for adduct/isotopologue annotations. Citations: [Pluskal et al., _BMC Bioinf._ 2010](https://bmcbioinformatics.biomedcentral.com/articles/10.1186/1471-2105-11-395) and [Schmid, Petras, Nothias et al. bioRxiv, 2020, 2020.05.11.088948](https://www.biorxiv.org/content/10.1101/2020.05.11.088948v1).

The MZmine processing was performed on Ubuntu 18.04 LTS 64-bits workstation (Intel Xeon 5E-2637, 3.5 GHz, 8 cores, 64 Go of RAM) and took ~3 days. 

The MZmine project, the MZmine batch file (.XML format), and results files (.MGF and .CSV) are available in the MassIVE dataset [`MSV000083475`](https://massive.ucsd.edu/ProteoSAFe/dataset.jsp?task=3de2b5de5c274ca6b689977d08d84195). The MZmine batch file contains all the parameters used during the processing. In brief, feature detection and deconvolution was performed with the ADAP chromatogram builder, and local minimum search algorithm. The isotopologues were regrouped, and the features (peaks) were aligned across samples. The peaklist was gap filled and only peaks with an associated fragmentation spectrum (MS2) and occuring in a minimum of 3 files were conserved. Peak shape correlation analysis was used to group peaks originating from the same molecule, and used for adduct/isotopologue annotations. Finally the feature table results (.CSV) and spectral information (.MGF) were exported for subsquent analysis on GNPS and with the GNPS and SIRIUS export modules.

##### [FBMN] MZmine processing files:

These files were deposited on MassIVE (MSV000083475) and available at: [`ftp://massive.ucsd.edu/MSV000083475/updates/2019-08-21_lfnothias_7cc0af40/other/1908_EMPv2_INN/`](ftp://massive.ucsd.edu/MSV000083475/updates/2019-08-21_lfnothias_7cc0af40/other/1908_EMPv2_INN/)
    
- `1907_Benchmarking_dataset_EMP_batch_v9_MinimumLocal_QE_v6_INN_v4.xml` : this is the MZmine batch file that was used for the procesing. It does not contains the Export step (GNPS and SIRIUS export that were employed with the default parameters).

- `1907_EMPv2_v3.mzmine`: the MZmine project that contains the results. It can be open with a powerful desktop computer (see the spec) to visualize aligned chromatograms etc.
	
##### [FBMN] MZmine result files: 

- `1907_EMPv2_INN_GNPS_quant.csv`: the feature table generated by MZmine that contains the ion intensity (LC-MS peak area) across the EMP samples. This feature table is the unprocessed table (no normalization or other post processing was applied to it). The ion intensity is the standard proxy to estimate the relative concentration of a metabolite across the samples. However the intensities of different metabolites (ions) cannot be compared due to different ionisation efficiency.
  
- `1907_EMPv2_INN_GNPS.mgf`: the MS2 spectral summary file generated by MZmine that contains the most intense MS2 spectra associated with an ions detected. It is used for GNPS analysis (molecular networking, spectral annotation, etc).
   
- `1907_EMPv2_INN_GNPS_edges_msannotation.csv`: the edges annotations from ion identity networking in MZmine that contains informations on related group of ions (peak shape correlation analysis).
   
- `1907_EMPv2_SIRIUS.mgf`: the MS2 spectral summary file generated by MZmine that contains the MS1 (isotopic pattern, adducts) MS2 spectra used for SIRIUS annotation (molecular formula prediction, and structure/class annotation).

#### [FBMN] Feature-Based Molecular Networking on GNPS

The results files of MZmine (.MGF and .CSV files) were uploaded to GNPS [(http://gnps.ucsd.edu)](http://gnps.ucsd.edu) and analyzed with the Feature-Based Molecular Networking (FBMN) workflow [(Nothias, Petras, Schmid et al Nat., Methods 2020)](https://www.nature.com/articles/s41592-020-0933-6). The metadata were also inputed in the job. Citation: [(Wang et al., Nat. Biotech. 2016)](https://www.nature.com/articles/nbt.3597).

Spectral library matching was performed against public MS/MS spectral library and the NIST17 library to obtain putative level 2 annotation (putative structure) based on [MSI standards](https://pubs.acs.org/doi/abs/10.1021/es5002105).

- The GNPS molecular networking job, paramaters and results can be consulted at the following address: [`https://gnps.ucsd.edu/ProteoSAFe/status.jsp?task=929ce9411f684cf8abd009670b293a33`](https://gnps.ucsd.edu/ProteoSAFe/status.jsp?task=929ce9411f684cf8abd009670b293a33).

- The GNPS molecular networking job was also performed in analogue mode to obtain level 3 MSI annotations (partial/class annotation): [`https://gnps.ucsd.edu/ProteoSAFe/status.jsp?task=fafdbfc058184c2b8c87968a7c56d7aa`](https://gnps.ucsd.edu/ProteoSAFe/status.jsp?task=fafdbfc058184c2b8c87968a7c56d7aa).

#### [FBMN] Putative annotation of small peptides with the DEREPLICATOR tools

For the putative annotation of small peptides. These annotations can be classified as level 2/3 annotation (putative/partial structure) based on [MSI standards](https://pubs.acs.org/doi/abs/10.1021/es5002105)). The DEREPLICATOR algorithm was used on GNPS. While DEREPLICATOR+ annotates known structures, the DEREPLICATOR VarQuest can search analogues of known peptidic molecules and that are differing by one amino acid residue. Citations: 
[Mohimani et al, Nat. Chem. Bio. 2016](https://www.nature.com/articles/nchembio.2219) and 
[Mohimani et al, Nat. Com. 2018]
(https://www.nature.com/articles/s41467-018-06082-8?_ga=2.258351242.188697708.1538611200-1366481109.1538611200).

- The DEREPLICATOR+ job can be accessed here: [`https://gnps.ucsd.edu/ProteoSAFe/status.jsp?task=ee40831bcc314bda928886964d853a52`](https://gnps.ucsd.edu/ProteoSAFe/status.jsp?task=ee40831bcc314bda928886964d853a52).

- The DEREPLICATOR VarQuest job can be accessed here: [`https://gnps.ucsd.edu/ProteoSAFe/status.jsp?task=1fafd4d4fe7e47dd9dd0b3d8bb0e6606`](https://gnps.ucsd.edu/ProteoSAFe/status.jsp?task=1fafd4d4fe7e47dd9dd0b3d8bb0e6606).

#### [FBMN] Putative annotation of small cyclopeptides with the CycloNovo

CycloNovo performs de novo cyclopeptide sequencing using employs de Bruijn graphs [Bahar et al, Cell System, 2020](https://www.sciencedirect.com/science/article/pii/S240547121930393X). Many of these cyclopeptides are bioactive molecules produced by microbes.

- The CycloNovo job results can be accessed here: [`https://gnps.ucsd.edu/ProteoSAFe/status.jsp?task=85d371f5c8e04687838ecbc28ac2dbb6`](https://gnps.ucsd.edu/ProteoSAFe/status.jsp?task=85d371f5c8e04687838ecbc28ac2dbb6)

#### [FBMN] Putative annotation of small molecules with SIRIUS

Additional spectral annotation of tandem mass spectrometry data were obtained with the SIRIUS [(Durkhop et al., Nat. Methods, 2019)](https://www.nature.com/articles/s41592-019-0344-8) computational annotation tool (vers. 4.4.25, headless, linux) running on a cluster computer (32 cores, 256 Gb of RAM).

- Molecular formulas were computed with the SIRIUS module by matching the experimental and predicted isotopic patterns [(Böcker, Bioinformatics 25, 218–224, 2009](https://academic.oup.com/bioinformatics/article/25/2/218/218950), and from fragmentation trees analysis of the fragment ions [(Böcker and Dührkop, J. Cheminform. 8, 5, 2016)](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-016-0116-8).
- Molecular formula prediction was refined with the ZODIAC module by using Gibbs sampling [(Ludwig et al, Nat. Mach. Intel., 2020)](https://www.nature.com/articles/s42256-020-00234-6) for fragmentation spectra that were not chimeric spectra or had a poor fragmentation.
- Structure annotation with structure database was done with the CSI:FingerID  module [(Durkhop et al., PNAS 2015)](https://www.pnas.org/content/112/41/12580).
- Systematic class annotations were obtained with CANOPUS [(Dührkop, et al. Nat. Biotech. 2020)](https://www.nature.com/articles/s41587-020-0740-8).  

Parameters were set as follows, for SIRIUS: molecular formula candidates retained (80), molecular formula database (ALL), maximum precursor ion m/z computed (750), profile (orbitrap), m/z maximum deviation (10 ppm), ions annotated with MZmine were prioritized and other ions were considered ([M+H3N+H]+, [M+H]+, [M+K]+,[M+Na]+, [M+H-H2O]+, [M+H-H4O2]+, [M+NH4]+); for ZODIAC: the features were splitted into 10 random subsets and were computed separately with the following parameters: threshold filter (0.9), minimum local connections (0); for CSI:FingerID: m/z maximum deviation (10 ppm) and biological database (BIO). The computation was performed on a linux cluster computer (32 cpu with 256 GB of RAM).

The SIRIUS results are available at [`emp/data/metabolomics/FBMN/SIRIUS`](../data/metabolomics/FBMN/SIRIUS).

### 3.1.2.2 Classical Molecular Networking workflow

#### [CMN] Classical molecular networking on GNPS

The mzML files were uploaded to GNPS [(http://gnps.ucsd.edu)](http://gnps.ucsd.edu) and analyzed with the Classical Molecular Networking (CMN) workflow. Citation: [(Wang et al., Nat. Biotech. 2016)](https://www.nature.com/articles/nbt.3597).

Spectral library matching was performed against public MS/MS spectral library and the NIST17 library to obtain putative level 2 annotation (putative structure) based on [MSI standards](https://pubs.acs.org/doi/abs/10.1021/es5002105).

- The GNPS molecular networking job, paramaters and results can be consulted at the following address: [`https://gnps.ucsd.edu/ProteoSAFe/status.jsp?task=b6e15e30aea24ded9a413379dee0b4eb`](https://gnps.ucsd.edu/ProteoSAFe/status.jsp?task=b6e15e30aea24ded9a413379dee0b4eb).

- The GNPS molecular networking job was also performed in analogue mode to obtain level 3 MSI annotations (partial/class annotation): [`https://gnps.ucsd.edu/ProteoSAFe/status.jsp?task=9a6208b0c20f4a45a8a1b30df14cbeb6`](https://gnps.ucsd.edu/ProteoSAFe/status.jsp?task=9a6208b0c20f4a45a8a1b30df14cbeb6).

#### [CMN] Putative annotation of small peptides with the DEREPLICATOR tools

For the putative annotation of small peptides. These annotations can be classified as level 2/3 annotation (putative/partial structure) based on [MSI standards](https://pubs.acs.org/doi/abs/10.1021/es5002105)). The DEREPLICATOR algorithm was used on GNPS. While DEREPLICATOR+ annotates known structures, the DEREPLICATOR VarQuest can search analogues of known peptidic molecules and that are differing by one amino acid residue. Citations: 
[Mohimani et al, Nat. Chem. Bio. 2016](https://www.nature.com/articles/nchembio.2219) and 
[Mohimani et al, Nat. Com. 2018]
(https://www.nature.com/articles/s41467-018-06082-8?_ga=2.258351242.188697708.1538611200-1366481109.1538611200).

- The DEREPLICATOR+ job can be accessed here: [`https://gnps.ucsd.edu/ProteoSAFe/status.jsp?task=532ea29acf194f859b3e67d3d0ca9980`](https://gnps.ucsd.edu/ProteoSAFe/status.jsp?task=532ea29acf194f859b3e67d3d0ca9980) 

- The DEREPLICATOR VarQuest job can be accessed here: [`https://gnps.ucsd.edu/ProteoSAFe/status.jsp?task=1457a3f93e6b423b965adc313e7198ec`](https://gnps.ucsd.edu/ProteoSAFe/status.jsp?task=1457a3f93e6b423b965adc313e7198ec). 

#### [CMN] Putative annotation of small cyclopeptides with the CycloNovo

CycloNovo performs de novo cyclopeptide sequencing using employs de Bruijn graphs [Bahar et al, Cell System, 2020](https://www.sciencedirect.com/science/article/pii/S240547121930393X). Many of these cyclopeptides are bioactive molecules produced by microbes.

- The CycloNovo job results can be accessed here: [`https://gnps.ucsd.edu/ProteoSAFe/status.jsp?task=fbbaa7f1e3a94937a1647e25095fb76c`](https://gnps.ucsd.edu/ProteoSAFe/status.jsp?task=fbbaa7f1e3a94937a1647e25095fb76c)

#### [CMN] Putative annotation of small molecules with SIRIUS
SIRIUS results for CMN are less accurate than with FBMN because the annotation is not informed by the MS1 isotopic pattern and ion annotation (i.e. adduct type). Therefor, caution is required when using these annotations. 


# 3.2 Non-targeted mass spectrometry analysis by GC-MS

Untargeted analyses of polar metabolites was performed by GC-MS (electronic ionisation source) The data were collected by Sneha Couvillion (sneha.couvillion@pnnl.gov) from the [Thomas Metz laboratory, Pacific Northwest National Laboratory](https://omics.pnl.gov/staff-page/Metz/Tom).

## 3.2.1 Data conversion and deposition
The GC-MS data were converted from the proprietary file format (.d format) to the netCDF file format (.cdf format) using [OpenChrom](https://sourceforge.net/projects/openchrom/) (ver. win32.x86_64_1.0.0_rel). Citation: [(Wenig et al. _OpenChrom._, 2010)](https://bmcbioinformatics.biomedcentral.com/articles/10.1186/1471-2105-11-405). For a detail description of the conversion, please refer to this [document pages 1-4](document/Metabolite Detector_GC-MS_PNNL_tutorial.pdf)

- The files were deposited on MassIVE under the following accession number [`MSV000083743`](https://massive.ucsd.edu/ProteoSAFe/dataset.jsp?task=948bad7011a544eab485d2114cac22f0). Every batch of samples that are run on the GC-MS have accompanying blanks and a FAMES file. 

## 3.2.2 Data Analysis and Annotation

### 3.2.2.1 PNNL GC-MS pipeline

The data were processed and annotated by Sneha Couvillion (sneha.couvillion@pnnl.gov) from the [Thomas Metz laboratory, Pacific Northwest National Laboratory](https://omics.pnl.gov/staff-page/Metz/Tom).

#### [GC-PNNL] Data Processing
The GC-MS data files (.netCDF format) were processed using MetaboliteDetector ([Hiller et al., Anal. Chem. 2009](https://pubs.acs.org/doi/10.1021/ac802689c)) in order to detect, align and measure the metabolites intensities accross samples. For a detail description of the processing, see this [document pages 4-8](document/Metabolite Detector_GC-MS_PNNL_tutorial.pdf)


#### [GC-PNNL] Annotation
Retention indices (RI) of detected metabolites were calculated based on the analysis of the FAME standard mixture, followed by their chromatographic alignment across all analyses after deconvolution. Metabolites were then identified by matching GC-MS features (characterized by measured retention indices and mass spectra) to an augmented version of the Agilent Fiehn Metabolomics Retention Time Locked (RTL) Library ([Kind et al., Anal. Chem. 2009](https://pubs.acs.org/doi/10.1021/ac9019522)), which contains spectra and validated retention indices for over 700 metabolites. All metabolite identifications were manually validated to reduce deconvolution errors during automated data-processing and to eliminate false identifications. The NIST 08 GC-MS library was also used to cross-validate the spectral matching scores obtained using the Agilent library.

##### [GC-PNNL] Result files

- `EMP_GCMSmetabolitedata_blocksABCD_080919.xlsx`: This excel file (.xlsx) contains the metabolites intensities and identification that were manually validated. The file can be accessed on the MassIVE at [ftp://massive.ucsd.edu/MSV000083743/updates/2019-08-22_lfnothias_7cc043bc/other/](ftp://massive.ucsd.edu/MSV000083743/updates/2019-08-22_lfnothias_7cc043bc/other/)

QC files for each samples accessible at [`ftp://massive.ucsd.edu/MSV000083743/other/`](ftp://massive.ucsd.edu/MSV000083743/other/):

- The `_GC_DatasetInfo.xml`: contains informations on the sample acquisition.
- The `_GC_BPI_MS.png`: contains an image of the sample's base peak chromatogram.
- The `_GC_GC_TIC.png`: contains an image of the sample's total ion chromatogram.
- The `_GC_LCMS.png`: contains an image of the sample's 2D chromatogram.
- The `_GC_HighAbu_LCMS.png`: contains an image of the sample's 2D chromatogram.

### 3.2.3 GNPS GC-MS pipeline

To be completed 

#### [GC-GNPS] Data Processing
To be completed 

#### [GC-GNPS] Annotation
To be completed 

#### [GC-GNPS] Result files
To be completed


# 4 Analysis of differential abundance


## 4.1 Estimation of log-fold changes across environments

* Log-fold changes for each feature across environments were quantified using Songbird [(Morton et al. 2019)](https://www.nature.com/articles/s41467-019-10656-5).
* Each sample was assigned to training or testing groups manually, using an 80/20 split at each level of EMPO 4.
* 'Animal distal gut (non-saline)' was used as the reference group.
* The fitted model was compared against a null model (i.e., '1')
* Log-fold changes for each environment were merged with feature metadata for subsequent analyses

Run fitted model:
`qiime songbird multinomial \
--i-table input_biom.qza \
--m-metadata-file emp500_metadata_basic.txt \
--p-formula "C(empo_4, (Treatment('Animal distal gut (non-saline)')))" \
--p-epochs 1000000 \
--p-differential-prior 0.5 \
--p-learning-rate 1e-5 \
--p-summary-interval 2 \
--p-batch-size 400 \
--p-min-sample-count 0 \
--p-training-column songbird_trainTest_8020_empo_4 \
--o-differentials differentials.qza \
--o-regression-stats regression-stats.qza \
--o-regression-biplot regression-biplot.qza`

Run null model:
`qiime songbird multinomial \
--i-table input_biom.qza \
--m-metadata-file emp500_metadata_basic.txt \
--p-formula "1" \
--p-epochs 1000000 \
--p-differential-prior 0.5 \
--p-learning-rate 1e-5 \
--p-summary-interval 2 \
--p-batch-size 400 \
--p-min-sample-count 0 \
--p-training-column songbird_trainTest_8020_empo_4 \
--o-differentials differentials_null.qza \
--o-regression-stats regression-stats_null.qza \
--o-regression-biplot regression-biplot_null.qza`

Compare models
`qiime songbird summarize-paired \
--i-regression-stats regression-stats.qza \
--i-baseline-stats regression-stats_null.qza \
--o-visualization paired-summary.qzv`


## 4.2 Visualization of broad-level patterns across environments for metabolites

* Metabolite intensities were summed across all samples within each environment at EMPO 4 (QIIME2)
* A presence/absence table was generated for comparison (QIIME2)
* Taxa bar plots were generated, and relative abundance data exported at the pathway and superclass levels, for subsequent analysis (QIIME2)
* Presence/absence and intensity of metabolites were visualized (R)

`qiime feature-table group \
  --i-table input_biom.qza \
  --p-axis 'sample' \
  --m-metadata-file emp500_metadata_basic.txt \
  --m-metadata-column 'empo_4' \
  --p-mode 'sum' \
  --o-grouped-table input_biom_sum_empo4.qza
  
  qiime feature-table presence-absence \
  --i-table input_biom.qza \
  --o-presence-absence-table input_biom_binary.qza
  
  unzip input_biom_binary.qza
  
  qiime tools import \
  --input-path input_biom_binary.biom \
  --type 'FeatureTable[Frequency]' \
  --input-format BIOMV210Format \
  --output-path input_biom_binaryFreq.qza
  
  qiime feature-table group \
  --i-table input_biom_binaryFreq.qza \
  --p-axis 'sample' \
  --m-metadata-file emp500_metadata_basic.txt \
  --m-metadata-column 'empo_4' \
  --p-mode 'sum' \
  --o-grouped-table input_biom_binaryFreq_sum_empo4.qza

qiime taxa barplot \
  --i-table input_biom_sum_empo4.qza \
  --i-taxonomy emp500_lcms_fbmn_feature_metadata_microbial_npc_taxonomy.qza \
  --m-metadata-file emp500_metadata_grouped_empo4.txt \
  --o-visualization input_biom_sum_empo4_taxa_barplot.qzv

qiime taxa barplot \
  --i-table input_biom_binaryFreq_sum_empo4.qza \
  --i-taxonomy emp500_lcms_fbmn_feature_metadata_microbial_npc_taxonomy.qza \
  --m-metadata-file emp500_metadata_grouped_empo4.txt \
  --o-visualization input_biom_binaryFreq_sum_empo4_taxa_barplot.qzv`


## 4.3 Comparison of normalized abundances for metabolites

* To account for the compositionality of the metabolite and microbial taxon data, we used log-ratios to compare groups of features across environments
* Log-ratios were quantified for feature groups of interest using Qurro [(Fedarko et al. 2020)](https://academic.oup.com/nargab/article/2/2/lqaa023/5826153?login=true).
* Plot data were exported from Qurro and merged with feature metadata (Python).
* Differences in log-ratios of feature groups across environments were visualized and tested statistically (R)

`qurro \
  --ranks differentials.tsv \
  --table input_biom.biom \
  --sample-metadata emp500_metadata_basic.txt \
  --feature-metadata emp500_lcms_fbmn_feature_metadata_microbial_npc_taxonomy.tsv \
  --output-dir qurro_metabolites/`


# 5 Analysis of co-occurrence


## 5.1 Estimation of log conditional probabilities (co-occurrence ranks)

* Co-occurrences between feature sets were estimated using mmvec [(Morton et al. 2019)](https://www.nature.com/articles/s41592-019-0616-3).
* The fitted model was compared against a null model (i.e., '1')
* Feature loadings from the co-occurrence ordination, as well as log conditional probabilities for each feature, were exported for subsequent analysis

`qiime mmvec paired-omics \
  --i-microbes input_biom_microbial_taxa.qza \
  --i-metabolites input_biom_metabolites.qza \
  --m-metadata-file emp500_metadata_basic.txt \
  --p-training-column 'songbird_trainTest_8020_empo_3' \
  --p-min-feature-count 10 \
  --p-epochs 100 \
  --p-batch-size 50 \
  --p-latent-dim 3 \
  --p-input-prior 1 \
  --p-output-prior 1 \
  --p-learning-rate 1e-05 \
  --p-summary-interval 60 \
  --o-conditionals mmvec_conditionals.qza \
  --o-conditional-biplot mmvec_biplot.qza

qiime mmvec paired-omics \
  --i-microbes input_biom_microbial_taxa.qza \
  --i-metabolites input_biom_metabolites.qza \
  --p-latent-dim 0 \
  --p-summary-interval 1 \
  --output-dir null_summary

qiime mmvec summarize-paired \
  --i-model-stats model_stats.qza \
  --i-baseline-stats model_stats_null.qza \
  --o-visualization paired-summary.qzv
	
qiime emperor biplot \
  --i-biplot mmvec_biplot.qza \
  --m-sample-metadata-file emp500_lcms_fbmn_feature_metadata_microbial.txt \
  --m-feature-metadata-file wol_taxonomy_with_differentials.txt \
  --o-visualization mmvec_biplot.qzv`


## 5.2 Correlation with log-fold changes and sample beta-diversity

* Feature loadings from the first 10 axes of the co-occurrence biplot were correlated with log-fold changes in metabolite abundances for each environment (Python)
* Feature loadings from the first 10 axes of the co-occurrence biplot were correlated with feature loadings from the first three axes, and the global magnitude, from the ordination representing sample beta-diversity based on metabolites (Python)
* To relate co-occurrences with differential abundance across environments, for focal environments with strong relationships from the first set of correlations above, two groups of features were manually selected for additional analysis of differential abundance (R)
* The log-ratio of the abundance of feature group 1 : group 2 were compared between the focal environment vs. all other environments (R)
