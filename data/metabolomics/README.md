# LC-MS metabolomics results


## Feature metadata

The *feature metadata* table summarizes the results from annotation tools used. The tool used are described in the [methods page](../methods/methods_release2) and the results accessible from their GNPS jobs and the content of the present folder. 

A feature metadata table is available for each of the processing/annotation workflows used:

 - Feature-Based Molecular Networking (FBMN): [`FBMN/FBMN_metabo_feature_metadata.tsv.zip`](FBMN/)
 - Classical Molecular Networking (CMN): [`CMN/CMN_metabo_feature_metadata.tsv.zip`](CMN/)

In the feature metadata table, the column name prefix indicates the source as indicated below:

**GNPS tools**:

- **Molecular networking** (column prefix: `GNPS_`).
- **Spectral library search** (column prefix: `GNPS_LIB_`).
- **Spectral library search in analogue mode** (column prefix: `GNPS_LIBA_`).
- **DEREPLICATOR**, small peptidic molecule annotation (column prefix: `DEREP_`).
- **DEREPLICATOR+**, putative structure annotation (column prefix: `DEREP_`).

**SIRIUS tools**:

- **ZODIAC**: Molecular formula annotation (column prefix: `SIR_MF_`).
- **CSI:FingerID**: Putative structure annotation (column prefix: `SIR_CSI_`).
- **CANOPUS**: Putative chemical class annotation (column prefix: `SIR_CAN_`).

The notebook used to the concatenate the annotations is available at [https://github.com/lfnothias/emp_metabolomics](https://github.com/lfnothias/emp_metabolomics).


### Some insight on how to use these annotations

#### Unsupervised molecular family discovery:

- **Molecular networking** is an unsupervised method that finds related spectra/molecules, also called molecular families. Molecular families shared the same [`GNPS_componentindex`]. If the value is -1, no related spectra were found.

#### Spectral library annotation with GNPS

- Amongst the annotation methods, matching by **spectral library search** (`GNPS_LIB_`) provides the high level of confidence annotation (since we are matching against spectra from real molecules). However these spectral matches could correspond to an isomer, or could be incorrect. In general, the higher the cosine score and the number of shared fragment ions are, the more likely a match is correct (columns [`GNPS_LIB_MQScore`] and [`GNPS_LIB_SharedPeaks`]. In addition, the difference between the precursor ions masses should be less than 10 ppm [`GNPS_LIB_MZErrorPPM`].  

- The **spectral library search in analogue mode** (`GNPS_LIBA_`) works similarly but search for related derivatives, instead of the exact molecule. This analogue mode is more likely to be incorrect. Equivalent columns can be used  [`GNPS_LIBA_MQScore`], [`GNPS_LIBA_SharedPeaks`], [`GNPS_LIBA_MZErrorPPM`].


#### Putative compound annotation with SIRIUS tools

- **ZODIAC** establishes the molecular formula identity. Molecular formula annotations that have a [`Zod_ZodiacScore`] > **0.9** are more likely to be correct. **CSI:FingerID** and **CANOPUS** annotations are derived from molecular formula assignment. Thus, if the [`Zod_ZodiacScore`] < 0.9, the **CSI:FingerID** and **CANOPUS** annotations are more likely to be incorrect.

- **CANOPUS** provides a putative chemical class annotation. This method is *'de novo'* (doesn't require the compound detected to be known). Note that one compound can have multiple class annotations since it uses the ClassyFire ontology. The most informative column is [`CAN_most specific class`], along with [`CAN_subclass`], [`CAN_class`]	, [`CAN_superclass`], [`CAN_all classifications`].

- **CSI:FingerID** provides a putative compound annotation from compound databases. The compound name is in the column [`CSI_name`]. Note that the column [`CSI_links`] contains link out to external database where the compound occur and could be use to define the type  of compound:
	- Natural product: ['COCONUT'](https://coconut.naturalproducts.net/), 'Natural Products', ['SuperNatural'](http://bioinf-applied.charite.de/supernatural_new/index.php).
	- Metabolome database: ['HMDB'](https://hmdb.ca/), ['CHEBI'](https://www.ebi.ac.uk/chebi/), ['KEGG'](https://www.genome.jp/kegg/compound/), ['KEGG Mine'](https://minedatabase.mcs.anl.gov/), 'PubChem class - bio and metabolites'
	- Medically relevant compound: ['MeSH'](https://www.nlm.nih.gov/bsd/disted/meshtutorial/themeshdatabase/index.html).
	- Pollutant: ['NORMAN'](https://www.norman-network.com/), 'PubChem class - safety and toxic'.
	- Non-specific database: ['PubChem'](https://pubchem.ncbi.nlm.nih.gov/) and ['ZINC'](http://zinc.docking.org/).


#### Putative compound annotation with GNPS tools

- **DEREPLICATOR** can search for known or related peptidic small molecules. Those are often produced my micro-organismes. In general, the higher the score the more likely the annotation is correct [`DEREP_score`].

- **DEREPLICATOR+** provides an compound annotation. In general, the higher the score the more likely the annotaiton is correct annotation [`DEREP+_score`].

## Feature table

To be released.