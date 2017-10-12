Earth Microbiome Project
========================

<div style="float: right; margin-left: 30px;"><img title="The EMP logo was designed by Eamonn Maguire of Antarctic Design." style="float: right;margin-left: 30px;" src="http://www.earthmicrobiome.org/files/2011/01/EMP-green-small.png" align=right /></div>

The Earth Microbiome Project (EMP) is a systematic attempt to characterize global microbial taxonomic and functional diversity for the benefit of the planet and humankind. Most of the data generated to this point are from 16S rRNA amplicon surveys, but the project also includes data from 18S and ITS amplicons, metagenomics, and metabolomics. For more information about the EMP -- people, publications, news, protocols and standards, and more -- please see the [EMP website](http://www.earthmicrobiome.org/).

This GitHub repository describes the EMP catalogue and how to use it. The EMP dataset is generated from samples that individual researchers have compiled and contributed to the EMP. Samples from each group of researchers represent individual EMP studies. In addition to analyses being done by contributing researchers on the individual studies, we are performing cross-study meta-analyses. A meta-analysis of the first 97 16S rRNA amplicon studies -- EMP 16S Release 1 -- is currently in press (Thompson et al., *Nature*, 2017, [doi:10.1038/nature24621](http://doi.org/10.1038/nature24621)); the analysis code for that manuscript is provided here.

Getting involved
----------------

There are several ways to get involved with the EMP:

* **Use the EMP catalogue in your own research.** Download the whole catalogue or just a few studies, merge and analyze them with your own data, or query the catalogue. Please skip to the next section for detailed instructions.
* **Join the analysis team.** If you are interested in getting involved with EMP meta-analyses, you can begin by reviewing the open [issues](https://github.com/biocore/emp/issues) on this GitHub page. You can add comments to an existing issue to propose your ideas, or create a new issue entirely. Note that the initial meta-analysis of the EMP has been accepted for publication. You can view the existing [code](https://github.com/biocore/emp/tree/master/code) for generating [figures](https://github.com/biocore/emp/tree/master/figures) for the meta-analysis.
* **Contribute samples.** We are not currently soliciting samples for the EMP. If you have an idea for samples you might like to submit in the future, you may [email](mailto:lukethompson@gmail.com) the project leader for the EMP, Dr. Luke Thompson.

Using the EMP catalogue
-----------------------

The EMP catalogue is a diverse and standardized set of thousands of microbiomes for use by the public. Here are some of the ways you can use this resource:

* **Download EMP Release 1 from our FTP site.** EMP Release 1 contains merged and quality-filtered mapping files, BIOM tables, OTU/sequence information, and alpha/beta-diversity results for ~25,000 samples in 97 studies of the initial meta-analysis of the EMP. The [FTP site](ftp://ftp.microbio.me/emp/release1) contains README files about its contents, and the individual files are listed [here](https://github.com/biocore/emp/blob/master/data/ftp_contents.txt).
* **Download individual studies from the Qiita EMP Portal.** For each study, you can download metadata (mapping file), feature tables (BIOM file), and demultiplexed raw sequence files. Like the rest of Qiita, the [EMP Portal](https://qiita.ucsd.edu/emp/) requires the Google Chrome browser.
* **Merge your data with all or part of the EMP dataset.** If you sequenced your sample using the [EMP 16S rRNA primers](http://www.earthmicrobiome.org/protocols-and-standards/16s/) and picked OTUs using either [Deblur](http://msystems.asm.org/content/2/2/e00191-16) or closed-reference against Greengenes 13.8 or Silva 123, you can merge your BIOM table with the relevant merged EMP Release 1 BIOM table or one of the individual per-study BIOM tables from Qiita. Basic instructions for [initial processing](http://www.earthmicrobiome.org/protocols-and-standards/initial-qiime-processing/) of your data are provided. You can then use [QIIME1](http://qiime.org/) or [QIIME2](https://qiime2.org/) to merge the BIOM tables and mapping files.
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

Organization of this repository
-------------------------------

This repository contains the following directories:

* `code` IPython notebooks and scripts (Python, Java, R, Bash) developed for meta-analysis of EMP data; this code is used in the top-level directory `figures`.
* `data` Data files used for processing and downstream analysis.
* `figures` Instructions to generate the figures in "A communal catalogue reveals Earth’s multiscale microbial diversity", Thompson et al., *Nature* (2017).
* `legacy` Early code, results, and website documents from the initial phase of the EMP (2010-2013).
* `presentations` Collection of presentations on the EMP.

File name abbreviation conventions
----------------------------------

Some abbreviations used in this repository:

* `demux` is shorthand for "demultiplexed", which describes the fastq data after it is split into per-sample fastq files using barcodes.
* `deblur` refers to the exact-sequence de novo OTU picking method [Deblur](https://github.com/cuttlefishh/deblur).
* `cr` refers to [closed-reference OTU picking](http://qiime.org/tutorials/otu_picking.html#closed-reference-otu-picking).
* `or` refers to [open-reference OTU picking](http://qiime.org/tutorials/otu_picking.html#open-reference-otu-picking).
* `refseqs` refers to reference sequence collections that could be used in reference-based OTU picking.
* `mc2` refers to minimum sequence count in an OTU to be included equals to 2.

Finding older data
------------------

If you're looking for data generated and used for the ISME 14 EMP presentations, look [here](https://github.com/EarthMicrobiomeProject/emp/tree/isme14).
