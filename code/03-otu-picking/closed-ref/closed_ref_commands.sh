#!/bin/bash

#sl_dir=/home/jona1883/EMP/split_libraries/
#param_fp=/home/jona1883/EMP/open_ref_params.txt
#gg_rep_set=/home/jona1883/software/gg_otus-13_8-release/rep_set/97_otus.fasta
#emp_dir=/home/jona1883/EMP

#echo "pick_open_reference_otus.py -i $sl_dir/1001/seqs.fna,$sl_dir/1024/seqs.fna,$sl_dir/1030/seqs.fna,$sl_dir/1031/seqs.fna,$sl_dir/1033/seqs.fna,$sl_dir/1034/seqs.fna,$sl_dir/1035/seqs.fna,$sl_dir/1036/seqs.fna,$sl_dir/1037/seqs.fna,$sl_dir/1038/seqs.fna,$sl_dir/1039/seqs.fna,$sl_dir/1041/seqs.fna,$sl_dir/1043/seqs.fna,$sl_dir/1056/seqs.fna,$sl_dir/1064/seqs.fna,$sl_dir/1098/seqs.fna,$sl_dir/1197/seqs.fna,$sl_dir/1198/seqs.fna,$sl_dir/1222/seqs.fna,$sl_dir/1235/seqs.fna,$sl_dir/1240/seqs.fna,$sl_dir/1242/seqs.fna,$sl_dir/1288/seqs.fna,$sl_dir/1289/seqs.fna,$sl_dir/1453/seqs.fna,$sl_dir/1481/seqs.fna,$sl_dir/1521/seqs.fna,$sl_dir/1526/seqs.fna,$sl_dir/1578/seqs.fna,$sl_dir/1579/seqs.fna,$sl_dir/1580/seqs.fna,$sl_dir/1621/seqs.fna,$sl_dir/1622/seqs.fna,$sl_dir/1627/seqs.fna,$sl_dir/1632/seqs.fna,$sl_dir/1642/seqs.fna,$sl_dir/1665/seqs.fna,$sl_dir/1673/seqs.fna,$sl_dir/1674/seqs.fna,$sl_dir/1692/seqs.fna,$sl_dir/1694/seqs.fna,$sl_dir/1696/seqs.fna,$sl_dir/1702/seqs.fna,$sl_dir/1711/seqs.fna,$sl_dir/1713/seqs.fna,$sl_dir/1714/seqs.fna,$sl_dir/1715/seqs.fna,$sl_dir/1716/seqs.fna,$sl_dir/1717/seqs.fna,$sl_dir/1721/seqs.fna,$sl_dir/1734/seqs.fna,$sl_dir/1736/seqs.fna,$sl_dir/1740/seqs.fna,$sl_dir/1747/seqs.fna,$sl_dir/1748/seqs.fna,$sl_dir/1773/seqs.fna,$sl_dir/1774/seqs.fna,$sl_dir/1799/seqs.fna,$sl_dir/829/seqs.fna,$sl_dir/889/seqs.fna,$sl_dir/713/seqs.fna,$sl_dir/895/seqs.fna,$sl_dir/810/seqs.fna,$sl_dir/805/seqs.fna,$sl_dir/2080/seqs.fna,$sl_dir/861/seqs.fna,$sl_dir/808/seqs.fna,$sl_dir/632/seqs.fna,$sl_dir/807/seqs.fna,$sl_dir/809/seqs.fna,$sl_dir/776/seqs.fna,$sl_dir/659/seqs.fna,$sl_dir/910/seqs.fna,$sl_dir/925/seqs.fna,$sl_dir/958/seqs.fna,$sl_dir/905/seqs.fna,$sl_dir/2182/seqs.fna,$sl_dir/2300/seqs.fna,$sl_dir/662/seqs.fna,$sl_dir/940/seqs.fna,$sl_dir/846/seqs.fna,$sl_dir/963/seqs.fna,$sl_dir/804/seqs.fna,$sl_dir/2338/seqs.fna,$sl_dir/678/seqs.fna,$sl_dir/723/seqs.fna,$sl_dir/722/seqs.fna,$sl_dir/864/seqs.fna,$sl_dir/638/seqs.fna,$sl_dir/550/seqs.fna,$sl_dir/933/seqs.fna,$sl_dir/945/seqs.fna,$sl_dir/2382/seqs.fna,$sl_dir/755/seqs.fna,$sl_dir/894/seqs.fna,$sl_dir/990/seqs.fna,$sl_dir/2229/seqs.fna,$sl_dir/2192/seqs.fna,$sl_dir/1883/seqs.fna -r $gg_rep_set -o $emp_dir/EMP_OR -a -O 20 -p $param_fp -m sortmerna_sumaclust -f" | qsub -N EMP_table -l nodes=1:ppn=60 -m abe -M josenavasmolina@gmail.com -q large -l mem=486gb -l walltime=4752:00:00

