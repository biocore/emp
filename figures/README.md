## figures

Code to generate the figures in "A communal catalogue reveals Earth’s multiscale microbial diversity", Thompson et al., *Nature* (2017). This manuscript describes the meta-analysis of EMP 16S Release 1, the first 97 studies subjected to 16S rRNA amplicon sequencing through the [Earth Microbiome Project](http://www.earthmicrobiome.org).

Input data files for generating the figures below are found in several places:

* All data files (except sequences) required to generate the figures below are available from ftp://ftp.microbio.me/emp/release1; full contents are listed in `data/ftp_contents.txt`. 
* All data files (except sequences) for this manuscript are archived with Zenodo, available from DOI [XXX](http://doi.org/XXX).
* Sequences files are available directly from EBI (see below).
* The mapping file (metadata) for analyses unless otherwise noted is `emp_qiime_mapping_qc_filtered.tsv` in `data/mapping_files`.
* Select smaller data files (<100 GB) are also stored in `data`.

### 1 Amplicon sequence processing

This section describes the commands to download the raw sequence data from EBI and perform OTU picking using different methods, including generating phylogenetic trees and taxonomies for reference sequences, if necessary.

#### 1.1 Download demultiplexed fasta sequence files

Per-study sequence files can be downloaded directly from EBI using the scripts `download_ebi_fasta.sh` (FASTA) and `download_ebi_fastq.sh` (FASTQ) in `code/download-sequences`. Fasta sequences are used by the steps below. The sequences from EBI were demultiplexed and minimally quality filtered using the QIIME 1 command [split_libraries_fastq.py](http://qiime.org/scripts/split_libraries_fastq.html) with Phred quality threshold of 3 and default parameters.

#### 1.2 Generation of OTU/sequence observation tables

Four separate OTU picking procedures were run on the EMP Release 1 data: de novo using Deblur, closed-reference using Greengenes 13.8, closed-reference using Silva 123, and open-reference using Greengenes 13.8.

##### 1.2.1 Deblur (de novo sequence variant determination)

Deblur sOTU (tag sequence or amplicon sequence variant) picking was done using a pre-release version of [Deblur](https://github.com/biocore/deblur). That workflow can be called from the script `run_deblur_emp_original.sh` in `code/03-otu-picking-trees/deblur`. The analogous workflow using the published distribution of Deblur can be called from the script `run_deblur_emp_new.sh`.

##### 1.2.2 Closed-reference Greengenes 13.8

Closed-reference OTU picking against Greengenes 13.8 was done using the QIIME 1 script [pick_closed_reference_otus.py](http://qiime.org/scripts/pick_closed_reference_otus.html). The workflow can be called from the notebook `closed_reference_otu_picking.ipynb` in `code/03-otu-picking-trees/closed-ref`.

##### 1.2.3 Closed-reference Silva 123

Closed-reference OTU picking against Silva 123 16S was done using the QIIME 1 script [pick_closed_reference_otus.py](http://qiime.org/scripts/pick_closed_reference_otus.html). The workflow can be called from the notebook `closed_reference_otu_picking.ipynb` in `code/03-otu-picking-trees/closed-ref`.

##### 1.2.4 Open-reference Greengenes 13.8

Closed-reference OTU picking against Greengenes 13.8 was done using the QIIME 1 script [pick_open_reference_otus.py](http://qiime.org/scripts/pick_open_reference_otus.html). The workflow can be called from the notebook `open_reference_otu_picking.ipynb` in `code/03-otu-picking-trees/open-ref`.

#### 1.3 Phylogenetic trees

##### 1.3.1 Deblur

Deblur sequences were inserted into the Greengenes reference tree using [SEPP](https://github.com/smirarab/sepp). The code for this method is in `code/03-otu-picking-trees/run_sepp.sh`.

##### 1.3.2 Closed-reference Greengenes 13.8

##### 1.3.3 Closed-reference Silva 123

##### 1.3.4 Open-reference Greengenes 13.8

Reference sequences from the open-reference OTU picking were aligned using [PyNAST](https://biocore.github.io/pynast/) and the tree built using [FastTree](https://www.msi.umn.edu/sw/fasttree).

#### 1.4 Rarefaction of tables

Deblur and OTU tables were rarefied (subsampled) to generate equal numbers of observations (sequences) per sample, used in many of the analyses as described below. Deblur tables were rarefied to 5000 observations per sample, and reference-based OTU tables were rarefied to 10000 observations per sample, each using the QIIME 1 script [single_rarefaction.py](http://qiime.org/scripts/single_rarefaction.html). 

#### 1.5 Subsets of tables

Deblur and OTU tables were subset to generate tables with more even representation across sample types and studies, used in many of the analyses as described below. Subsetting of the tables is accomplished by running the IPython notebooks `observation_table.ipynb` and `subset_samples_by_empo_and_study.ipynb` in `code/04-subsets-prevalence`.

<!--
REDBIOM
    # assuming an interactive job
    
    cp /home/mcdonadt/emp-create-redbiomdb/emp-redbiom.rdb /localscratch/
    
    /home/mcdonadt/redis-3.2.6/src/redis-server --daemonize yes --dbfilename /localscratch/emp-redbiom.rdb
    /home/mcdonadt/webdis/webdis &
    
    source activate redbiom
    
    export REDBIOM_HOST=http://127.0.0.1:7379
    
    # IMPORTANT, redis will not service requests until the database is loaded, and it takes a few minutes. redbiom queries during that time will error with a confusing error (hadn't encountered this before...)
    
    # memory foot print is like 18.5GB
    
    # recommending using redis / webdis out of my home right now to avoid compilation, but i think just pointing to redbiom readme would be fine?
-->

### 2 Metadata processing

QIIME mapping files were downloaded from https://qiita.ucsd.edu and refined to fix errors, standardize formatting, and add fields specific for this investigation. The IPython notebook for this metadata processing is `metadata_refine.ipynb` in `code/01-metadata`.

### 3 Generating figures

#### 3.1 Environment type and provenance of EMP samples included in this meta-analysis (Fig. 1)

![](images/figure1_samples.png)

##### 3.1.1. Sankey diagram (Fig. 1a)

Sankey generated from mapping file column `empo_3` using Google Charts [Sankey Diagram](https://developers.google.com/chart/interactive/docs/gallery/sankey). Here is the current version of the Sankey diagram: https://jsfiddle.net/aqxw0cqz/8/. Note that you can turn on the text labels by changing line 61.

##### 3.1.2 World map (Fig. 1b)

Map generated from mapping file columns `latitude_deg` and `longitude_deg` using IPython notebook `map_samples_by_empo.ipynb` in `code/01-metadata`.

#### 3.2 Alpha-diversity, beta-diversity, and predicted average 16S rRNA gene copy number (Fig. 2)

![](images/figure2_abdiv.png)

##### 3.2.1 Alpha-diversity boxplots (Fig. 2a)

Alpha-diversity for the Deblur 90-bp table (QC-filtered) subset was run using the script `alpha_diversity.py` in `code/05-alpha-diversity`. The results for the Deblur 90-bp table rarefied to 5000 sequences per sample were added to the mapping file as the columns adiv_observed_otus, adiv_chao1, adiv_shannon, and adiv_faith_pd.

##### 3.2.2 Alpha-diversity vs. pH and temperature (Fig. 2b)

<!--
Ken's repo: https://github.com/klocey/emp_macroeco
-->

##### 3.2.3 Beta-diversity principal coordinates (Fig. 2c)


##### 3.2.4 Predicted average 16S rRNA copy number (Fig. 2d)


#### 3.3 Nestedness of community composition (Fig. 3)

![](images/figure3_nestedness.png)

##### 3.3.1 Nestedness binary heatmap of all samples (Fig. 3a)

##### 3.3.2 Nestedness binary heatmap of EMPO level 2 classes (Fig. 3b)

##### 3.3.3 NODF scores vs. taxonomic level (Fig. 3c)

<!--
A GitHub repository that can be used to easily replicate the results is located here:

https://github.com/jladau/Nestedness.EMP

As noted in the repository, the data files that were used are posted at this Dropbox link:

https://www.dropbox.com/s/velnv86z1l81ilx/nestedness_emp_data.tar.gz?dl=0

Is there an EMP GitHub repository where the data can be posted, or alternatively, can you point to where these files are already posted? For consistency with the file naming conventions that I used, some of the files in Dropbox are renamed as follows (they have also each been rarefied to 5000 reads):

otu_subset.emp_deblur_90bp.subset_2k.lt_1.0_pc_samp.biom -> Global.Global2000Subset.BacteriaSubset1.EMP.biom
otu_subset.emp_deblur_90bp.subset_2k.lt_5.0_pc_samp.biom -> Global.Global2000Subset.BacteriaSubset5.EMP.biom
otu_subset.emp_deblur_90bp.subset_2k.lt_10.0_pc_samp.biom -> Global.Global2000Subset.BacteriaSubset10.EMP.biom
emp_deblur_90bp.subset_2k.rare_5000.biom -> Global.Global2000Subset.Bacteria.EMP.biom
-->

#### 3.4 Specificity of tag sequences for environment (Fig. 4)

![](images/figure4_entropy.png)

##### 3.4.1 EMPO level 3 distribution of genera and tag sequences (Fig. 4a)

##### 3.4.2 Entropy of EMPO level 3 distribution vs. taxonomic level (Fig. 4b)

##### 3.4.3 Entropy of EMPO level 3 distribution vs. branch length (Fig. 4c)


#### 3.5 Physicochemical properties of the EMP samples (Extended Data Fig. 1)

![](images/figureED1_physicochemical.png)

The pairplot of physicochemical metadata was generated using IPython notebook `physicochemical_pairplot.ipynb` in `code/01-metadata`.

#### 3.6 Sequence length, database effects, and beta-diversity patterns (Extended Data Fig. 2)

![](images/figureED2_seqsdiv.png)

The histogram of median sequence length after trimming (output of split_libraries.py, i.e., sequences downloaded from EBI) was generated using IPython notebook `sequence_length.ipynb` in `code/02-sequence-processing`.

#### 3.7 Sequence length effects on observed diversity patterns (Extended Data Fig. 3)

![](images/figureED3_trimming.png)

#### 3.8 Tag sequence prevalence patterns (Extended Data Fig. 4)

![](images/figureED4_prevalence.png)

#### 3.9 Environmental effect sizes, sample classification, and correlation patterns (Extended Data Fig. 5)

![](images/figureED5_environmental.png)

#### 3.10 NODF scores of nestedness across samples by taxonomic level (Extended Data Fig. 6)

![](images/figureED6_nodf.png)

#### 3.11 Subsets and EMP Trading Cards (Extended Data Fig. 7)

![](images/figureED7_cards.png)

