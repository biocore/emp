#!/bin/bash

#echo "parallel_merge_otu_tables.py -i /home/jona1883/EMP/EMP_OR_NEW/0/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/1/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/2/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/3/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/4/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/5/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/6/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/7/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/8/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/9/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/10/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/11/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/12/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/13/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/14/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/15/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/16/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/17/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/18/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/19/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/20/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/21/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/22/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/23/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/24/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/25/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/26/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/27/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/28/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/29/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/30/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/31/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/32/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/33/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/34/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/35/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/36/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/37/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/38/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/39/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/40/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/41/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/42/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/43/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/44/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/45/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/46/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/47/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/48/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/49/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/50/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/51/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/52/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/53/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/54/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/55/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/56/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/57/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/58/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/59/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/60/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/61/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/62/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/63/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/64/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/65/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/66/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/67/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/68/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/69/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/70/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/71/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/72/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/73/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/74/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/75/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/76/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/77/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/78/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/79/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/80/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/81/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/82/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/83/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/84/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/85/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/86/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/87/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/88/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/89/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/90/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/91/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/92/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/93/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/94/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/95/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/96/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/97/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/98/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/99/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/100/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/101/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/102/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/103/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/104/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/105/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/106/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/107/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/108/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/109/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/110/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/111/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/112/otu_table_mc2.biom,/home/jona1883/EMP/EMP_OR_NEW/113/otu_table_mc2.biom -o /home/jona1883/EMP/EMP_OR_NEW/otu_table_mc2.biom -C -X EMP_MOTU" | qsub -N EMP_M -m abe -M josenavasmolina@gmail.com -q mem8gbq

# Create the phylogenetic tree
# Step 1: align the seqs
#echo "parallel_align_seqs_pynast.py -i /home/jona1883/EMP/EMP_OR_NEW/rep_set.fna -o /home/jona1883/EMP/EMP_OR_NEW/pynast_aligned_seqs -O 100 -T" | qsub -N EMP_ALIGN -m abe -M josenavasmolina@gmail.com -q mem32gbq
# Step 2: filter the alignment
#echo "filter_alignment.py -o $PWD/pynast_aligned_seqs/ -i $PWD/pynast_aligned_seqs/rep_set_aligned.fasta" | qsub -N EMP_FILT -m abe -M josenavasmolina@gmail.com -q mem128gbq
# Step 3: make phylogeny
#echo "make_phylogeny.py -i $PWD/pynast_aligned_seqs/rep_set_aligned_pfiltered.fasta -o $PWD/rep_set.tre -l $PWD/log_make_phylogeny.txt" | qsub -N EMP_TREE -m abe -M josenavasmolina@gmail.com -q mem128gbq

# Assign taxonomy
# We run it on parallel using uclust since sortmerna is not available
#echo "parallel_assign_taxonomy_uclust.py -i /home/jona1883/EMP/EMP_OR_NEW/rep_set.fna -o /home/jona1883/EMP/EMP_OR_NEW/uclust_assigned_taxonomy -T -O 100" | qsub -N EMP_TAX -m abe -M josenavasmolina@gmail.com -q mem32gbq
# We run it on serial using sortmerna
#echo "assign_taxonomy.py -i /home/jona1883/EMP/EMP_OR_NEW/rep_set.fna -o /home/jona1883/EMP/EMP_OR_NEW/sortmerna_assigned_taxonomy -m sortmerna --sortmerna_threads 60" | qsub -N EMP_TAX_SMR -m abe -M josenavasmolina@gmail.com -q mem8gbq -l nodes=1:ppn=60

# Add the taxonomy information to the OTU table
#echo "biom add-metadata -i $PWD/otu_table_mc2.biom/merged.biom --observation-metadata-fp $PWD/sortmerna_assigned_taxonomy/rep_set_tax_assignments.txt -o $PWD/otu_table_mc2_w_tax.biom --sc-separated taxonomy --observation-header OTUID,taxonomy" | qsub -N EMP_ADDMETA -m abe -M josenavasmolina@gmail.com -q mem32gbq

# Filter the OTU table for pynast failures
#echo "filter_otus_from_otu_table.py -i $PWD/otu_table_mc2_w_tax.biom -o $PWD/otu_table_mc2_w_tax_no_pynast_failures.biom -e $PWD/pynast_aligned_seqs/rep_set_failures.fasta" | qsub -N EMP_TAXFP -m abe -M josenavasmolina@gmail.com -q mem64gbq
#echo "filter_otus_from_otu_table.py -i $PWD/otu_table_mc2.biom/merged.biom -o $PWD/otu_table_mc2_no_pynast_failures.biom -e $PWD/pynast_aligned_seqs/rep_set_failures.fasta" | qsub -N EMP_FILTPYNAST -m abe -M josenavasmolina@gmail.com -q mem32gbq