#echo "merge_mapping_files.py -m $PWD/mapping_files/1001_prep_6_qiime_20141124-091848.txt,$PWD/mapping_files/1024_prep_7_qiime_20141124-091848.txt,$PWD/mapping_files/1030_prep_8_qiime_20141124-091848.txt,$PWD/mapping_files/1031_prep_9_qiime_20141124-091848.txt,$PWD/mapping_files/1033_prep_10_qiime_20141124-091848.txt,$PWD/mapping_files/1034_prep_11_qiime_20141124-091848.txt,$PWD/mapping_files/1035_prep_12_qiime_20141124-091848.txt,$PWD/mapping_files/1036_prep_13_qiime_20141124-091849.txt,$PWD/mapping_files/1037_prep_14_qiime_20141124-091849.txt,$PWD/mapping_files/1038_prep_15_qiime_20141124-091849.txt,$PWD/mapping_files/1039_prep_16_qiime_20141124-091849.txt,$PWD/mapping_files/1041_prep_17_qiime_20141124-091849.txt,$PWD/mapping_files/1043_prep_18_qiime_20141124-091849.txt,$PWD/mapping_files/1056_prep_19_qiime_20141124-091850.txt,$PWD/mapping_files/1064_prep_20_qiime_20141124-091850.txt,$PWD/mapping_files/1098_prep_21_qiime_20141124-091850.txt,$PWD/mapping_files/1197_prep_22_qiime_20141124-091850.txt,$PWD/mapping_files/1198_prep_23_qiime_20141124-091850.txt,$PWD/mapping_files/1222_prep_24_qiime_20141124-091850.txt,$PWD/mapping_files/1235_prep_25_qiime_20141124-091850.txt,$PWD/mapping_files/1240_prep_26_qiime_20141124-091851.txt,$PWD/mapping_files/1242_prep_27_qiime_20141124-091851.txt,$PWD/mapping_files/1288_prep_28_qiime_20141124-091851.txt,$PWD/mapping_files/1289_prep_29_qiime_20141124-091851.txt,$PWD/mapping_files/1453_prep_30_qiime_20141124-091851.txt,$PWD/mapping_files/1481_prep_31_qiime_20141124-091851.txt,$PWD/mapping_files/1521_prep_32_qiime_20141124-091852.txt,$PWD/mapping_files/1526_prep_33_qiime_20141124-091852.txt,$PWD/mapping_files/1578_prep_34_qiime_20141124-091852.txt,$PWD/mapping_files/1579_prep_35_qiime_20141124-091852.txt,$PWD/mapping_files/1580_prep_36_qiime_20141124-091852.txt,$PWD/mapping_files/1621_prep_37_qiime_20141124-091852.txt,$PWD/mapping_files/1622_prep_38_qiime_20141124-091852.txt,$PWD/mapping_files/1627_prep_39_qiime_20141124-091853.txt,$PWD/mapping_files/1632_prep_40_qiime_20141124-091853.txt,$PWD/mapping_files/1642_prep_41_qiime_20141124-091853.txt,$PWD/mapping_files/1665_prep_42_qiime_20141124-091853.txt,$PWD/mapping_files/1673_prep_43_qiime_20141124-091853.txt,$PWD/mapping_files/1674_prep_44_qiime_20141124-091853.txt,$PWD/mapping_files/1692_prep_45_qiime_20141124-091853.txt,$PWD/mapping_files/1694_prep_46_qiime_20141124-091854.txt,$PWD/mapping_files/1696_prep_47_qiime_20141124-091854.txt,$PWD/mapping_files/1702_prep_48_qiime_20141124-091854.txt,$PWD/mapping_files/1711_prep_49_qiime_20141124-091854.txt,$PWD/mapping_files/1713_prep_50_qiime_20141124-091854.txt,$PWD/mapping_files/1714_prep_51_qiime_20141124-091854.txt,$PWD/mapping_files/1715_prep_52_qiime_20141124-091854.txt,$PWD/mapping_files/1716_prep_53_qiime_20141124-091854.txt,$PWD/mapping_files/1717_prep_54_qiime_20141124-091855.txt,$PWD/mapping_files/1721_prep_55_qiime_20141124-091855.txt,$PWD/mapping_files/1734_prep_56_qiime_20141124-091855.txt,$PWD/mapping_files/1736_prep_57_qiime_20141124-091855.txt,$PWD/mapping_files/1740_prep_58_qiime_20141124-091855.txt,$PWD/mapping_files/1747_prep_59_qiime_20141124-091855.txt,$PWD/mapping_files/1748_prep_60_qiime_20141124-091855.txt,$PWD/mapping_files/1773_prep_61_qiime_20141124-091856.txt,$PWD/mapping_files/1774_prep_62_qiime_20141124-091856.txt,$PWD/mapping_files/1799_prep_63_qiime_20141124-091856.txt,$PWD/mapping_files/1883_prep_64_qiime_20141124-091856.txt,$PWD/mapping_files/2080_prep_65_qiime_20141124-091857.txt,$PWD/mapping_files/2182_prep_66_qiime_20141124-091857.txt,$PWD/mapping_files/2192_prep_67_qiime_20141124-091857.txt,$PWD/mapping_files/2229_prep_68_qiime_20141124-091857.txt,$PWD/mapping_files/2300_prep_69_qiime_20141124-091857.txt,$PWD/mapping_files/2338_prep_70_qiime_20141124-091858.txt,$PWD/mapping_files/2382_prep_71_qiime_20141124-091858.txt,$PWD/mapping_files/550_prep_72_qiime_20141124-091858.txt,$PWD/mapping_files/632_prep_73_qiime_20141124-091858.txt,$PWD/mapping_files/638_prep_74_qiime_20141124-091858.txt,$PWD/mapping_files/659_prep_75_qiime_20141124-091859.txt,$PWD/mapping_files/662_prep_76_qiime_20141124-091859.txt,$PWD/mapping_files/678_prep_77_qiime_20141124-091859.txt,$PWD/mapping_files/713_prep_78_qiime_20141124-091859.txt,$PWD/mapping_files/722_prep_79_qiime_20141124-091859.txt,$PWD/mapping_files/723_prep_80_qiime_20141124-091859.txt,$PWD/mapping_files/755_prep_81_qiime_20141124-091859.txt,$PWD/mapping_files/776_prep_82_qiime_20141124-091900.txt,$PWD/mapping_files/804_prep_83_qiime_20141124-091900.txt,$PWD/mapping_files/805_prep_84_qiime_20141124-091900.txt,$PWD/mapping_files/807_prep_85_qiime_20141124-091900.txt,$PWD/mapping_files/808_prep_86_qiime_20141124-091900.txt,$PWD/mapping_files/809_prep_87_qiime_20141124-091900.txt,$PWD/mapping_files/810_prep_88_qiime_20141124-091900.txt,$PWD/mapping_files/829_prep_89_qiime_20141124-091900.txt,$PWD/mapping_files/846_prep_90_qiime_20141124-091900.txt,$PWD/mapping_files/861_prep_91_qiime_20141124-091901.txt,$PWD/mapping_files/864_prep_92_qiime_20141124-091901.txt,$PWD/mapping_files/889_prep_93_qiime_20141124-091901.txt,$PWD/mapping_files/894_prep_94_qiime_20141124-091901.txt,$PWD/mapping_files/895_prep_95_qiime_20141124-091901.txt,$PWD/mapping_files/905_prep_96_qiime_20141124-091901.txt,$PWD/mapping_files/910_prep_97_qiime_20141124-091902.txt,$PWD/mapping_files/925_prep_98_qiime_20141124-091849.txt,$PWD/mapping_files/933_prep_99_qiime_20141124-091849.txt,$PWD/mapping_files/940_prep_100_qiime_20141124-091902.txt,$PWD/mapping_files/945_prep_101_qiime_20141124-091902.txt,$PWD/mapping_files/958_prep_102_qiime_20141124-091902.txt,$PWD/mapping_files/963_prep_103_qiime_20141124-091902.txt,$PWD/mapping_files/990_prep_104_qiime_20141124-091902.txt -o $PWD/emp_mapping_file.txt -n unknown" | qsub -N EMPmm -m abe -M josenavasmolina@gmail.com -q short8gb


