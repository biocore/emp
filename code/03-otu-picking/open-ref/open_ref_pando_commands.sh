#!/bin/bash

emp_dir=/scratch/Users/emhy1389/EMP/
sl_dir=$emp_dir/split_libraries
param_fp=$emp_dir/open_ref_params.txt
gg_dir=/Users/emhy1389/software/qiime_software/gg_otus-13_8-release
gg_rep_set=$gg_dir/rep_set/97_otus.fasta
gg_tax=$gg_dir/taxonomy/97_otu_taxonomy.txt
gg_smr=$gg_dir/SortMeRNA/97_otus_db.idx

#echo "pick_open_reference_otus.py -i $sl_dir/1001/seqs.fna,$sl_dir/1024/seqs.fna,$sl_dir/1030/seqs.fna,$sl_dir/1031/seqs.fna,$sl_dir/1033/seqs.fna,$sl_dir/1034/seqs.fna,$sl_dir/1035/seqs.fna,$sl_dir/1036/seqs.fna,$sl_dir/1037/seqs.fna,$sl_dir/1038/seqs.fna,$sl_dir/1039/seqs.fna,$sl_dir/1041/seqs.fna,$sl_dir/1043/seqs.fna,$sl_dir/1056/seqs.fna,$sl_dir/1064/seqs.fna,$sl_dir/1098/seqs.fna,$sl_dir/1197/seqs.fna,$sl_dir/1198/seqs.fna,$sl_dir/1222/seqs.fna,$sl_dir/1235/seqs.fna,$sl_dir/1240/seqs.fna,$sl_dir/1242/seqs.fna,$sl_dir/1288/seqs.fna,$sl_dir/1289/seqs.fna,$sl_dir/1453/seqs.fna,$sl_dir/1481/seqs.fna,$sl_dir/1521/seqs.fna,$sl_dir/1526/seqs.fna,$sl_dir/1578/seqs.fna,$sl_dir/1579/seqs.fna,$sl_dir/1580/seqs.fna,$sl_dir/1621/seqs.fna,$sl_dir/1622/seqs.fna,$sl_dir/1627/seqs.fna,$sl_dir/1632/seqs.fna,$sl_dir/1642/seqs.fna,$sl_dir/1665/seqs.fna,$sl_dir/1673/seqs.fna,$sl_dir/1674/seqs.fna,$sl_dir/1692/seqs.fna,$sl_dir/1694/seqs.fna,$sl_dir/1696/seqs.fna,$sl_dir/1702/seqs.fna,$sl_dir/1711/seqs.fna,$sl_dir/1713/seqs.fna,$sl_dir/1714/seqs.fna,$sl_dir/1715/seqs.fna,$sl_dir/1716/seqs.fna,$sl_dir/1717/seqs.fna,$sl_dir/1721/seqs.fna,$sl_dir/1734/seqs.fna,$sl_dir/1736/seqs.fna,$sl_dir/1740/seqs.fna,$sl_dir/1747/seqs.fna,$sl_dir/1748/seqs.fna,$sl_dir/1773/seqs.fna,$sl_dir/1774/seqs.fna,$sl_dir/1799/seqs.fna,$sl_dir/829/seqs.fna,$sl_dir/889/seqs.fna,$sl_dir/713/seqs.fna,$sl_dir/895/seqs.fna,$sl_dir/810/seqs.fna,$sl_dir/805/seqs.fna,$sl_dir/2080/seqs.fna,$sl_dir/861/seqs.fna,$sl_dir/808/seqs.fna,$sl_dir/632/seqs.fna,$sl_dir/807/seqs.fna,$sl_dir/809/seqs.fna,$sl_dir/776/seqs.fna,$sl_dir/659/seqs.fna,$sl_dir/910/seqs.fna,$sl_dir/925/seqs.fna,$sl_dir/958/seqs.fna,$sl_dir/905/seqs.fna,$sl_dir/2182/seqs.fna,$sl_dir/2300/seqs.fna,$sl_dir/662/seqs.fna,$sl_dir/940/seqs.fna,$sl_dir/846/seqs.fna,$sl_dir/963/seqs.fna,$sl_dir/804/seqs.fna,$sl_dir/2338/seqs.fna,$sl_dir/678/seqs.fna,$sl_dir/723/seqs.fna,$sl_dir/722/seqs.fna,$sl_dir/864/seqs.fna,$sl_dir/638/seqs.fna,$sl_dir/550/seqs.fna,$sl_dir/933/seqs.fna,$sl_dir/945/seqs.fna,$sl_dir/2382/seqs.fna,$sl_dir/755/seqs.fna,$sl_dir/894/seqs.fna,$sl_dir/990/seqs.fna,$sl_dir/2192/seqs.fna,$sl_dir/2229/per_preifx_fasta/s1.fna,$sl_dir/2229/per_preifx_fasta/s2.fna,$sl_dir/2229/per_preifx_fasta/w1.fna,$sl_dir/2229/per_preifx_fasta/w2.fna,$sl_dir/2229/per_preifx_fasta/t.fna,$sl_dir/1883/per_preifx_fasta/2000.fna,$sl_dir/1883/per_preifx_fasta/2001.fna,$sl_dir/1883/per_preifx_fasta/2002.fna,$sl_dir/1883/per_preifx_fasta/2003.fna,$sl_dir/1883/per_preifx_fasta/2004.fna,$sl_dir/1883/per_preifx_fasta/2005.fna,$sl_dir/1883/per_preifx_fasta/2006.fna,$sl_dir/1883/per_preifx_fasta/2007.fna,$sl_dir/1883/per_preifx_fasta/2008.fna,$sl_dir/1883/per_preifx_fasta/2009.fna,$sl_dir/1883/per_preifx_fasta/2010.fna,$sl_dir/1883/per_preifx_fasta/2011.fna -r $gg_rep_set -o $emp_dir/EMP_OR_NEW -a -O 100 -p $param_fp -m sortmerna_sumaclust -f" | qsub -N EMP_table -l nodes=1:ppn=32 -m abe -M josenavasmolina@gmail.com -q jumbo8gb -l mem=486gb -l walltime=4752:00:00

