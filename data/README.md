## data

Data files required to run the scripts and notebooks in `code` and generate the figures described in `methods`.

### Release 1

Data files used in Release 1 (Thompson et al., 2017) are found in several locations:

* Most processed files are in the current directory.
* All files except sequences are on the [EMP FTP site](ftp://ftp.microbio.me/emp/release1), with contents listed in `data/ftp_contents.txt`.
* All files except sequences are in the [Zenodo archive](https://zenodo.org/record/890000) for the [paper](http://doi.org/10.1038/nature24621).
* Sequences are in the [European Nucleotide Archive](http://ebi.ac.uk/ena/), downloaded using scripts in `code/download-sequences`.

### EMP500

Data generated in the EMP500 project are accessible via a Globus Endpoint, which prior to publication is accessible only to project collaborators.

#### Globus instructions

Globus is a high-speed distributed file transfer architecture that enables secure, efficient, and reliable transfers. We have set up a Globus data share for these data. 

Instead of simply transferring files like FTP, Globus uses 'Endpoints' that allow for restarts of interrupted transfers and incremental updates as additional data are added. To access these data, you will need to sign up to Globus using the email address you've provided us, and the set up an endpoint on the computer to which you want to transfer the data. Globus will send you a link giving you access to this share. If you already have a Globus endpoint installed at the destination, you can select that endpoint when clicking the share link. 

How to register for a globus identity and overview of transfer:

* https://docs.globus.org/how-to/get-started/

Installing and connecting personal endpoints:

* https://docs.globus.org/how-to/globus-connect-personal-mac
* https://docs.globus.org/how-to/globus-connect-personal-windows
* https://docs.globus.org/how-to/globus-connect-personal-linux

Additional documentation for setting up Globus:

* https://docs.globus.org/how-to/

#### Globus directory structure

Within each directory of sequence data are subdirectories nammed by PI and study ID, for example "Doe99" (where "Doe" is the PI name and "99" is the EMP500 study ID). Within those subdirectories, the sequence files are named according to the sample IDs in the mapping files (periods in the mapping files are converted to underscores in the sequence file names).

```
public/amplicon/:

public/shotgun/raw/:
  160805_K00180_0231_AHCTHWBBXX_NexteraXT_HiSeq
  161220_K00180_0292_BHG5H3BBXX_KapaHP_HiSeq
  170418_K00180_0352_AHHVLVBBXX_KapaHP_HiSeq
  170703_ILUM_NA_HMWGDMCVY_NexteraXT_NovaSeq
  170721_K00180_0403_AHKNLJBBXX_KapaHP_HiSeq

public/metabolomics/:

```