####### OTU PICKING CLOSED REFERENCE USING SILVA DATABASE
#echo "indexdb_rna --ref $HOME/software/Silva119_release/rep_set/97/Silva_119_rep_set97.fna,$HOME/software/Silva119_release/rep_set/SortMeRNA/silva_97.idx --max_pos 10000" | qsub -N SilvaIndexDB -m abe -M josenavasmolina@gmail.com -l pmem=8gb -l walltime=01:30:00 -m abe -M josenavasmolina@gmail.com



###### Get the % of sequences clustered in closed-ref ######
#for d in `ls -d EMP_CR_NEW/[0-9]* | cut -d "/" -f 2`
#do
#    echo "get_seq_counts.py -d $PWD/split_libraries/$d/seqs.fna -b $PWD/EMP_CR_NEW/$d/otu_table.biom -o $PWD/per_sample_perc_cr/$d.txt"
#done

###### Fixing sequence IDS ####

#for d in `ls /projects/emp/01-split-libraries`
#do
    # Rename the incorrect sequences to OLD
    #mv /projects/emp/01-split-libraries/$d/seqs.fna /projects/emp/01-split-libraries/$d/old_seqs.fna
    # Fix the sequence labels
    #echo "source activate emp-rename; cp /projects/emp/01-split-libraries/$d/old_seqs.fna /localscratch/${d}_seqs.fna; /home/jona1883/software/bin/rename_fasta.py /localscratch/${d}_seqs.fna /projects/emp/qiime-maps/${d}_qiime_mapping.tsv; cp /localscratch/new_${d}_seqs.fna /projects/emp/01-split-libraries/$d/seqs.fna" | qsub -N RN_$d  -m abe -M josenavasmolina@gmail.com -l walltime=6:00:00
    #sleep 0.5
