#### Version 4\_13

The 18S protocol detailed here is designed to amplify eukaryotes broadly
with a focus on microbial eukaryotic lineages. The primers are based on
those of Amaral-Zettler et al 2009 and designed to be used with the
Illumina platform. As with the 16S EMP Illumina protocol, in order to
run 18S libraries on the MISeq and HiSeq please make sure you read the
supplementary methods of Caporaso et al 2012 ISME very carefully – you
will need to make your sample more complex by adding 30-50% PhiX to your
run. The outlines of the protocol are the same as the 16S protocol, but
different primers, PCR conditions, and sequencing primers are used. In
addition, we have designed a blocking primer that reduces the
amplification of vertebrate host DNA to be used on host-associated
samples, especially those that have a low eukaryotic biomass. Blocking
primer strategy is based on Vestheim et al 2008. Throughout
concentrations are listed in µM (micromolar).

-   Amaral-Zettler, LA, EA McCliment, HW Ducklow, SM Huse. 2009. A
    method for studying protistan diversity using massively parallel
    sequencing of V9 hypervariable regions of small-subunit ribosomal
    RNA genes. PLoS ONE 4:e6372.
-   Caporaso JG, Lauber CL, Walters WA, Berg-Lyons D, Huntley J, Fierer
    N, Owens SM, Betley J, Fraser L, Bauer M, Gormley N, Gilbert JA,
    Smith G, Knight R. 2012. Ultra-high-throughput microbial community
    analysis on the Illumina HiSeq and MiSeq platforms. ISME J.
-   Vestheim, H, SN Jarman. 2008. Blocking primers to enhance PCR
    amplification of rare sequences in mixed samples - a case study on
    prey DNA in Antarctic krill stomachs. Frontiers in zoology 5:12.

Download Links
--------------

