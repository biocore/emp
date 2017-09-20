#~/bin/bash

# Description of the starting OTU table: emp_or_orig.biom
# The emp_or.biom table is the BIOM table generated from the pick_open_reference_otus.py command named otu_table_mc2_w_tax.biom in which the study 1098 has been removed
# The reason why such study has been removed is because we cannot trust the barcode information that we had in the mapping file at demultiplexing time

# We also need to filter study 1740
#echo "filter_samples_from_otu_table.py -i $PWD/emp_or_orig.biom -o $PWD/emp_or_no_1740.biom --sample_id_fp /home/jona1883/EMP/mapping_files/1740_prep_58_qiime_20141124-091855.txt --negate_sample_id_fp" | qsub -N EMP_F1740 -m abe -M josenavasmolina@gmail.com -l pmem=32gb -l walltime=2:00:00

# Start Greg's workflow
# Filter the OTUs that are present in a single sample
#echo "filter_otus_from_otu_table.py -i $PWD/emp_or_no_1740.biom -o $PWD/emp_or.biom -s 2" | qsub -N EMPORFMS2 -m abe -M josenavasmolina@gmail.com -l pmem=64gb -l walltime=01:00:00
# Drop those representative sequences
#echo "filter_fasta.py -f $PWD/rep_set.fna -o $PWD/rep_set_ms2.fna -b $PWD/emp_or.biom" | qsub -N EMPORFFMS2 -m abe -M josenavasmolina@gmail.com -l pmem=32gb -l walltime=02:00:00
# Align sequences using ssu-align - FAILED
#echo "cd $PWD; ssu-align rep_set_ms2.fna ssu-align-ms2/" | qsub -N EMPORSSUA -m abe -M josenavasmolina@gmail.com -l pmem=32gb -l walltime=48:00:00
# Rerun using the parallel version
# ssu-prep rep_set_ms2.fna parallel_100 100 presuf.txt -f
# These 2 doesn't work (they're using the default masks)
# ssu-mask -a parallel_100.bacteria.stk -d
# ssu-mask -a parallel_100.archaea.stk -d
# Use the new masks from Eric
#echo "cd /home/jona1883/EMP/ANALYSES/open_ref/ssu-align; ssu-mask -a parallel_100/parallel_100.archaea.stk -s new_masks/arc.arc-bac.rfam12.1183-1s.1508c.mask --key-out arc-bac-mask; ssu-mask -a parallel_100/parallel_100.bacteria.stk -s new_masks/bac.arc-bac.rfam12.1183-1s.1582c.mask --key-out arc-bac-mask" | qsub -m abe -M josenavasmolina@gmail.com -l pmem=32gb -l walltime=100:00:00 -N EMPNMsk
# Run FastTree
#echo "export OMP_NUM_THREADS=60; FastTreeMP -nosupport -fastest -nt $PWD/ssu-align/parallel_100.all.arc-bac-mask.afa > $PWD/rep_set_ms2.tre" | qsub -m abe -M josenavasmolina@gmail.com -l walltime=480:00:00 -l nodes=1:highmem:ppn=60 -l pmem=8gb -N FTEMP
#echo "export OMP_NUM_THREADS=8; FastTreeMP -nosupport -fastest -nt $PWD/ssu-align/parallel_100.all.arc-bac-mask.afa > $PWD/rep_set_ms2_8threads.tre" | qsub -m abe -M josenavasmolina@gmail.com -l walltime=480:00:00 -l nodes=1:highmem:ppn=8 -l pmem=60gb -N FTEMP





#echo "biom summarize-table -i $PWD/emp_or.biom -o $PWD/obs_summaryi.txt --observations" | qsub -N EMPOBSSUM -m abe -M josenavasmolina@gmail.com -l pmem=40gb -l walltime=00:30:00

# Get the table summary
#echo "biom summarize-table -i $PWD/emp_or.biom -o $PWD/summaries/emp_or_mc2.summary.txt" | qsub -N EMPORSUM -m abe -M josenavasmolina@gmail.com -l pmem=4gb -l walltime=00:10:00

