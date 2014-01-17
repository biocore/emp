Earth Microbiome Project
========================

Data and analysis results for the Earth Microbiome Project.

Organization of this repository
-------------------------------

* ``data/`` data files used for downstream analysis (biom tables, trees, mapping files, etc)
  * ``biom-urls.txt`` : URLs where BIOM tables can be found - these are not stored in the repository, due to space limitations (``or`` refers to [open-reference OTU picking](http://qiime.org/tutorials/otu_picking.html#open-reference-otu-picking); ``cr`` refers to [closed reference OTU picking](http://qiime.org/tutorials/otu_picking.html#closed-reference-otu-picking))
  * ``master_mapping_file.txt.gz`` : sample metadata for all samples in biom table
  * ``new_refseqs.fna.gz`` the new reference sequence collection resulting from open reference (or) OTU picking
  * ``emp-or-tax-assignments.txt.gz`` taxonomy assignments for open reference (or) biom table
  * ``emp-or.tre.gz`` newick-formatted tree for open reference (or) biom table

* ``code`` code developed for EMP analysis

* ``results`` high-level results (e.g., figures, etc that are useful for presentations)

* ``presentations`` collection of presentations on EMP


Finding older data
------------------

If you're looking for data generated and used for the ISME 14 EMP presentations, [see here](https://github.com/EarthMicrobiomeProject/emp/tree/isme14).