-   [EMP DNA Extraction
    Protocol](http://press.igsb.anl.gov/earthmicrobiome/files/2013/04/EMP_DNA_extraction_protocol_version_4_13.doc)
-   [18S Illumina Amplification
    Protocol](http://press.igsb.anl.gov/earthmicrobiome/files/2013/04/1391f_EukBr_18S_illumina_amplification_protocol.doc)
    (this document)
-   [Illumina HiSeq 18S Primer
    Sequences](https://dl.dropboxusercontent.com/u/68839641/emp_website/Illumina_Hiseq_euk_primers_master.txt "Illumina HiSeq 18S Primer Sequences")
-   [Primer Ordering and
    Resuspension](http://press.igsb.anl.gov/earthmicrobiome/files/2013/04/EMP_primer_ordering_and_resuspension.doc)

Primer Constructs designed by Laura Wegener Parfrey
---------------------------------------------------

The [primer
sequences](ftp://ftp.metagenomics.anl.gov/data/misc/EMP/Illumina_Hiseq_euk_primers_1391f_EukBr.txt)
in this protocol are always listed in the 5’ -\> 3’ orientation. This is
the orientation that should be used for ordering. See [primer tips and
getting
started](http://press.igsb.anl.gov/earthmicrobiome/files/2013/04/EMP_primer_ordering_and_resuspension.doc)
for information on ordering, concentration, and resuspension.

Illumina\_Euk\_1391f PCR Primer Sequence – Forward primer
---------------------------------------------------------

Field number (space-delimited), description: 1. 5' Illumina adapter 2.
Forward primer pad 3. Forward primer linker 4. Forward primer (1391f)
`AATGATACGGCGACCACCGAGATCTACAC TATCGCCGTT CG GTACACACCGCCCGTC`

Illumina\_EukBr PCR primer sequence – Reverse primer, barcoded
--------------------------------------------------------------

*Each sequence contains a different barcode*
--------------------------------------------

1\. Reverse complement of 3' Illumina adapter 2. Golay barcode 3. Reverse
primer pad 4. Reverse primer linker 5. Reverse primer (EukBr)
`CAAGCAGAAGACGGCATACGAGAT XXXXXXXXXXXX AGTCAGTCAG CA TGATCCTTCTGCAGGTTCACCTAC`
 

Mammal\_block\_I-short\_1391f Mammal Blocking Primer Sequence
-------------------------------------------------------------

`GCCCGTCGCTACTACCGATTGG`/ideoxyI//ideoxyI//ideoxyI//ideoxyI//ideoxyI/`TTAGTGAGGCCCT`/3SpC3/
Mammal blocking primer is to be used when there is a high probability of
picking up host genomic DNA. The C3 spacer (/3SpC3/) is a chemical
modification that prevents extension during the PCR. Please note that
the use of blocking primer reduces the number of host sequences detected
but does not completely eliminate them. Thus remaining host sequences
should also be filtered out during the analysis phase. We have found
blocking primers to be particularly useful for host-associated samples
with a low biomass of eukaryotic DNA. Note: sequence is formatted for
ordering from IDT DNA.

PCR Conditions for Illumina\_Euk\_1391f / Illumina\_EukBr (WITHOUT mammal blocking primer):
-------------------------------------------------------------------------------------------

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
3.  Final primer concentration of mastermix: 0.2 µM

### Thermocycler Conditions (WITHOUT mammal blocking primer)

*Note: Thermocycler conditions optimized for 96 well cyclers.* Step
Temperature Time:

1.  94°C 3 minutes
2.  94°C 45 seconds
3.  57°C 60 seconds
4.  72°C 90 seconds
5.  Repeat steps 2-4 35 times
6.  72°C 10 minutes
7.  4°C HOLD

PCR Conditions for Illumina\_Euk\_1391f / Illumina\_EukBr (WITH mammal blocking primer):
----------------------------------------------------------------------------------------

Complete reagent recipe (master mix) for 1X PCR reaction:

  --------------------------------- ---------
  PCR Grade H2O (note 1, below)     9.0 µL
  5 Primer Hot MM (note 2, below)   10.0 µL
  Forward primer (10µM)             0.5 µL
  Reverse primer (10µM)             0.5 µL
  Blocking Primer (10µM)            4.0 µL
  Template DNA                      1.0 µL
  Total reaction volume             25.0 µL
  --------------------------------- ---------

### Notes:

1.  PCR grade water was purchased from MoBio Laboratories (MoBio Labs:
    Item\#17000-11)
2.  Five Prime Hot Master Mix (5 prime: Item\# 2200410)
3.  Final forward and reverse primer concentration in mastermix: 0.2 µM
4.  Final concentration of blocking primer in mastermix: 1.6
    µMThermocycler Conditions (WITH mammal blocking primer)

### Thermocycler conditions

*Note: Thermocycler conditions optimized for 96 well cyclers.* Step
Temperature Time

1.  94°C 3 minutes
2.  94°C 45 seconds
3.  65°C 15 seconds
4.  57°C 30 seconds
5.  72°C 90 seconds
6.  Repeat steps 2-5 35 times
7.  72°C 10 minutes
8.  4°C HOLD

### Protocol:

1.  Amplify samples in triplicate, meaning each sample will be amplified
    in 3 replicate 25 µL PCR reactions.
2.  Combine the triplicate PCR reactions for each sample into a single
    volume. Combination will result in a total of 75 µL of amplicon for
    each sample. Do NOT combine amplicons from different samples at this
    point.
3.  Run amplicons (with triplicates pooled) on an agarose gel. Expected
    band size for 1391f/Eukbr is roughly 200 bp.
4.  Quantify amplicons with Picogreen (see manufacturers protocol;
    Invitrogen Item \#P11496).
5.  Combine an equal amount of amplicon from each sample into a single,
    sterile tube. Generally 240 ng of DNA per sample are pooled.
    However, larger amounts can be used if the final pool will be gel
    isolated or when working with low biomass samples. Note: When
    working with multiple plates of samples, it is typical to produce a
    single tube of amplicons for each plate of samples.
6.  Clean Amplicon pool using MoBio UltraClean PCR Clean-Up Kit \#12500
    according to the manufacturer’s instructions. If working with more
    than 96 samples, the pool may need to be split evenly for cleaning
    and then recombined. *Optional: if spurious bands were present on
    gel (in step 3), part of the final pool can be run on a gel and then
    gel extracted to select only the target bands. It is a good idea to
    only gel extract part of the pool to prevent against losing the
    entire pool in the event something goes wrong.*
7.  Measure concentration and 260/280 of final pool that has been
    cleaned. For best results the 260/280 should be between 1.8-2.0.
8.  Send an aliquot for sequencing along with sequencing primers listed
    below.

***IMPORTANT:** Sequencing requires use of 18S sequencing primers,
constructs below.*

Euk\_illumina\_read1\_seq\_primer : Read 1 Sequencing Primer
------------------------------------------------------------

*Field, description (space-delimited):*

1.  Forward primer pad
2.  Forward primer linker
3.  Forward primer

`TATCGCCGTT CG GTACACACCGCCCGTC`

Euk\_illumina\_read2\_seq\_primer: Read 2 Sequencing Primer
-----------------------------------------------------------

*Field, description (space-delimited):*

1.  Reverse primer pad
2.  Reverse primer linker
3.  Reverse primer

`AGTCAGTCAG CA TGATCCTTCTGCAGGTTCACCTAC`

Euk\_illumina\_index\_seq\_primer: Index Sequencing Primer
----------------------------------------------------------

*Field, description (space-delimited):*

1.  Reverse complement of reverse primer
2.  Reverse complement of reverse primer linker
3.  Reverse complement of reverse primer pad

`GTAGGTGAACCTGCAGAAGGATCA TG CTGACTGACT`