# Study 1098 was incorrectly demultiplexed - remove those samples from the OTU table
#echo "filter_samples_from_otu_table.py -i $PWD/otu_table_mc2_w_tax.biom -o $PWD/otu_table_mc2_w_tax_no_1098.biom --sample_id_fp /home/jona1883/EMP/mapping_files/1098_prep_21_qiime_20141124-091850.txt --negate_sample_id_fp" | qsub -N EMP_F1098 -m abe -M josenavasmolina@gmail.com -q mem32gbq

# ---------------------------------------------------------------------------------------------------------
# Filtering the Adaptors - we need to perform a lot of different checks and
# analysis to make sure if some samples are more affected than others
# The sequences that should be removed from the representative set are (OTU count):
#	ATCTCGTATGCCGTCTTCTGC (1108396)
#	GCAGAAGACGGCATACGAGAT (22406)
#	GTAGTCCGGCTGACTGACT (1582369)
#	AGTCAGTCAGCCGGACTAC (3396)
#
# At the end, we want to get a table like this:
# sample_id	adapter_observed	number_of_sequences_impacted	number_of_sequences_in_sample
#
# These sequences can affect the tree reconstruction (not the taxonomy assignment) so we need to
# re-generate the tree.
# ---------------------------------------------------------------------------------------------------------
#mkdir adaptor_clean_up

# First, get the sequences for each adaptor
adaptors=(ATCTCGTATGCCGTCTTCTGC GCAGAAGACGGCATACGAGAT GTAGTCCGGCTGACTGACT AGTCAGTCAGCCGGACTAC)

#for i in ${adaptors[@]}
#do
    # Create a folder for each adaptor so we can count them individually
    #mkdir adaptor_clean_up/$i
    # First step, find the affected sequences
    #cat rep_set.fna | grep $i -B 1 --no-group-separator > adaptor_clean_up/$i/bad_seqs.fna

    # Generate a single file with all the bad sequences
    #cat adaptor_clean_up/$i/bad_seqs.fna >> adaptor_clean_up/sequences_to_filter.fna

    # Get an OTU table in which the current adaptor OTUs have been filtered out
    #echo "filter_otus_from_otu_table.py -i $PWD/otu_table_mc2_w_tax_no_1098.biom -o $PWD/adaptor_clean_up/$i/otu_table_no_$i.biom -e $PWD/adaptor_clean_up/$i/bad_seqs.fna" | qsub -N EMP_F_$i -m abe -M josenavasmolina@gmail.com -q mem32gbq
    # Get an OTU table that contains only the adaptor OTUs
    #echo "filter_otus_from_otu_table.py -i $PWD/otu_table_mc2_w_tax_no_1098.biom -o $PWD/adaptor_clean_up/$i/otu_table_only_$i.biom -e $PWD/adaptor_clean_up/$i/bad_seqs.fna --negate_ids_to_exclude" | qsub -N EMP_F_O_$i -m abe -M josenavasmolina@gmail.com -q mem32gbq
    # Filter the samples from the OTU tables that do not have any read
    #echo "filter_samples_from_otu_table.py -i $PWD/adaptor_clean_up/$i/otu_table_no_$i.biom -o $PWD/adaptor_clean_up/$i/otu_table_no_${i}_f.biom -n 1" | qsub -N F_$i -m abe -M josenavasmolina@gmail.com -q mem32gbq
    #echo "filter_samples_from_otu_table.py -i $PWD/adaptor_clean_up/$i/otu_table_only_$i.biom -o $PWD/adaptor_clean_up/$i/otu_table_only_${i}_f.biom -n 1" | qsub -N FN_$i -m abe -M josenavasmolina@gmail.com -q mem32gbq
#done

# Get an OTU table in which the adaptor OTUs have been filtered out
#echo "filter_otus_from_otu_table.py -i $PWD/otu_table_mc2_w_tax_no_1098.biom -o $PWD/adaptor_clean_up/otu_table_mc2_w_tax_no_1098_no_adaptor_otus.biom -e $PWD/adaptor_clean_up/sequences_to_filter.fna" | qsub -N EMP_F_ADAP -m abe -M josenavasmolina@gmail.com -q mem32gbq
# Get an OTU table that contains only the adaptor OTUs
#echo "filter_otus_from_otu_table.py -i $PWD/otu_table_mc2_w_tax_no_1098.biom -o $PWD/adaptor_clean_up/otu_table_mc2_w_tax_no_1098_only_adaptor_otus.biom -e $PWD/adaptor_clean_up/sequences_to_filter.fna --negate_ids_to_exclude" | qsub -N EMP_G_ADAP -m abe -M josenavasmolina@gmail.com -q mem32gbq