#Filter doubletons 
#echo "filter_otus_from_otu_table.py -i $PWD/emp_or.biom -o $PWD/emp_or_mc3.biom -n 3" | qsub -N EMPORFDOUB -m abe -M josenavasmolina@gmail.com -l pmem=32gb -l walltime=01:00:00
#sleep 2
#echo "filter_otus_from_otu_table.py -i $PWD/emp_or.biom -o $PWD/emp_or_mc2.biom -n 2" | qsub -N EMPORFSINGL -m abe -M josenavasmolina@gmail.com -l pmem=32gb -l walltime=01:00:00

# Filtering OTUs that are present in only a single sample, and then dropping those representative sequences
#echo "filter_otus_from_otu_table.py -i $PWD/emp_or.biom -o $PWD/emp_or_ms2.biom -s 2" | qsub -N EMPORFMS2 -m abe -M josenavasmolina@gmail.com -l pmem=32gb -l walltime=01:00:00
#echo "filter_fasta.py -f $PWD/rep_set.fna -o $PWD/rep_set_ms2.fna -b $PWD/emp_or_ms2.biom" | qsub -N EMPORFFMS2 -m abe -M josenavasmolina@gmail.com -l pmem=32gb -l walltime=02:00:00
#echo "biom summarize-table -i $PWD/emp_or_ms2.biom -o $PWD/summaries/emp_or_ms2.summary.txt" | qsub -N EMPORSUMMS2 -m abe -M josenavasmolina@gmail.com -l pmem=32gb -l walltime=00:10:00

# Align sequences using ssu-align
#echo "cd $PWD; ssu-align rep_set_ms2.fna ssu-align-ms2/" | qsub -N EMPORSSUALIGN -m abe -M josenavasmolina@gmail.com -l pmem=32gb -l walltime=24:00:00








# Rarefy table
#mkdir $PWD/bdiv_even10k
#echo "single_rarefaction.py -i $PWD/emp_cr_mc2.biom -o $PWD/bdiv_even10k/emp_cr_mc2_even10k.biom -d 10000" | qsub -N EMPCR10K -m abe -M josenvasmolina@gmail.com -l pmem=4gb -l walltime=00:45:00

# Run beta diversity on the rarefied table
#echo "parallel_beta_diversity.py -i $PWD/bdiv_even10k/emp_cr_mc2_even10k.biom -o $PWD/bdiv_even10k -m unweighted_unifrac -t $HOME/software/gg_otus-13_8-release/trees/97_otus.tree -T -O 100 -U /home/jona1883/software/bin/cluster_jobs_64_barnacle.py" | qsub -N EMPCR10Kbdiv -m abe -M josenavasmolina@gmail.com -l walltime=240:00:00 -l pmem=200gb





#echo "parallel_beta_diversity.py -i /home/jona1883/EMP/EMP_CR_NEW/analyses/emp_cr_mc2_even20k.biom -o /home/jona1883/EMP/EMP_CR_NEW/analyses/bdiv_even20k -m unweighted_unifrac -t $HOME/software/gg_otus-13_8-release/trees/97_otus.tree -T -O 100 -U /home/jona1883/software/bin/cluster_jobs_64_barnacle.py" | qsub -N bdiv_20k -m abe -M josenavasmolina@gmail.com -l walltime=240:00:00 -l pmem=200gb

#echo "principal_coordinates.py -i /home/jona1883/EMP/EMP_CR_NEW/analyses/bdiv_even20k/unweighted_unifrac_emp_cr_mc2_even20k.txt -o /home/jona1883/EMP/EMP_CR_NEW/analyses/bdiv_even20k/unweighted_unifrac_emp_cr_mc2_even20k_pc.txt" | qsub -N pc_20k -m abe -M josenavasmolina@gmail.com -l walltime=24:00:00 -l pmem=64gb

#echo "make_emperor.py -i /home/jona1883/EMP/EMP_CR_NEW/analyses/bdiv_even20k/unweighted_unifrac_emp_cr_mc2_even20k_pc.txt -m /home/jona1883/EMP/emp_mapping_file.txt -o /home/jona1883/EMP/EMP_CR_NEW/analyses/bdiv_even20k/unweighted_unifrac_20k_plots" | qsub -N me_20k -m abe -M josenavasmolina@gmail.com -l walltime=12:00:00 -l pmem=32gb