# From study 58 to 95: torque running time 13788:22
# Extra time: 816:08:5

#echo "split_sequence_file_on_sample_ids.py -i $sl_dir/2229/seqs.fna --file_type fasta -o $sl_dir/2229/per_sample_fasta" | qsub -N ps_2229 -m abe -M josenavasmolina@gmail.com -q jumbo8gb

#echo "split_sequence_file_on_sample_ids.py -i $sl_dir/1883/seqs.fna --file_type fasta -o $sl_dir/1883/per_sample_fasta" | qsub -N ps_1883 -m abe -M josenavasmolina@gmail.com -q jumbo8gb

#mkdir $sl_dir/2229/per_preifx_fasta
#for pref in `ls $sl_dir/2229/per_sample_fasta | cut -d . -f 2 | sort | uniq`
#do
#    for f in `ls $sl_dir/2229/per_sample_fasta/2229\.${pref}\.*`
#    do
#        cat $f >> $sl_dir/2229/per_preifx_fasta/$pref.fna
#    done
#done

#mkdir $sl_dir/1883/per_preifx_fasta
#for pref in `ls $sl_dir/1883/per_sample_fasta | cut -d . -f 2 | sort | uniq`
#do
#    for f in `ls $sl_dir/1883/per_sample_fasta/1883\.${pref}\.*`
#    do
#        cat $f >> $sl_dir/1883/per_preifx_fasta/$pref.fna
#    done
#done

# Recovering the run
#echo "/bin/bash;  pick_otus.py -m sortmerna -i /scratch/Users/emhy1389/EMP//EMP_OR_NEW/100//step1_otus/POTU_SvtF_/POTU_SvtF_.5.fasta -r /scratch/Users/emhy1389/EMP//EMP_OR_NEW/99//new_refseqs.fna --sortmerna_db /scratch/Users/emhy1389/EMP//EMP_OR_NEW/100//step1_otus/POTU_SvtF_/new_refseqs -o /scratch/Users/emhy1389/EMP//EMP_OR_NEW/100//step1_otus/POTU_SvtF_/5 --sortmerna_e_value 1 -s 0.97 --threads 32 ; mv /scratch/Users/emhy1389/EMP//EMP_OR_NEW/100//step1_otus/POTU_SvtF_/5/POTU_SvtF_.5_otus.log /scratch/Users/emhy1389/EMP//EMP_OR_NEW/100//step1_otus/POTU_SvtF_.5_otus.log; mv /scratch/Users/emhy1389/EMP//EMP_OR_NEW/100//step1_otus/POTU_SvtF_/5/POTU_SvtF_.5_otus.txt /scratch/Users/emhy1389/EMP//EMP_OR_NEW/100//step1_otus/POTU_SvtF_.5_otus.txt; mv /scratch/Users/emhy1389/EMP//EMP_OR_NEW/100//step1_otus/POTU_SvtF_/5/POTU_SvtF_.5_failures.txt /scratch/Users/emhy1389/EMP//EMP_OR_NEW/100//step1_otus/POTU_SvtF_.5_failures.txt ; exit" | qsub -m abe -M josenavasmolina@gmail.com -N recov -q long8gb

