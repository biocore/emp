#### Version 4\_13

## Primers for amplicon community sequencing

Please see this
article: [Caporaso JG, Lauber CL, Walters WA, Berg-Lyons D, Huntley J,
Fierer N, Owens SM, Betley J, Fraser L, Bauer M, Gormley N, Gilbert JA,
Smith G, Knight R. 2012. Ultra-high-throughput microbial community
analysis on the Illumina HiSeq and MiSeq platforms. **ISME
J.**](http://www.nature.com/ismej/journal/vaop/ncurrent/full/ismej20128a.html)
For running these libraries on the MiSeq and HiSeq please make sure you
read the supplementary methods of the above manuscript very well – you
will need to make your sample more complex by adding **5-10%** PhiX to
your run.

Download Links
--------------

-   [EMP DNA Extraction
    Protocol](http://press.igsb.anl.gov/earthmicrobiome/files/2013/04/EMP_DNA_extraction_protocol_version_4_13.doc)
-   [New 16S Illumina Amplification
    Protocol](https://dl.dropboxusercontent.com/u/68839641/emp_website/515f_806_16S_illumina_amplification_protocol_version_6_15.doc)
-   [Old 16S Illumina Amplification
    Protocol](http://press.igsb.anl.gov/earthmicrobiome/files/2013/04/515f_806_16S_illumina_amplification_protocol_version_4_13.doc)
-   [Old Illumina 16S Primer
    Sequences](ftp://ftp.metagenomics.anl.gov/data/misc/EMP/SupplementaryFile1_barcoded_primers_515F_806R.txt)
    (515f - 806r)
-   [New Illumina 16S Primer
    Sequences](https://dl.dropboxusercontent.com/u/68839641/emp_website/515f_806rb_new.xls)
    (515f - 806rB)
-   [New Illumina 16S Primer
    Sequences](https://dl.dropboxusercontent.com/u/68839641/emp_website/515f_926r_new.xlsx)
    (515f - 926r)
-   [Illumina 18S Primer - Coming soon](#)
-   [Illumina ITS 1/2 Primer - Coming soon](#)
-   [Primer Ordering and
    Resuspension](http://press.igsb.anl.gov/earthmicrobiome/files/2013/04/EMP_primer_ordering_and_resuspension.doc)

Primer Constructs designed by Greg Caporaso
-------------------------------------------

The primer sequences in this protocol are always listed in the 5’ -\> 3’
orientation. This is the orientation that should be used for ordering.
See [primer tips and getting
started](http://press.igsb.anl.gov/earthmicrobiome/files/2013/04/EMP_primer_ordering_and_resuspension.doc)
for information on ordering, concentration, and resuspension. **Original
EMP primers have been modified slightly:**

-   barcodes are now located on the forward (515) primer to enable the
    usage of various reverse primer constructs to enable longer
    amplicons (tested on 806r and 926r)
-   Degeneracy was added to both the forward and reverse primers (see
    below), with the intent of removing known biases against
    Crenarchaeota/Thaumarchaeota (515f modification) and the marine and
    freshwater Alphaproteobacterial clade SAR11 (806r modification)

515f PCR Primer Sequence – Forward primer
-----------------------------------------

*Field description (space-delimited):*

1.  5' Illumina adapter
2.  Golay barcode
3.  Forward primer pad
4.  Forward primer linker
5.  Forward primer (515f)

`AATGATACGGCGACCACCGAGATCTACAC XXXXXXXXXXXX TATGGTAATT GT GTGYCAGCMGCCGCGGTAA`

806r PCR primer sequence – Reverse primer
-----------------------------------------

*Field description (space-delimited):*

1.  Reverse complement of 3' Illumina adapter
2.  Reverse primer pad
3.  Reverse primer linker
4.  Reverse primer (806r)

`CAAGCAGAAGACGGCATACGAGAT AGTCAGTCAG CC GGACTACNVGGGTWTCTAAT`

Illumina PCR Conditions: 515f-806r region of the 16S rRNA gene (Caporaso et al PNAS 2010):
------------------------------------------------------------------------------------------

### Complete reagent recipe (master mix) for 1X PCR reaction

  --------------------------------- ---------
  PCR Grade H2O (note 1, below)     13.0 µL
  5 Primer Hot MM (note 2, below)   10.0 µL
  Forward primer (10µM)             0.5 µL
  Reverse primer (10µM)             0.5 µL
  Template DNA                      1.0 µL
  Total reaction volume             25.0 µL
  --------------------------------- ---------

### Notes:

1.  PCR grade water was purchased from MoBio Laboratories (MoBio Labs:
    Item\#17000-11)
2.  Five Prime Hot Master Mix (5 prime: Item\# 2200410)
3.  Final primer concentration of master mix: 0.2 µM

### Thermocycler Conditions for 96 well thermocyclers:

1.  94°C 3 minutes
2.  94°C 45 seconds
3.  50°C 60 seconds
4.  72°C 90 seconds
5.  Repeat steps 2-4 35 times
6.  72°C 10 minutes
7.  4°C HOLD

### Thermocycler Conditions for 384 well thermocyclers:

1.  94°C 3 minutes
2.  94°C 60 seconds
3.  50°C 60 seconds
4.  72°C 105 seconds
5.  Repeat steps 2-4 35 times
6.  72°C 10 minutes
7.  4°C HOLD

### Protocol:

1.  Amplify samples in triplicate, meaning each sample will be amplified
    in 3 replicate 25 µL PCR reactions.
2.  Combine the triplicate PCR reactions for each sample into a single
    volume. Combination will result in a total of 75 µL of amplicon for
    each sample. Do NOT combine amplicons from different samples at this
    point.
3.  Run amplicons for each sample on an agarose gel. Expected band size
    for 515f/806r is roughly 300 - 350 bp.
4.  Quantify amplicons with Picogreen (see manufacturers protocol;
    Invitrogen Item \#P11496).
5.  Combine an equal amount of amplicon from each sample into a single,
    sterile tube. Generally 240 ng of DNA per sample are pooled.
    However, higher amounts can be used if the final pool will be gel
    isolated or when working with low biomass samples. (*Note: When
    working with multiple plates of samples, it is typical to produce a
    single tube of amplicons for each plate of samples.*)
6.  Clean Amplicon pool using MoBio UltraClean PCR Clean-Up Kit \#12500
    according to the manufacturer’s instructions. If working with more
    than 96 samples, the pool may need to be split evenly for cleaning
    and then recombined. (*Optional: if spurious bands were present on
    gel (in step 3), ½ of the final pool can be run on a gel and then
    gel extracted to select only the target bands.*)
7.  Measure concentration and 260/280 of final pool that has been
    cleaned. For best results the 260/280 should be between 1.8-2.0.
8.  Send an aliquot for sequencing along with sequencing primers listed
    below.

***IMPORTANT:** Sequencing requires use of 16S and Index sequencing
primers, constructs below.*

Read 1 sequencing primer:
-------------------------

*Field description (space-delimited):*

1.  Forward primer pad
2.  Forward primer linker
3.  Forward primer

`TATGGTAATT GT GTGYCAGCMGCCGCGGTAA`

Read 2 sequencing primer:
-------------------------

*Field description (space-delimited):*

1.  Reverse primer pad
2.  Reverse primer linker
3.  Reverse primer

`AGTCAGTCAG CC GGACTACNVGGGTWTCTAAT`

Index sequence primer:
----------------------

*Field description (space-delimited):*

1.  Reverse complement of reverse primer
2.  Reverse complement of reverse primer linker
3.  Reverse complement of reverse primer pad

`ATTAGAWACCCBDGTAGTCC GG CTGACTGACT`

Next Steps:
-----------

-   [16S Taxonomic
    Assignments](http://www.earthmicrobiome.org/emp-standard-protocols/16s-taxonomic-assignments/)
-   [Metadata
    Formatting](http://www.earthmicrobiome.org/emp-standard-protocols/metadata-formatting/)

Related Protocols:
------------------

-   [18S rRNA Amplification
    Protocol](http://www.earthmicrobiome.org/emp-standard-protocols/18s/)
-   Shotgun Metagenomics Protocol - Shotgun metagenomics is being
    performed using Illumina 2x125bp HiSeq2000 protocols. A full
    description will follow.

