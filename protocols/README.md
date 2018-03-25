## protocols

This directory contains laboratory protocols and SOPs (or links to them) for sample and metadata collection, sample tracking, amplicon sequencing, shotgun sequencing, and metabolomics.

The first phase of the EMP (2010–2017) explicitly used the DNA extraction and amplicon sequencing protocols, but not necessarily the other protocols, described here. The 16S rRNA amplicon protocol in particular is described in detail by Caporaso et al. ([*PNAS*, 2011](http://doi.org/10.1073/pnas.1000080107)). The full methods used in the meta-analysis of this first phase (Release 1) are described by Thompson et al. ([*Nature*, 2017](http://doi.org/10.1038/nature24621)).

The second phase of the EMP (2016–present), a multi-omics effort informally called "EMP500", uses all of the protocols and SOPs presented here. EMP500 involves the metagenomic sequencing and metabolomic profiling, in addition to amplicon sequencing, of ~500 freshly collected environmental samples from diverse sites on our planet. This multi-omics dataset will be used to address multiple technical and ecological questions in microbial ecology. A biobank of frozen aliquots of samples are being maintained at UCSD and PNNL for future methods testing and analysis.

### Sample collection and aliquot tracking

Samples for EMP500 were collected with standardized methods, in most cases divided into 10 aliquots per sample (please refer to the EMP500 [sample submission guide](http://www.earthmicrobiome.org/in-progress/emp500-sample-submission-guide/)). To track the provenance of these aliquots, we devised a QR barcoding scheme. Ideally, labels should be affixed to aliquot tubes before shipping, and 2-mL screw-cap bead beater tubes should be used to enable direct use in DNA extraction.

QR codes had the format `doe.99.s003.a05` (where "doe" is the PI name, "99" is the study ID, "s003" is the sample number, and "a05" is the aliquot number). Code for generating these codes and other label information in an Excel spreadsheet is in notebooks "s4" and "s5" below. QR codes were printed on XX by XX labels and cap labels (part number XXX) using the XXX printer and ZebraDesigner Pro software for Windows, and scanned into a sample inventory spreadsheet using the BADDASS scanner.

### Metadata collection, curation, and processing

Metadata were requested to comply with MIxS and Qiita standards (please refer to the EMP500 [metadata guide](http://press.igsb.anl.gov/earthmicrobiome/protocols-and-standards/metadata-guide/)). Excel templates were provided corresponding to 15 MIxS environmental packages. The completed spreadsheets were collected from collaborators and checked for completeness and standardized. Terms from [EMPO](http://www.earthmicrobiome.org/protocols-and-standards/empo/), the EMP Ontology of microbial environments, which was developed for EMP500 to improve coverage of microbial environments, were assigned and added to each sample in notebook "s2" below.

The metadata workflow -- from individual study metadata files, general sample information, and prep information -- to mapping files, sample information files, and prep information files -- is summarized by these IPython notebooks:

* `emp500_s1_merge_sample_info.ipynb` - merge individual study metadata files, add general prep information (including plate and well numbers for the initial DNA extraction), generate sample information file
* `emp500_s2_add_prep_info_sample_names.ipynb` - add prep information (16S, 18S, ITS) and sample information (sample names, study information, EMPO categories, etc.)
* `emp500_s3_make_mapping_files_prep_info.ipynb` - generate mapping files and prep information files
* `emp500_s4_project_summary.ipynb` - generate project summary and list of samples (for labels)
* `emp500_s5_labels.ipynb` - generate label spreadsheet with QR codes (not encoded)

### Amplicon sequencing

The standard EMP protocols for DNA extraction and 16S, 18S, and ITS amplicon sequencing are at [earthmicrobiome.org](http://www.earthmicrobiome.org/protocols-and-standards/), which has the following sections:

* [DNA Extraction Protocol](http://www.earthmicrobiome.org/protocols-and-standards/dna-extraction-protocol/)
* [Primer Ordering and Resuspension](http://www.earthmicrobiome.org/protocols-and-standards/primer-ordering-and-resuspension/)
* [16S Illumina Amplicon Protocol](http://www.earthmicrobiome.org/protocols-and-standards/16s/)
* [18S Illumina Amplicon Protocol](http://www.earthmicrobiome.org/protocols-and-standards/18s/)
* [ITS Illumina Amplicon Protocol](http://www.earthmicrobiome.org/protocols-and-standards/its/)

### Shotgun sequencing

* ~10 Gbp/sample

### Metabolomics