#done

# Some of the above jobs failed, so re-run them specifying some memory
#   1030 -> 2GB
#echo "source activate emp-rename; cp /projects/emp/01-split-libraries/1030/old_seqs.fna /localscratch/1030_seqs.fna; /home/jona1883/software/bin/rename_fasta.py /localscratch/1030_seqs.fna /projects/emp/qiime-maps/1030_qiime_mapping.tsv; cp /localscratch/new_1030_seqs.fna /projects/emp/01-split-libraries/1030/seqs.fna" | qsub -N RN_1030 -m abe -M josenavasmolina@gmail.com -l walltime=3:00:00 -l pmem=2GB
#sleep 0.5
#   1774 -> 6GB
#echo "source activate emp-rename; cp /projects/emp/01-split-libraries/1774/old_seqs.fna /localscratch/1774_seqs.fna; /home/jona1883/software/bin/rename_fasta.py /localscratch/1774_seqs.fna /projects/emp/qiime-maps/1774_qiime_mapping.tsv; cp /localscratch/new_1774_seqs.fna /projects/emp/01-split-libraries/1774/seqs.fna" | qsub -N RN_1774 -m abe -M josenavasmolina@gmail.com -l walltime=3:00:00 -l pmem=6GB
#sleep 0.5
##   864  -> 4GB
#echo "source activate emp-rename; cp /projects/emp/01-split-libraries/864/old_seqs.fna /localscratch/864_seqs.fna; /home/jona1883/software/bin/rename_fasta.py /localscratch/864_seqs.fna /projects/emp/qiime-maps/864_qiime_mapping.tsv; cp /localscratch/new_864_seqs.fna /projects/emp/01-split-libraries/864/seqs.fna" | qsub -N RN_864 -m abe -M josenavasmolina@gmail.com -l walltime=3:00:00 -l pmem=4GB
#sleep 0.5
##   1748 -> 4GB
#echo "source activate emp-rename; cp /projects/emp/01-split-libraries/1748/old_seqs.fna /localscratch/1748_seqs.fna; /home/jona1883/software/bin/rename_fasta.py /localscratch/1748_seqs.fna /projects/emp/qiime-maps/1748_qiime_mapping.tsv; cp /localscratch/new_1748_seqs.fna /projects/emp/01-split-libraries/1748/seqs.fna" | qsub -N RN_1748 -m abe -M josenavasmolina@gmail.com -l walltime=3:00:00 -l pmem=4GB
#sleep 0.5
##   678  -> 4GB
#echo "source activate emp-rename; cp /projects/emp/01-split-libraries/678/old_seqs.fna /localscratch/678_seqs.fna; /home/jona1883/software/bin/rename_fasta.py /localscratch/678_seqs.fna /projects/emp/qiime-maps/678_qiime_mapping.tsv; cp /localscratch/new_678_seqs.fna /projects/emp/01-split-libraries/678/seqs.fna" | qsub -N RN_678 -m abe -M josenavasmolina@gmail.com -l walltime=3:00:00 -l pmem=4GB
#sleep 0.5
##   1721 -> 4GB
#echo "source activate emp-rename; cp /projects/emp/01-split-libraries/1721/old_seqs.fna /localscratch/1721_seqs.fna; /home/jona1883/software/bin/rename_fasta.py /localscratch/1721_seqs.fna /projects/emp/qiime-maps/1721_qiime_mapping.tsv; cp /localscratch/new_1721_seqs.fna /projects/emp/01-split-libraries/1721/seqs.fna" | qsub -N RN_1721 -m abe -M josenavasmolina@gmail.com -l walltime=3:00:00 -l pmem=4GB
#sleep 0.5
##   1622 -> 4GB
#echo "source activate emp-rename; cp /projects/emp/01-split-libraries/1622/old_seqs.fna /localscratch/1622_seqs.fna; /home/jona1883/software/bin/rename_fasta.py /localscratch/1622_seqs.fna /projects/emp/qiime-maps/1622_qiime_mapping.tsv; cp /localscratch/new_1622_seqs.fna /projects/emp/01-split-libraries/1622/seqs.fna" | qsub -N RN_1622 -m abe -M josenavasmolina@gmail.com -l walltime=3:00:00 -l pmem=4GB
#sleep 0.5
##   550  -> 16GB
#echo "source activate emp-rename; cp /projects/emp/01-split-libraries/550/old_seqs.fna /localscratch/550_seqs.fna; /home/jona1883/software/bin/rename_fasta.py /localscratch/550_seqs.fna /projects/emp/qiime-maps/550_qiime_mapping.tsv; cp /localscratch/new_550_seqs.fna /projects/emp/01-split-libraries/550/seqs.fna" | qsub -N RN_550 -m abe -M josenavasmolina@gmail.com -l walltime=3:00:00 -l pmem=16GB
#sleep 0.5
##   933  -> 4GB
#echo "source activate emp-rename; cp /projects/emp/01-split-libraries/933/old_seqs.fna /localscratch/933_seqs.fna; /home/jona1883/software/bin/rename_fasta.py /localscratch/933_seqs.fna /projects/emp/qiime-maps/933_qiime_mapping.tsv; cp /localscratch/new_933_seqs.fna /projects/emp/01-split-libraries/933/seqs.fna" | qsub -N RN_933 -m abe -M josenavasmolina@gmail.com -l walltime=3:00:00 -l pmem=4GB
#sleep 0.5
##   1736 -> 6GB
#echo "source activate emp-rename; cp /projects/emp/01-split-libraries/1736/old_seqs.fna /localscratch/1736_seqs.fna; /home/jona1883/software/bin/rename_fasta.py /localscratch/1736_seqs.fna /projects/emp/qiime-maps/1736_qiime_mapping.tsv; cp /localscratch/new_1736_seqs.fna /projects/emp/01-split-libraries/1736/seqs.fna" | qsub -N RN_1736 -m abe -M josenavasmolina@gmail.com -l walltime=3:00:00 -l pmem=6GB
#sleep 0.5
##   1694 -> 6GB
#echo "source activate emp-rename; cp /projects/emp/01-split-libraries/1694/old_seqs.fna /localscratch/1694_seqs.fna; /home/jona1883/software/bin/rename_fasta.py /localscratch/1694_seqs.fna /projects/emp/qiime-maps/1694_qiime_mapping.tsv; cp /localscratch/new_1694_seqs.fna /projects/emp/01-split-libraries/1694/seqs.fna" | qsub -N RN_1694 -m abe -M josenavasmolina@gmail.com -l walltime=3:00:00 -l pmem=6GB
#sleep 0.5
##   945  -> 12GB
#echo "source activate emp-rename; cp /projects/emp/01-split-libraries/945/old_seqs.fna /localscratch/945_seqs.fna; /home/jona1883/software/bin/rename_fasta.py /localscratch/945_seqs.fna /projects/emp/qiime-maps/945_qiime_mapping.tsv; cp /localscratch/new_945_seqs.fna /projects/emp/01-split-libraries/945/seqs.fna" | qsub -N RN_945 -m abe -M josenavasmolina@gmail.com -l walltime=3:00:00 -l pmem=12GB
#sleep 0.5
##   2192 -> 12GB
#echo "source activate emp-rename; cp /projects/emp/01-split-libraries/2192/old_seqs.fna /localscratch/2192_seqs.fna; /home/jona1883/software/bin/rename_fasta.py /localscratch/2192_seqs.fna /projects/emp/qiime-maps/2192_qiime_mapping.tsv; cp /localscratch/new_2192_seqs.fna /projects/emp/01-split-libraries/2192/seqs.fna" | qsub -N RN_2192 -m abe -M josenavasmolina@gmail.com -l walltime=3:00:00 -l pmem=12GB
#sleep 0.5
##   2229 -> 12GB
#echo "source activate emp-rename; cp /projects/emp/01-split-libraries/2229/old_seqs.fna /localscratch/2229_seqs.fna; /home/jona1883/software/bin/rename_fasta.py /localscratch/2229_seqs.fna /projects/emp/qiime-maps/2229_qiime_mapping.tsv; cp /localscratch/new_2229_seqs.fna /projects/emp/01-split-libraries/2229/seqs.fna" | qsub -N RN_2229 -m abe -M josenavasmolina@gmail.com -l walltime=3:00:00 -l pmem=12GB
#sleep 0.5
##   722  -> 4GB
#echo "source activate emp-rename; cp /projects/emp/01-split-libraries/722/old_seqs.fna /localscratch/722_seqs.fna; /home/jona1883/software/bin/rename_fasta.py /localscratch/722_seqs.fna /projects/emp/qiime-maps/722_qiime_mapping.tsv; cp /localscratch/new_722_seqs.fna /projects/emp/01-split-libraries/722/seqs.fna" | qsub -N RN_722 -m abe -M josenavasmolina@gmail.com -l walltime=3:00:00 -l pmem=4GB
#sleep 0.5
##   990  -> 8GB
#echo "source activate emp-rename; cp /projects/emp/01-split-libraries/990/old_seqs.fna /localscratch/990_seqs.fna; /home/jona1883/software/bin/rename_fasta.py /localscratch/990_seqs.fna /projects/emp/qiime-maps/990_qiime_mapping.tsv; cp /localscratch/new_990_seqs.fna /projects/emp/01-split-libraries/990/seqs.fna" | qsub -N RN_990 -m abe -M josenavasmolina@gmail.com -l walltime=3:00:00 -l pmem=8GB
#sleep 0.5
##   2382 -> 6GB
#echo "source activate emp-rename; cp /projects/emp/01-split-libraries/2382/old_seqs.fna /localscratch/2382_seqs.fna; /home/jona1883/software/bin/rename_fasta.py /localscratch/2382_seqs.fna /projects/emp/qiime-maps/2382_qiime_mapping.tsv; cp /localscratch/new_2382_seqs.fna /projects/emp/01-split-libraries/2382/seqs.fna" | qsub -N RN_2382 -m abe -M josenavasmolina@gmail.com -l walltime=3:00:00 -l pmem=6GB
#sleep 0.5
##   1642 -> 6GB
#echo "source activate emp-rename; cp /projects/emp/01-split-libraries/1642/old_seqs.fna /localscratch/1642_seqs.fna; /home/jona1883/software/bin/rename_fasta.py /localscratch/1642_seqs.fna /projects/emp/qiime-maps/1642_qiime_mapping.tsv; cp /localscratch/new_1642_seqs.fna /projects/emp/01-split-libraries/1642/seqs.fna" | qsub -N RN_1642 -m abe -M josenavasmolina@gmail.com -l walltime=3:00:00 -l pmem=6GB
#sleep 0.5
##   894  -> 18GB
#echo "source activate emp-rename; cp /projects/emp/01-split-libraries/894/old_seqs.fna /localscratch/894_seqs.fna; /home/jona1883/software/bin/rename_fasta.py /localscratch/894_seqs.fna /projects/emp/qiime-maps/894_qiime_mapping.tsv; cp /localscratch/new_894_seqs.fna /projects/emp/01-split-libraries/894/seqs.fna" | qsub -N RN_894 -m abe -M josenavasmolina@gmail.com -l walltime=3:00:00 -l pmem=18GB
#sleep 0.5
##   1288 -> 12GB
#echo "source activate emp-rename; cp /projects/emp/01-split-libraries/1288/old_seqs.fna /localscratch/1288_seqs.fna; /home/jona1883/software/bin/rename_fasta.py /localscratch/1288_seqs.fna /projects/emp/qiime-maps/1288_qiime_mapping.tsv; cp /localscratch/new_1288_seqs.fna /projects/emp/01-split-libraries/1288/seqs.fna" | qsub -N RN_1288 -m abe -M josenavasmolina@gmail.com -l walltime=3:00:00 -l pmem=12GB
#sleep 0.5
##   755  -> 10GB
#echo "source activate emp-rename; cp /projects/emp/01-split-libraries/755/old_seqs.fna /localscratch/755_seqs.fna; /home/jona1883/software/bin/rename_fasta.py /localscratch/755_seqs.fna /projects/emp/qiime-maps/755_qiime_mapping.tsv; cp /localscratch/new_755_seqs.fna /projects/emp/01-split-libraries/755/seqs.fna" | qsub -N RN_755 -m abe -M josenavasmolina@gmail.com -l walltime=3:00:00 -l pmem=10GB
#sleep 0.5
##   1235 -> 4GB
#echo "source activate emp-rename; cp /projects/emp/01-split-libraries/1235/old_seqs.fna /localscratch/1235_seqs.fna; /home/jona1883/software/bin/rename_fasta.py /localscratch/1235_seqs.fna /projects/emp/qiime-maps/1235_qiime_mapping.tsv; cp /localscratch/new_1235_seqs.fna /projects/emp/01-split-libraries/1235/seqs.fna" | qsub -N RN_1235 -m abe -M josenavasmolina@gmail.com -l walltime=3:00:00 -l pmem=4GB
#sleep 0.5
##   1632 -> 6GB
#echo "source activate emp-rename; cp /projects/emp/01-split-libraries/1632/old_seqs.fna /localscratch/1632_seqs.fna; /home/jona1883/software/bin/rename_fasta.py /localscratch/1632_seqs.fna /projects/emp/qiime-maps/1632_qiime_mapping.tsv; cp /localscratch/new_1632_seqs.fna /projects/emp/01-split-libraries/1632/seqs.fna" | qsub -N RN_1632 -m abe -M josenavasmolina@gmail.com -l walltime=3:00:00 -l pmem=6GB
#sleep 0.5
##   1521 -> 6GB
#echo "source activate emp-rename; cp /projects/emp/01-split-libraries/1521/old_seqs.fna /localscratch/1521_seqs.fna; /home/jona1883/software/bin/rename_fasta.py /localscratch/1521_seqs.fna /projects/emp/qiime-maps/1521_qiime_mapping.tsv; cp /localscratch/new_1521_seqs.fna /projects/emp/01-split-libraries/1521/seqs.fna" | qsub -N RN_1521 -m abe -M josenavasmolina@gmail.com -l walltime=3:00:00 -l pmem=6GB
#sleep 0.5
#   1883 -> 16GB
#echo "source activate emp-rename; cp /projects/emp/01-split-libraries/1883/old_seqs.fna /localscratch/1883_seqs.fna; /home/jona1883/software/bin/rename_fasta.py /localscratch/1883_seqs.fna /projects/emp/qiime-maps/1883_qiime_mapping.tsv; cp /localscratch/new_1883_seqs.fna /projects/emp/01-split-libraries/1883/seqs.fna" | qsub -N RN_1883 -m abe -M josenavasmolina@gmail.com -l walltime=6:00:00 -l pmem=80GB
#   905
#echo "source activate emp-rename; cp /projects/emp/01-split-libraries/905/old_seqs.fna /localscratch/905_seqs.fna; /home/jona1883/software/bin/rename_fasta.py /localscratch/905_seqs.fna /projects/emp/qiime-maps/905_qiime_mapping.tsv; cp /localscratch/new_905_seqs.fna /projects/emp/01-split-libraries/905/seqs.fna" | qsub -N RN_905 -m abe -M josenavasmolina@gmail.com -l walltime=3:00:00 -l pmem=8gb
#echo "source activate emp-rename; cp /projects/emp/01-split-libraries/1453/old_seqs.fna /localscratch/1453_seqs.fna; /home/jona1883/software/bin/rename_fasta.py /localscratch/1453_seqs.fna /projects/emp/qiime-maps/1453_qiime_mapping.tsv; cp /localscratch/new_1453_seqs.fna /projects/emp/01-split-libraries/1453/seqs.fna" | qsub -N RN_1453 -m abe -M josenavasmolina@gmail.com -l walltime=3:00:00 -l pmem=8gb