# Get the table summaries
#mkdir $PWD/adaptor_clean_up/table_summaries
#echo "biom summarize-table -i $PWD/otu_table_mc2_w_tax_no_1098.biom -o $PWD/adaptor_clean_up/table_summaries/otu_table_mc2_w_tax_no_1098.summary.txt" | qsub -N NO1098summ -m abe -M josenavasmolina@gmail.com -q mem32gbq
#echo "biom summarize-table -i $PWD/adaptor_clean_up/otu_table_mc2_w_tax_no_1098_no_adaptor_otus.biom -o $PWD/adaptor_clean_up/table_summaries/otu_table_mc2_w_tax_no_1098_no_adaptor_otus.summary.txt" | qsub -N NOADAPsumm -m abe -M josenavasmolina@gmail.com -q mem32gbq
#echo "biom summarize-table -i $PWD/adaptor_clean_up/otu_table_mc2_w_tax_no_1098_only_adaptor_otus.biom -o $PWD/adaptor_clean_up/table_summaries/otu_table_mc2_w_tax_no_1098_only_adaptor_otus.summary.txt" | qsub -N ADAPsumm -m abe -M josenavasmolina@gmail.com -q mem8gbq

# Filter the samples that do not have any read from the OTU tables
#echo "filter_samples_from_otu_table.py -i $PWD/adaptor_clean_up/otu_table_mc2_w_tax_no_1098_no_adaptor_otus.biom -o $PWD/adaptor_clean_up/otu_table_mc2_w_tax_no_1098_no_adaptor_otus_f.biom -n 1" | qsub -N NOADAPF -m abe -M josenavasmolina@gmail.com -q mem32gbq
#echo "filter_samples_from_otu_table.py -i $PWD/adaptor_clean_up/otu_table_mc2_w_tax_no_1098_only_adaptor_otus.biom -o $PWD/adaptor_clean_up/otu_table_mc2_w_tax_no_1098_only_adaptor_otus_f.biom -n 1" | qsub -N ADAPF -m abe -M josenavasmolina@gmail.com -q mem32gbq

# Get the summaries
#echo "biom summarize-table -i $PWD/adaptor_clean_up/otu_table_mc2_w_tax_no_1098_only_adaptor_otus_f.biom -o $PWD/adaptor_clean_up/table_summaries/otu_table_mc2_w_tax_no_1098_only_adaptor_otus_f.summary.txt" | qsub -N ADAPFsumm -m abe -M josenavasmolina@gmail.com -q short8gb -l mem=32gb -l walltime=2:00:00
#echo "biom summarize-table -i $PWD/adaptor_clean_up/otu_table_mc2_w_tax_no_1098_no_adaptor_otus_f.biom -o $PWD/adaptor_clean_up/table_summaries/otu_table_mc2_w_tax_no_1098_no_adaptor_otus_f.summary.txt" | qsub -N NOADAPFsumm -m abe -M josenavasmolina@gmail.com -q short8gb -l mem=32gb -l walltime=2:00:00

# Filter the adaptor sequences from the representative set
#echo "filter_fasta.py -f $PWD/rep_set.fna -o $PWD/adaptor_clean_up/rep_set_filtered.fna -a $PWD/adaptor_clean_up/sequences_to_filter.fna -n" | qsub -N FILT_REPSET -m abe -M josenavasmolina@gmail.com -q mem4gbq

# Re-run the phylogeny reconstruction
# Step 1: align the seqs
#echo "parallel_align_seqs_pynast.py -i $PWD/adaptor_clean_up/rep_set_filtered.fna -o $PWD/adaptor_clean_up/pynast_aligned_seqs -O 100 -T" | qsub -N EMP_F_ALIGN -m abe -M josenavasmolina@gmail.com -q mem32gbq
# Step 2: filter the alignment
#echo "filter_alignment.py -o $PWD/adaptor_clean_up/pynast_aligned_seqs -i $PWD/adaptor_clean_up/pynast_aligned_seqs/rep_set_filtered_aligned.fasta" | qsub -N EMP_F_FILT -m abe -M josenavasmolina@gmail.com -q mem128gbq
#echo "filter_alignment.py -o $PWD/adaptor_clean_up/pynast_aligned_seqs_new -i $PWD/adaptor_clean_up/pynast_aligned_seqs_new/rep_set_filtered_aligned.fasta -m $PWD/adaptor_clean_up/new_mask.txt" | qsub -N EMP_F_FIL -m abe -M josenavasmolina@gmail.com -l pmem=128gb
# Step 3: Make the phylogeny
#echo "make_phylogeny.py -i $PWD/adaptor_clean_up/pynast_aligned_seqs/rep_set_filtered_aligned_pfiltered.fasta -o $PWD/adaptor_clean_up/rep_set_filtered.tre -l $PWD/adaptor_clean_up/log_make_phylogeny.txt" | qsub -N EMP_F_TREE -m abe -M josenavasmolina@gmail.com -q mem512gbq
#echo "FastTree -spr 4 -gamma -fastest -no2nd < $PWD/adaptor_clean_up/pynast_aligned_seqs_filtered_85/rep_set_filtered_aligned_pfiltered.fasta > $PWD/adaptor_clean_up/rep_set.tre" | qsub -N EMP_TREE -m abe -M josenavasmolina@gmail.com -l nodes=1:ppn=24 -l mem=250gb -l pmem=8gb -l walltime=4752:00:00

