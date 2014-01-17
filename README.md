Earth Microbiome Project
========================

Data and analysis results for the Earth Microbiome Project.

Organization of this repository
-------------------------------

* ``data/`` data files used for downstream analysis (biom tables, trees, mapping files, etc)
  * ``data-urls.txt`` : URLs where large data files can be found (e.g., BIOM and tree files) - these are not stored in the repository, due to space limitations
    * ``emp-or.tre.gz`` newick-formatted tree corresponding to open reference (or) biom table
    * ``emp-or.biom.gz`` open-reference (or) biom table
    * ``emp-cr.biom.gz`` closed-reference (cr) biom table
  * ``sample-map.txt.gz`` : sample metadata (i.e., mapping) file for all samples in biom table
  * ``observation-map.txt.gz`` observation (OTU) metadata (e.g., taxonomy assignments) for open reference (or) biom table
  * ``refseqs.fna.gz`` : the new reference sequence collection resulting from open reference (or) OTU picking [COMING SOON]

* ``code`` code developed for EMP analysis

* ``results`` high-level results (e.g., figures, etc that are useful for presentations)

* ``presentations`` collection of presentations on EMP

File name abbreviation conventions
----------------------------------

``or`` refers to [open-reference OTU picking](http://qiime.org/tutorials/otu_picking.html#open-reference-otu-picking)
``cr`` refers to [closed reference OTU picking](http://qiime.org/tutorials/otu_picking.html#closed-reference-otu-picking))
``refseqs`` refers to reference sequence collections that could be used in reference-based OTU picking

Finding older data
------------------

If you're looking for data generated and used for the ISME 14 EMP presentations, [see here](https://github.com/EarthMicrobiomeProject/emp/tree/isme14).


