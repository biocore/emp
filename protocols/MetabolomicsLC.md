## Metabolomics protocols (LC-MS)

The LC-MS-based metabolomics experiments were designed to extract and detect a large spectrum of middle polarity metabolites due to the fact that:

	- The extractions were carried out with 7/3 MeOH/H2O.
	- Solid phase extraction (SPE) was performed with a mixed polarity stationary phase. 
	- The LC was performed in reversed-phase with a C18 stationary phase column. 

It is understood that, while LC-MS based metabolomics is a sensitive method, it is NOT a universal detection method and thus is highly compositional. In the present protocol, metabolites are detected only if:
	
	- The metabolites are soluble in the extraction can be detected.
	- The metabolites were recovered from the SPE process.
	- The metabolites are eluting over C18-based column chromatography.
	- The metabolites can be ionised in a electrospray ionisation source in positive ionisation mode.
	- The ions formed are above the limit of detection of the intrument.
	- The ions are annotated only if a fragmentation spectrum (MS/MS) is collected.

### Sample preparation

The samples were prepared by Melissa Esposito, Kevin Ngoc, Fernando Vargas, and Louis Felix Nothias (nothias@ucsd.edu) from the [Dorrestein Lab at University of California San Diego](https://dorresteinlab.ucsd.edu/).

#### Sample extraction
All solvents and reactants used were LC-MS grade. To maximise the extraction yield, the samples were prepared differently based on their sampling method (bulk, filter, swabs, controls), and organised on seven 96-well plates depending on depending on their environmental package (host-associated, misc. environment, sediment, soil, microbial mat/biofilm, water, plant-associated, and wastewater/sludge).
 
1. The swabs were transferred in a 96 well plate (polypropylene-based), and dissolved in 1.0 mL of 9/1 EtOH/H2O. The plate was put in an µLtrasonic bath for 30 min, and after 12 hours at 4°C, the swabs were removed from the wells. 
2. The filter samples were dissolved in 1.5 mL of 7/3 MeOH/H2O, and the tubes were put in an µLtrasonic bath for 30 min. After 12 hours at 4°C, the filters were removed from the tubes, and the supernatant was collected in a 96 well plate (polypropylene-based). 
3. The bulk samples were dissolved in 7/3 MeOH/H2O, in a volume varying from 600 µL to 1.5 mL depending on the available amounts, and homogenized in a tissue-lyser (QIAGEN) at 25 Hz for 5 min. Then, the tubes were centrifuged at 15,000 rpm for 15 min, and the supernatant was collected in a 96 well plate (polypropylene-based). 
4. For the material control samples (bags, filters, and tubes) 3.0 mL of 2/8 MeOH/H2O were added and 1.5 mL were recovered after two minutes, and added as control wells in the 96 well plates (polypropylene-based). 

	After the extraction, the plates were dried with a vaccum concentrator.

#### Solid phase microextraction (SPE)
	
This SPE step is done to remove both salts (reduce ionisation efficiency), very polar compounds (not retained by C18 LC column) as well as very apolar compounds that would carry over runs.
	
1. The samples (in plates) were dissolved in 300 µL of 7/3 MeOH/H2O, and put in an µLtrasound bath for 20 min. 
2. Solid phase extraction were performed with SPE plates (Oasis HLB, Hydrophilic-Lipophilic-Balance, 30 mg with particle sizes of 30 um).
	- 	The SPE beds were activated with 100% MeOH, and equilibrated with 100% H2O.
	-   The samples were loaded on the SPE beds, and 100% H2O was used as wash solvent (600 µL). The eluted solution was discarded (it contains salts and very polar metabolites that are subsequent analysis are not designed for).
	-   The sample elution was carried out sequentially with 7/3 MeOH/H2O (600 µL) and with 100% methanol (600 µL). 
	-   The obtained plates were dried with a vaccum concentrator.
3. Preparation for mass spectrometry analysis
	-	The samples were resuspended in 130 µL of 7/3 MeOH/H2O containing 0.2 uM of amitriptyline as internal standard. 
	-   The plates were centrifugated at 2,000 rpm for 15 min at 4°C
	-   100 µL of samples were transferred into a new 96 well plate (polypropylene-based) for mass spectrometry analysis.


### Mass Spectrometry Analysis (non targeted LC-MS/MS)

The analysis were Louis Felix Nothias (nothias@ucsd.edu) from the [Dorrestein Lab at University of California San Diego](https://dorresteinlab.ucsd.edu/).

Samples were analyzed using ultra high performance liquid chromatography (Vanquish, Thermo Scientific) coupled to a quadrupole-Orbitrap mass spectrometer (Q Exactive, Thermo Scientific) operating in data-dependent acquisition mode (LC-M/MS in DDA mode). 

#### Chromatography
Chromatographic separation was done using a Kinetex C18 1.7 µm  (Phenomenex, Torrance, USA), 100 Å pore size, 2.1 mm (internal diameter) x 50 mm (length) column with a C18 guard cartridge (Phenomenex). The column was maintained at 40°C. The mobile phases used were 0.1% formic acid in water (A) and 0.1% formic acid in acetonitrile (B). Chromatographic elution method was set as follows: 0.00-1.00 min, isocratic 5% B; 1.00-9.00 min, gradient from 5% to 100% B; 9.00-11.00 min, isocratic 100% B; and followed by equilibration: 11.00 -11.50 min, gradient from 100% to 5% B; 11.50 - 12.50 min, isocratic 5% B. The flow rate was set to 0.5 mL/min.

#### Mass Spectrometry
Mass spectrometry was performed in electrospray ionization, in positive mode, was performed using a heated electrospray ionization source with the following source parameters: spray voltage, +3496.2 V; heater temperature, 363.90°C; capillary temperature, 377.50°C; S-lens RF, 60 (arb. units); sheath gas flow rate, 60.19 (arb. units); and auxiliary gas flow rate, 20.00 (arb. units). The MS1 scans were acquired at a resolution (at m/z 200) of 35,000 in the 100-1500 m/z range, and the MS2 scans at a resolution of 17,500 from 0 to 12.5 min. The automatic gain control (AGC) target and maximum injection time were set at 1 x 10^6 and 160 ms for MS1 scans, and set at 5 x 10^5 and 220 ms for MS2 scans, respectively. Up to three MS2 scans in data-dependent mode (TOP3) were acquired for most abundant ions per duty cycle, with a starting value of m/z 50. Higher-energy collision induced dissociation was performed with a normalized collision energy of 20, 30, 40 eV. The apex trigger mode was used (4 to 15 sec), the isotopes were excluded and dynamic exclusion was set to 11 seconds. The major background ions originating from the SPE were excluded manually from the MS2 acquisition.

#### Batch preparation
The injections were randomized within a plate. Blanks samples were analyzed every 20 injections. QCmix samples were injected at the beginning, the middle, and the end of each plate sequence. The chromatographic shift observed throughout the batch is estimated as less than 2 seconds, and the relative standard deviation was +/- 15% per replicates. The samples are containing the internal standards (amitriptyline, m/z 278.19, 3.81 min). 