#echo "parallel_align_seqs_pynast.py -i $PWD/adaptor_clean_up/rep_set_filtered.fna -o $PWD/adaptor_clean_up/pynast_aligned_seqs_filtered_85 -O 100 -T -t $PWD/adaptor_clean_up/85_aligned_seqs_filtered.fna -U ~/software/bin/cluster_jobs_8_barnacle.py" | qsub -N EMP_F_ALIGN -m abe -M josenavasmolina@gmail.com -l pmem=32gb -l walltime=03:00:00
#echo "filter_alignment.py -o $PWD/adaptor_clean_up/pynast_aligned_seqs_filtered_85/ -i $PWD/adaptor_clean_up/pynast_aligned_seqs_filtered_85/rep_set_filtered_aligned.fasta -m $PWD/adaptor_clean_up/new_mask.txt" | qsub -N EMP_F_FIL2 -m abe -M josenavasmolina@gmail.com -l pmem=128gb -l walltime=03:00:00


# Filter the pynast failures from the otu table
#echo "filter_otus_from_otu_table.py -i $PWD/adaptor_clean_up/otu_table_mc2_w_tax_no_1098_no_adaptor_otus_f.biom -o $PWD/otu_table_mc2_w_tax_no_1098_no_adaptor_otus_f_no_pynast_failures.biom -e $PWD/adaptor_clean_up/pynast_aligned_seqs/rep_set_filtered_failures.fasta" | qsub -N EMP_TAXFP -m abe -M josenavasmolina@gmail.com -l pmem=64gb -l walltime=03:00:00

#echo "biom summarize-table -i $PWD/otu_table_mc2_w_tax_no_1098_no_adaptor_otus_f_no_pynast_failures.biom -o $PWD/all_filters.summ.txt" | qsub -N empsumm -m abe -M josenavasmolina@gmail.com -l pmem=32gb -l walltime=00:30:00

# Filter the all filters tables to remove the samples that do not have any sequence
#echo "filter_samples_from_otu_table.py -i $PWD/otu_table_mc2_w_tax_no_1098_no_adaptor_otus_f_no_pynast_failures.biom -o $PWD/emp_or.biom -n 1" | qsub -N emp_f_samples -m abe -M josenavasmolina@gmail.com -l walltime=01:30:00 -l pmem=32gb
#echo "biom summarize-table -i $PWD/emp_or.biom -o $PWD/emp_or.summ.txt" | qsub -N empsum -m abe -M josenavasmolina@gmail.com -l pmem=32gb -l walltime=00:30:00

# Generate tree using ghost-tree
#echo "ghost-tree filter-alignment-positions /home/jona1883/software/gg_otus-13_8-release/rep_set_aligned/97_otus.fasta 0.9 0.8 /home/jona1883/EMP/EMP_OR_NEW/adaptor_clean_up/ghost_tree_emp_tree/97_otus_aligned_filtered.fasta" | qsub -N EMP_gt_1 -m abe -M josenavasmolina@gmail.com -l pmem=32gb -l walltime=24:00:00
#echo "ghost-tree extensions group-extensions /home/jona1883/EMP/EMP_OR_NEW/adaptor_clean_up/rep_set_filtered.fna 0.8 /home/jona1883/EMP/EMP_OR_NEW/adaptor_clean_up/ghost_tree_emp_tree/rep_set_map_80.txt" | qsub -N EMP_gt_2 -m abe -M josenavasmolina@gmail.com -l pmem=32gb -l walltime=300:00:00
#echo "cd $PWD/adaptor_clean_up/ghost_tree_emp_tree/; ghost-tree scaffold hybrid-tree rep_set_map_80.txt tax_assignments_no_u_no_spaces_genera.txt ../rep_set_filtered.fna 97_otus_aligned_filtered.fasta EMP_ghosttree.tre" | qsub -N EMP_gt_3 -m abe -M josenavasmolina@gmail.com -l pmem=32gb -l walltime=300:00:00
