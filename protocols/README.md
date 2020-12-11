## protocols

This directory contains laboratory protocols and SOPs (or links to them) for sample- and metadata collection, sample tracking, sample extraction, amplicon sequencing, shotgun metagenomic sequencing, and metabolomic profiling. 

Accompanying information to `protocols`:

* [`methods`](https://github.com/biocore/emp/blob/master/methods) Methods used in EMP analyses.
* [`code`](https://github.com/biocore/emp/tree/master/code) Notebooks and scripts for reproducing analyses.
* [`data`](https://github.com/biocore/emp/tree/master/data) Results of sequence processing and analyses.

### Overview

The first phase of the EMP (2010-2017) explicitly used the DNA extraction and amplicon sequencing protocols—but not necessarily the other protocols—described here. The 16S rRNA amplicon protocol in particular is described in detail by Caporaso et al. ([*PNAS*, 2011](http://doi.org/10.1073/pnas.1000080107)). The full methods used in the meta-analysis of this first phase (Release 1) are described by Thompson et al. ([*Nature*, 2017](http://doi.org/10.1038/nature24621)).

The second phase of the EMP (2016-present), a multi-omics effort informally called "EMP500", uses all of the protocols and SOPs presented here. EMP500 involves the metagenomic sequencing and metabolomic profiling, in addition to amplicon sequencing, of ~500 freshly collected environmental samples from diverse sites on our planet. This multi-omics dataset will be used to address multiple technical and ecological questions in microbial ecology. A biobank of frozen aliquots of samples are being maintained at UCSD and PNNL for future methods testing and analysis.

### Sample collection and aliquot tracking

Maintaining multiple (~10) individual frozen aliquots of each raw bulk sample is suggested. This minimizes freeze-thaw cycles and permits multiple future downstream processing protocols. Instructions are provided in the [EMP Sample Submission Guide](https://dx.doi.org/10.17504/protocols.io.pfqdjmw). 

To track the provenance of these aliquots, we employ the following QR barcoding scheme:

* Tubes should be 2-mL screw-cap bead beater tubes to enable direct use in DNA extraction.
* Labels should be affixed to aliquot tubes before shipping. 
* QR codes have the format `doe.99.s003.a05`, where "doe" is the PI name, "99" is the study ID, "s003" is the sample number, and "a05" is the aliquot number. 
* QR codes (version 2, 25x25) are printed on Cryogenic Direct Thermal Labels, 1.125" x 0.75" rectangluar labels and 0.437" circular cap labels (GA International, part no. DFP-70) using a Zebra model GK420d printer and ZebraDesigner Pro software for Windows.
* Before aliquots are put away, QR codes are scanned into a sample inventory spreadsheet using a QR scanner.

### Metadata collection, curation, and processing

Metadata should comply with MIMS and Qiita standards. Please refer to the EMP500 [metadata guide](http://www.earthmicrobiome.org/protocols-and-standards/metadata-guide/).

### Amplicon sequencing

The standard EMP protocols for DNA extraction and 16S, 18S, and ITS amplicon sequencing are at [earthmicrobiome.org](http://www.earthmicrobiome.org/protocols-and-standards/), which has the following sections:

* [DNA Extraction Protocol](http://www.earthmicrobiome.org/protocols-and-standards/dna-extraction-protocol/)
* [Primer Ordering and Resuspension](http://www.earthmicrobiome.org/protocols-and-standards/primer-ordering-and-resuspension/)
* [16S Illumina Amplicon Protocol](http://www.earthmicrobiome.org/protocols-and-standards/16s/)
* [18S Illumina Amplicon Protocol](http://www.earthmicrobiome.org/protocols-and-standards/18s/)
* [ITS Illumina Amplicon Protocol](http://www.earthmicrobiome.org/protocols-and-standards/its/)

Since EMP release 1 described in Thompson et al. ([*Nature*, 2017](http://doi.org/10.1038/nature24621), important updates to the EMP amplicon sequencing protocols have been made - these will be summarized soon on the EMP website linked above:

* [16S PCR update 1], miniaturized reactions, described in Minich et al. ([*mSystems*, 2018](https://doi.org/10.1128/mSystems.00166-18)
* [16S PCR update 2], single reactions (i.e., vs. triplicate), described in Marotz et al. ([*BioTechniques*, 2019](https://doi.org/10.2144/btn-2018-0192)

### Shotgun sequencing

The standard EMP protocols for short-read shotgun metagenomic sequencing are described in Sanders et al. ([*Genome Biology*, 2019](https://doi.org/10.1186/s13059-019-1834-9)).

### Metabolomics

The protocol for [non-targeted metabolomics analysis by LC-MS/MS](MetabolomicsLC.md). 

The protocol for [non-targeted metabolomics analysis by GC-MS](MetabolomicsGC.md). 