# TODO: we are missing studies 2229 and 1883 (in this order) - we can divide them in chunks so SumaClust does not hang with a huge dataset...

#echo "pick_open_reference_otus.py -i $sl_dir/1001/seqs.fna,$sl_dir/1024/seqs.fna,$sl_dir/1030/seqs.fna,$sl_dir/1031/seqs.fna,$sl_dir/1033/seqs.fna,$sl_dir/1034/seqs.fna,$sl_dir/1035/seqs.fna,$sl_dir/1036/seqs.fna,$sl_dir/1037/seqs.fna,$sl_dir/1038/seqs.fna,$sl_dir/1039/seqs.fna,$sl_dir/1041/seqs.fna,$sl_dir/1043/seqs.fna,$sl_dir/1056/seqs.fna,$sl_dir/1064/seqs.fna,$sl_dir/1098/seqs.fna,$sl_dir/1197/seqs.fna,$sl_dir/1198/seqs.fna,$sl_dir/1222/seqs.fna,$sl_dir/1235/seqs.fna,$sl_dir/1240/seqs.fna,$sl_dir/1242/seqs.fna,$sl_dir/1288/seqs.fna,$sl_dir/1289/seqs.fna,$sl_dir/1453/seqs.fna,$sl_dir/1481/seqs.fna,$sl_dir/1521/seqs.fna,$sl_dir/1526/seqs.fna,$sl_dir/1578/seqs.fna,$sl_dir/1579/seqs.fna,$sl_dir/1580/seqs.fna,$sl_dir/1621/seqs.fna,$sl_dir/1622/seqs.fna,$sl_dir/1627/seqs.fna,$sl_dir/1632/seqs.fna,$sl_dir/1642/seqs.fna,$sl_dir/1665/seqs.fna,$sl_dir/1673/seqs.fna,$sl_dir/1674/seqs.fna,$sl_dir/1692/seqs.fna,$sl_dir/1694/seqs.fna,$sl_dir/1696/seqs.fna,$sl_dir/1702/seqs.fna,$sl_dir/1711/seqs.fna,$sl_dir/1713/seqs.fna,$sl_dir/1714/seqs.fna,$sl_dir/1715/seqs.fna,$sl_dir/1716/seqs.fna,$sl_dir/1717/seqs.fna,$sl_dir/1721/seqs.fna,$sl_dir/1734/seqs.fna,$sl_dir/1736/seqs.fna,$sl_dir/1740/seqs.fna,$sl_dir/1747/seqs.fna,$sl_dir/1748/seqs.fna,$sl_dir/1773/seqs.fna,$sl_dir/1774/seqs.fna,$sl_dir/1799/seqs.fna,$sl_dir/1883/seqs.fna,$sl_dir/2080/seqs.fna,$sl_dir/2182/seqs.fna,$sl_dir/2192/seqs.fna,$sl_dir/2229/seqs.fna,$sl_dir/2300/seqs.fna,$sl_dir/2338/seqs.fna,$sl_dir/2382/seqs.fna,$sl_dir/550/seqs.fna,$sl_dir/632/seqs.fna,$sl_dir/638/seqs.fna,$sl_dir/659/seqs.fna,$sl_dir/662/seqs.fna,$sl_dir/678/seqs.fna,$sl_dir/713/seqs.fna,$sl_dir/722/seqs.fna,$sl_dir/723/seqs.fna,$sl_dir/755/seqs.fna,$sl_dir/776/seqs.fna,$sl_dir/804/seqs.fna,$sl_dir/805/seqs.fna,$sl_dir/807/seqs.fna,$sl_dir/808/seqs.fna,$sl_dir/809/seqs.fna,$sl_dir/810/seqs.fna,$sl_dir/829/seqs.fna,$sl_dir/846/seqs.fna,$sl_dir/861/seqs.fna,$sl_dir/864/seqs.fna,$sl_dir/889/seqs.fna,$sl_dir/894/seqs.fna,$sl_dir/895/seqs.fna,$sl_dir/905/seqs.fna,$sl_dir/910/seqs.fna,$sl_dir/925/seqs.fna,$sl_dir/933/seqs.fna,$sl_dir/940/seqs.fna,$sl_dir/945/seqs.fna,$sl_dir/958/seqs.fna,$sl_dir/963/seqs.fna,$sl_dir/990/seqs.fna -r $gg_rep_set -o $emp_dir/EMP_OR_CONV -a -O 100 -p $param_fp -m sortmerna_sumaclust --convergent --num_seqs 100000 --min_otu_size 1" | qsub -N EMP_table_C -l nodes=1:ppn=32 -m abe -M josenavasmolina@gmail.com -q jumbo8gb -l mem=486gb -l walltime=4752:00:00

