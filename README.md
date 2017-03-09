Earth Microbiome Project
========================

<div style="float: right; margin-left: 30px;"><img title="The EMP logo was designed by Eamonn Maguire of Antarctic Design." style="float: right;margin-left: 30px;" src="http://www.earthmicrobiome.org/files/2011/01/EMP-green-small.png" align=right /></div>

The [Earth Microbiome Project](www.earthmicrobiome.org) (EMP) is a systematic attempt to characterize global microbial taxonomic and functional diversity for the benefit of the planet and humankind.

The EMP is open science: anyone can get involved. The EMP data set is generated from samples that individual researchers have compiled and donated to the EMP. The samples from each group of researchers represent individual EMP studies. In addition to analyses being done by contributing researchers on the individual studies, we are performing a cross-study meta-analysis. All per-study raw data is publicly available through the [EMP Portal](https://qiita.ucsd.edu/emp/) of the [Qiita](https://qiita.ucsd.edu/) database. This GitHub repository contains resources for the EMP meta-analysis: links to the processed, combined (across studies) EMP data on our [FTP site](ftp://ftp.microbio.me/emp/latest); code developed specifically for the EMP meta-analyses; and results of initial analyses, with new results added as they are generated.

If you're interested in getting involved in [EMP data analyses](https://github.com/EarthMicrobiomeProject/emp/issues) you should begin by reviewing the [open issues](https://github.com/EarthMicrobiomeProject/emp/issues). These describe analyses that we're interested in performing across studies. If you're interested in working on one of these analyses, or have ideas for other analyses that should be performed, you should get in touch with [Luke Thompson] (lukethompson@gmail.com), the project leader for the EMP. 

Additional information is available on the [Earth Microbiome Project website](www.earthmicrobiome.org).

Organization of this repository
-------------------------------

* `data/` data files used for downstream analysis (biom tables, trees, mapping files, etc)
    - `data_locations.txt` links to where large data files can be found (e.g., BIOM and tree files)
    - `MIxS/` Excel files describing MIxS, EBI, and Qiita metadata standard requirements; used to generate metadata templates
    - `sequence-lookup/` files used for the EMP Trading Cards (sequence lookup) notebooks (e.g., RDP taxonomy files)

* `ipynb/` IPython notebooks and scripts (Python, Java, R, Bash) developed for meta-analysis of EMP data (Thompson et al., in prep.)
    - `01-metadata-processing/`
    - `02-sequence-processing/`
    - `03-otu-picking/`
    - `04-rarefaction-and-subsets/`
    - `05-alpha-diversity/`
    - `06-beta-diversity/`
    - `07-environmental-covariation/`
    - `08-cooccurrence-and-nestedness/`
    - `09-sequence-lookup/`

* `legacy/` code, results, and website documents from the early phase of the EMP (2010-2013)

* `presentations/` collection of presentations on the EMP

* `results/` diversity analyses and high-level results (e.g., figures and tables that are useful for presentations)
    - `results_locations.txt` links to where large results files can be found (e.g., alpha- and beta-diversity results)

* `scripts/` utility scripts and code not specific to particular analyses
    - `01-metadata-templates/`
    - `02-colors-and-styles/`
    - `03-phylogenetic-placement/`

File name abbreviation conventions
----------------------------------

* `or` refers to [open-reference OTU picking](http://qiime.org/tutorials/otu_picking.html#open-reference-otu-picking)
* `cr` refers to [closed-reference OTU picking](http://qiime.org/tutorials/otu_picking.html#closed-reference-otu-picking)
* `refseqs` refers to reference sequence collections that could be used in reference-based OTU picking
* `mc2` refers to minimum sequence count in an OTU to be included equals to 2

Finding older data
------------------

If you're looking for data generated and used for the ISME 14 EMP presentations, [see here](https://github.com/EarthMicrobiomeProject/emp/tree/isme14).