#for d in `ls /projects/emp/02-adaptor-clean-up/`
#do
#    #mv /projects/emp/02-adaptor-clean-up/$d/filtered_seqs.fna /projects/emp/02-adaptor-clean-up/$d/old_filtered_seqs.fna
#    #mv /projects/emp/02-adaptor-clean-up/$d/seqs_to_filter.fna /projects/emp/02-adaptor-clean-up/$d/old_seqs_to_filter.fna
#    sleep 0.5
#done

#for d in `ls /projects/emp/03-otus/01-closed-ref/`
#do
    # Fix the sample ids
#    echo "source activate emp-rename; /home/jona1883/software/bin/rename_biom.py /projects/emp/03-otus/01-closed-ref/$d/otu_table.biom /projects/emp/qiime-maps/${d}_qiime_mapping.tsv" | qsub -N RNOTU_$d  -m abe -M josenavasmolina@gmail.com -l walltime=1:00:00
#    sleep 0.5
#done

#echo "source activate emp-rename; /home/jona1883/software/bin/rename_biom.py /projects/emp/03-otus/01-closed-ref/merged/merged.biom /projects/emp/merged_qiime_mapping.tsv" | qsub -N RNOTU_$d  -m abe -M josenavasmolina@gmail.com -l walltime=1:00:00

#echo "source activate emp-rename; /home/jona1883/software/bin/rename_biom.py /home/jona1883/EMP/ANALYSES/open_ref/emp_or_no_1740.biom /projects/emp/merged_qiime_mapping.tsv" | qsub -N RNOTU_$d  -m abe -M josenavasmolina@gmail.com -l walltime=1:00:00

