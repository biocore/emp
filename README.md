# Earth Microbiome Project

<div style="float: right; margin-left: 30px;"><img title="The EMP logo was designed by Eamonn Maguire of Antarctic Design." style="float: right;margin-left: 30px;" src="https://upload.wikimedia.org/wikipedia/en/4/4f/EMP-green-small.png" align=right /></div>

The Earth Microbiome Project (EMP) is a systematic attempt to characterize global microbial taxonomic and functional diversity for the benefit of the planet and humankind.

This GitHub repository describes the EMP catalogue -- how it is generated and how to use it. The EMP dataset is generated from samples that individual researchers have compiled and contributed to the EMP. Samples from each group of researchers represent individual EMP studies. In addition to analyses by contributing researchers on individual studies, we perform cross-study meta-analyses. EMP 16S Release 1, a meta-analysis of the first 97 16S rRNA amplicon studies, has been published ([article](http://doi.org/10.1038/nature24621), [preprint](https://github.com/biocore/emp/tree/master/papers)), and the code and methods used for that manuscript are provided here. EMP 16S Release 2, currently unpublished, includes additional 16S rRNA amplicon data. We are currently finalizing the EMP500 - a mult-omics meta-analysis of 50 studies including >500 samples each processed for 16S, 18S, ITS amplicon sequencing, shotgun metagenomic sequencing, and metabolic profiling ([preprint](https://www.biorxiv.org/content/10.1101/2021.06.04.446988v3)). Methods and standard operating procedures (SOPs) for additional amplicon sequencing, shotgun sequencing, and metabolomics related to EMP 16S release 2 and the EMP500 are also provided here.

## Organization of this repository

This repository contains the directories listed below. Each directory will have contents related to EMP 16S Release 1 and EMP Multi-omics (EMP500).

* [`methods`](https://github.com/biocore/emp/tree/master/methods) Methods used in EMP analyses. Includes sample processing for extraction and sequencing, and computational methods for performing analyses and generating figures for meta-analyses of the EMP dataset.
* [`protocols`](https://github.com/biocore/emp/tree/master/protocols) Laboratory protocols and SOPs for sample and metadata collection, sample tracking, amplicon sequencing, shotgun sequencing, and metabolomics.
* [`code`](https://github.com/biocore/emp/tree/master/code) IPython notebooks and scripts (Python, Java, R, Bash) developed for meta-analysis of EMP data; this code is used in `methods`.
* [`data`](https://github.com/biocore/emp/tree/master/data) Data files resulting from or used in processing and analysis.
* [`papers`](https://github.com/biocore/emp/tree/master/papers) Preprints of major meta-analyses of the EMP dataset and links to papers about individual studies.
* [`presentations`](https://github.com/biocore/emp/tree/master/presentations) Links to slide decks from presentations on the EMP.
* [`legacy`](https://github.com/biocore/emp/tree/master/legacy) Early code, results, and website documents from the initial phase of the EMP (2010-2013).

## Getting involved

There are several ways to get involved with the EMP:

* **Use the EMP catalogue in your own research.** Download the whole catalogue or just a few studies, merge and analyze them with your own data, or query the catalogue. Please skip to the next section for detailed instructions.
* **Join the analysis team.** If you are interested in getting involved with EMP meta-analyses, you can begin by reviewing the open [issues](https://github.com/biocore/emp/issues) on this GitHub page. You can add comments to an existing issue to propose your ideas, or create a new issue entirely. Note that the initial meta-analysis of the EMP has been [published](http://doi.org/10.1038/nature24621). You can view the existing [code](https://github.com/biocore/emp/tree/master/code) and [methods](https://github.com/biocore/emp/tree/master/methods) (instructions) for generating figures for the meta-analysis.
* **Contribute samples.** We are not currently soliciting samples for the EMP. If you have an idea for samples you might like to submit in the future, you may [email](mailto:jpshaffer@health.ucsd.edu) Dr. Justin Shaffer.

## Using the EMP catalogue

The EMP catalogue is a diverse and standardized set of thousands of microbiomes for use by the public. Here are some of the ways you can use this resource:

* **Download EMP Release 1 from our FTP site.** EMP 16S Release 1 contains merged and quality-filtered mapping files, BIOM tables, OTU/sequence information, and alpha/beta-diversity results for ~25,000 samples in 97 studies of the initial meta-analysis of the EMP. The [FTP site](ftp://ftp.microbio.me/emp/release1) contains README files about its contents, and the individual files are listed [here](https://github.com/biocore/emp/blob/master/data/ftp_contents.txt).
* **Download individual studies from the Qiita EMP Portal.** For each study, you can download metadata (mapping file), feature tables (BIOM file), and demultiplexed raw sequence files. Like the rest of Qiita, the [EMP Portal](https://qiita.ucsd.edu/emp/) requires the Google Chrome browser.
* **Merge your data with all or part of the EMP dataset.** If you sequenced your sample using the [EMP 16S rRNA primers](http://earthmicrobiome.org/protocols-and-standards/16s/) and picked OTUs using either [Deblur](http://msystems.asm.org/content/2/2/e00191-16) or closed-reference against Greengenes 13.8 or Silva 123, you can merge your BIOM table with the relevant merged EMP 16S Release 1 BIOM table or one of the individual per-study BIOM tables from Qiita. Basic instructions for [initial processing](http://earthmicrobiome.org/protocols-and-standards/initial-qiime-processing/) of your data are provided. You can then use [QIIME1](http://qiime.org/) or [QIIME2](https://qiime2.org/) to merge the BIOM tables and mapping files.
* **Query the EMP catalogue using Redbiom.** [Redbiom](https://github.com/biocore/redbiom) is a command-line tool that allows users to query the Qiita database, including EMP studies. It allows you to find samples based on the sequences or taxa they contain or on sample metadata, and to export selected sample data and metadata. Once you have Redbiom [installed](https://github.com/biocore/redbiom#installation), you can carry out queries such as those described here:

    ```
    # First, summarize the contexts available. A context represents a partition by 
    # processing parameters (e.g., closed-reference OTU picking) and preparation 
    # (e.g., 16S V4).
    
    redbiom summarize contexts | cut -f 1,2,3
    
    # Create a variable for the context. For this example, we will use the closed-
    # reference 16S V4 context by setting a local bash variable "ctx". 
    
    ctx=Pick_closed-reference_OTUs-illumina-16S-v4-66f541
    
    # Query 1: "Show me all the genera that were observed at pH > 8."
    # First we search for samples with pH > 8, then select the features from those 
    # samples, then summarize the taxonomy of those features, then grep for just 
    # the genera and count them.
    
    redbiom search metadata "where ph > 8" | redbiom select features-from-samples \
    --context $ctx | redbiom summarize taxonomy --context $ctx | grep g__ | wc -l
    
    # Answer: There are 1423 genera found in samples with pH > 8.
    
    # Query 2: "Show me all sites where Pyrobaculum are found." 
    # First we search for features that are genus Pyrobaculum, then search for 
    # samples containing those features, then fetch sample metadata for those 
    # samples and output the metadata file, then grab the columns for latitude and 
    # longitude (note: these are not guaranteed to reside in columns 10 and 11).
    
    redbiom search taxon --context $ctx g__Pyrobaculum | redbiom search features \
    --context $ctx | redbiom fetch sample-metadata --context $ctx \
    --output g__Pyrobaculum_metadata.txt; cut g__Pyrobaculum_metadata.txt -f 10,11
    ```

## Citing the EMP

If you use the EMP 16S Release 1 data in your research, please cite Thompson et al., "A communal catalogue reveals Earth's multiscale microbial diversity", *Nature*, 2017 ([article](http://doi.org/10.1038/nature24621)).

If you use the EMP500 data in your research, please cite Shaffer-Nothias-Thompson et al., "Multi-omics profiling of Earth’s biomes reveals that microbial and metabolite composition are shaped by the environment", *bioRxiv*, 2022 ([preprint](https://www.biorxiv.org/content/10.1101/2021.06.04.446988v3)).

If you use EMP protocols in your research, please cite [earthmicrobiome.org](earthmicrobiome.org) and the relevant papers referenced therein.

## File name abbreviation conventions

Some abbreviations used in this repository:

* `demux` is shorthand for "demultiplexed", which describes the fastq data after it is split into per-sample fastq files using barcodes.
* `deblur` refers to the exact-sequence de novo OTU picking method [Deblur](https://github.com/cuttlefishh/deblur).
* `cr` refers to [closed-reference OTU picking](http://qiime.org/tutorials/otu_picking.html#closed-reference-otu-picking).
* `or` refers to [open-reference OTU picking](http://qiime.org/tutorials/otu_picking.html#open-reference-otu-picking).
* `refseqs` refers to reference sequence collections that could be used in reference-based OTU picking.
* `mc2` refers to minimum sequence count in an OTU to be included equals to 2.

## Finding older data

If you're looking for data generated and used for the ISME 14 EMP presentations, look [here](https://github.com/EarthMicrobiomeProject/emp/tree/isme14).
