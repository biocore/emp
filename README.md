Earth Microbiome Project
========================

<div style="float: right; margin-left: 30px;"><img title="The EMP logo was designed by Eamonn Maguire of Antarctic Design." style="float: right;margin-left: 30px;" src="http://www.earthmicrobiome.org/files/2011/01/EMP-green-small.png" align=right /></div>

The [Earth Microbiome Project](www.earthmicrobiome.org) (EMP) is a systematic attempt to characterize the global microbial taxonomic and functional diversity for the benefit of the planet and mankind. 

The EMP is open science: anyone can get involved. The EMP data set is generated from samples that individual researchers have compiled and donated to the EMP. These data sets represent individual EMP studies. In addition to the individual studies, we are performing a cross-study meta-analysis. All per-study raw data is publicly available in the [EMP portal](http://www.microbio.me/emp) to the [QIIME](www.qiime.org) database. This repository contains the processed, combined (i.e., across study) EMP data for the EMP meta-analysis as well as code developed specifically for the EMP meta-analyses, and new results as they are generated.

If you're interested in getting involved in [EMP data analyses](https://github.com/EarthMicrobiomeProject/emp/issues) you should begin by reviewing the [open issues](https://github.com/EarthMicrobiomeProject/emp/issues). These describe analyses that we're interested in performing across studies. If you're interested in working on one of these analyses, or have ideas for other analyses that should be performed, you should get in touch with Greg Caporaso (gregcaporaso@gmail.com), the Chief Data Analyst for the EMP. 

Additional information is available on the [Earth Microbiome Project website](www.earthmicrobiome.org).

Organization of this repository
-------------------------------

* ``data/`` data files used for downstream analysis (biom tables, trees, mapping files, etc)
  * ``data-urls.txt`` URLs where large data files can be found (e.g., BIOM and tree files). These are not stored in the repository, due to space limitations. You can download all of these files by running ``wget -i data-urls.txt`` from this directory.
    * ``emp-or.tre.gz`` newick-formatted tree corresponding to open reference (or) biom table
    * ``emp-or.biom.gz`` open-reference (or) biom table
    * ``emp-cr.biom.gz`` closed-reference (cr) biom table
    * ``refseqs.fna.gz`` the new reference sequence collection resulting from open reference (or) OTU picking
  * ``sample-map.txt.gz`` sample metadata (i.e., mapping) file for all samples in biom table
  * ``observation-map.txt.gz`` observation (OTU) metadata (e.g., taxonomy assignments) for open reference (or) biom table

* ``code`` code developed for EMP analysis

* ``results`` high-level results (e.g., figures, etc that are useful for presentations)

* ``presentations`` collection of presentations on EMP

File name abbreviation conventions
----------------------------------

* ``or`` refers to [open-reference OTU picking](http://qiime.org/tutorials/otu_picking.html#open-reference-otu-picking)
* ``cr`` refers to [closed-reference OTU picking](http://qiime.org/tutorials/otu_picking.html#closed-reference-otu-picking)
* ``refseqs`` refers to reference sequence collections that could be used in reference-based OTU picking

Finding older data
------------------

If you're looking for data generated and used for the ISME 14 EMP presentations, [see here](https://github.com/EarthMicrobiomeProject/emp/tree/isme14).


