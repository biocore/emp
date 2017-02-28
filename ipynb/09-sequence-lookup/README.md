## EMP OTU Trading Cards

### Summary of OTUs

**otu_summary.ipynb**

Gives for each OTU:

* sequence
* num_samples
* num_samples_frac
* num_samples_rank
* total_obs
* total_obs_rank
* total_obs_frac
* list_samples
* taxonomy (Greengenes)

```
# input:
path_table: emp_deblur_100bp.subset_2k.rare_5000.biom
# output:
path_otu_summary: otu_summary.emp_deblur_100bp.subset_2k.rare_5000.tsv
```

### RDP Taxonomy of OTUs

`deblur_blast_xml_to_taxonomy.ipynb`

Gives for each OTU:

* query
* lineage_count (RDP 100% matches)
* species_1st_count (RDP 100% matches)
* species_2nd_count (RDP 100% matches)
* species_3rd_count (RDP 100% matches)

#### Blast strategy

1. blastn -query DEBLUR-SEQS -db ~/databases/rdp-release-11/rdp11.ArchBact.noUncult.fa -perc_identity 100 -out DEBLUR-SEQS.xml -outfmt 5
2. Parse xml to get strain names and taxonomy (with value counts) for each record:
    * query sequence
    * query name
    * alignment strains (value counts)
    * alignment taxonomy (value counts)
3. Output: text file.

#### RDP Database

1. Downloaded unaligned fasta files for Archaea and Bacteria from [RDP Release 11](http://rdp.cme.msu.edu/misc/resources.jsp).
2. Concatenated current_Archaea_unaligned.fa and current_ Bacteria_unaligned.fa.
3. Removed any sequences with "uncultured" in header using fastaSelect.pl.
4. Created blast database: ~/databases/rdp-release-11/rdp11.ArchBact.noUncult.fa.

#### Blast implementation

1. Grab top 500 most prevalent 90-bp, 100-bp, and 150-bp OTUs:

        bash get_top_500_prevalence.sh
        # which generates:
        # otu_seqs_top_500_prev.emp_deblur_100bp.subset_2k.rare_5000.fna

2. Blast top seqs against RDP (here: 90bp, repeat for 100bp and 150bp):

        blastn -db ~/databases/rdp-release-11/rdp11.ArchBact.noUncult.fa -query ~/emp/analyses-otus/otu_seqs_top_500_prev.emp_deblur_90bp.subset_2k.rare_5000.fna -perc_identity 100 -out otu_seqs_top_500_prev.emp_deblur_90bp.subset_2k.rare_5000.xml -outfmt 5

3. Get RDP taxonomy using `deblur_blast_xml_to_taxonomy.ipynb` which generates e.g. `otu_seqs_top_500_prev.emp_deblur_100bp.subset_2k.rare_5000.tsv`.

### OTU Trading Card

otu_trading_card.ipynb<br>

```
# input:
path_map = 'input-tsv/emp_qiime_mapping_subset_2k.tsv'
path_otus = 'input-tsv/otu_summary.emp_deblur_100bp.subset_2k.rare_5000.tsv'
path_rdp = 'input-tsv/otu_seqs_top_500_prev.emp_deblur_100bp.subset_2k.rare_5000.tsv'
# output:
# macros.tex, plots and otu_trading_card.html in a new subdirectory for each OTU
```
