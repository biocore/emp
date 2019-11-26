## code/download-sequences

This code is described in the following section(s) of [`methods/methods_release1.md`](https://github.com/biocore/emp/blob/master/methods/methods_release1.md):

**1.1:**

* `download_ebi_fasta.sh`
* `download_ebi_fastq.sh`

### Mapping EBI sample accessions to Qiita/EMP sample names

There are 97 studies in EMP 16S Release 1. Study IDs in EMP are identical to their corresponding Qiita study IDs, which have the format of a 2- to 5-digit number. The corresponding EBI study accessions have the format "ERP" followed by a 6-digit number. Each study ID (Qiita/EMP format) has an associated EBI study accession. These are listed in `study_ids_qiita_ebi.tsv`.

On each study page on [Qiita](https://qiita.ucsd.edu/), you can find mappings of the Qiita/EMP sample names to the EBI sample accessions. For your convenience, these sample name mappings are provided in the directory `ebi-sample-accessions`.

