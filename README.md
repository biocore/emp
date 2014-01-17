Earth Microbiome Project
========================

Data and analysis results for the Earth Microbiome Project.

Organization of this repository
-------------------------------

* ``data/`` data files used for downstream analysis (biom tables, trees, mapping files, etc)
  * ``biom-urls.txt`` : URLs where BIOM tables can be found - these are not stored in the repository, due to space limitations (``or`` refers to open-reference OTU picking; ``cr`` refers to closed reference OTU picking)
  * ``master_mapping_file.txt.gz`` : sample metadata for all samples in biom table
  * ``new_refseqs.fna.gz`` the new reference sequence collection
  * ``emp-or-tax-assignments.txt.gz`` taxonomy assignments for open reference OTU picking

* ``code`` code developed for EMP analysis

* ``results`` high-level results (e.g., figures, etc that are useful for presentations)

* ``presentations`` collection of presentations on EMP


Finding older data
------------------

If you're looking for data generated and used for the ISME 14 EMP presentations, [see here](https://github.com/EarthMicrobiomeProject/emp/tree/isme14).


