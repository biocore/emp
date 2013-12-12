###
# Notes compiled by Greg Caporaso (gregcaporaso@gmail.com)
# Analyses run with QIIME 1.5.0-dev on compy.colorado.edu
###


## OTU picking on 30 EMP fasta files (demultiplexed using the QIIME database by Jesse Stombaugh)
echo "pick_subsampled_reference_otus_through_otu_table.py -i
/home/shared/emp-isme14/study_1031_split_library_seqs_and_mapping/study_1031_split_library_seqs.fna,/home/shared/emp-isme14/study_1033_split_library_seqs_and_mapping/study_1033_split_library_seqs.fna,/home/shared/emp-isme14/study_1034_split_library_seqs_and_mapping/study_1034_split_library_seqs.fna,/home/shared/emp-isme14/study_1035_split_library_seqs_and_mapping/study_1035_split_library_seqs.fna,/home/shared/emp-isme14/study_1036_split_library_seqs_and_mapping/study_1036_split_library_seqs.fna,/home/shared/emp-isme14/study_1037_split_library_seqs_and_mapping/study_1037_split_library_seqs.fna,/home/shared/emp-isme14/study_1038_split_library_seqs_and_mapping/study_1038_split_library_seqs.fna,/home/shared/emp-isme14/study_1039_split_library_seqs_and_mapping/study_1039_split_library_seqs.fna,/home/shared/emp-isme14/study_1043_split_library_seqs_and_mapping/study_1043_split_library_seqs.fna,/home/shared/emp-isme14/study_1197_split_library_seqs_and_mapping/study_1197_split_library_seqs.fna,/home/shared/emp-isme14/study_1198_split_library_seqs_and_mapping/study_1198_split_library_seqs.fna,/home/shared/emp-isme14/study_1222_split_library_seqs_and_mapping/study_1222_split_library_seqs.fna,/home/shared/emp-isme14/study_1240_split_library_seqs_and_mapping/study_1240_split_library_seqs.fna,/home/shared/emp-isme14/study_1242_split_library_seqs_and_mapping/study_1242_split_library_seqs.fna,/home/shared/emp-isme14/study_1288_split_library_seqs_and_mapping/study_1288_split_library_seqs.fna,/home/shared/emp-isme14/study_1289_split_library_seqs_and_mapping/study_1289_split_library_seqs.fna,/home/shared/emp-isme14/study_1453_split_library_seqs_and_mapping/study_1453_split_library_seqs.fna,/home/shared/emp-isme14/study_1526_split_library_seqs_and_mapping/study_1526_split_library_seqs.fna,/home/shared/emp-isme14/study_632_split_library_seqs_and_mapping/study_632_split_library_seqs.fna,/home/shared/emp-isme14/study_638_split_library_seqs_and_mapping/study_638_split_library_seqs.fna,/home/shared/emp-isme14/study_659_split_library_seqs_and_mapping/study_659_split_library_seqs.fna,/home/shared/emp-isme14/study_662_split_library_seqs_and_mapping/study_662_split_library_seqs.fna,/home/shared/emp-isme14/study_678_split_library_seqs_and_mapping/study_678_split_library_seqs.fna,/home/shared/emp-isme14/study_723_split_library_seqs_and_mapping/study_723_split_library_seqs.fna,/home/shared/emp-isme14/study_776_split_library_seqs_and_mapping/study_776_split_library_seqs.fna,/home/shared/emp-isme14/study_808_split_library_seqs_and_mapping/study_808_split_library_seqs.fna,/home/shared/emp-isme14/study_809_split_library_seqs_and_mapping/study_809_split_library_seqs.fna,/home/shared/emp-isme14/study_810_split_library_seqs_and_mapping/study_810_split_library_seqs.fna,/home/shared/emp-isme14/study_925_split_library_seqs_and_mapping/study_925_split_library_seqs.fna,/home/shared/emp-isme14/study_933_split_library_seqs_and_mapping/study_933_split_library_seqs.fna
-r /scratch/caporaso/gg_otus_4feb2011/rep_set/gg_97_otus_4feb2011.fasta -o
/home/shared/emp-isme14/ucrss_fast/ -aO 50 -n emp.isme14. -p
/home/shared/emp-isme14/ucrss_params.txt" | qsub -k oe -N emp-otus -q
norestrict -l nodes=1:ppn=60

## OTU picking second round of EMP data
pick_subsampled_reference_otus_through_otu_table.py -i
/home/shared/study_1235_split_library_seqs_and_mapping_updated/study_1235_split_library_seqs.fna,/home/shared/emp-isme14-additional/study_850_split_library_seqs_and_mapping/study_850_split_library_seqs.fna.gz,/home/shared/emp-isme14-additional/study_550_split_library_seqs_and_mapping/study_550_split_library_seqs.fna.gz,/home/shared/emp-isme14-additional/study_722_split_library_seqs_and_mapping/study_722_split_library_seqs.fna.gz,/home/shared/emp-isme14-additional/study_714_split_library_seqs_and_mapping/study_714_split_library_seqs.fna.gz,/home/shared/emp-isme14-additional/study_940_split_library_seqs_and_mapping/study_940_split_library_seqs.fna.gz,/home/shared/emp-isme14-additional/study_1530_split_library_seqs_and_mapping/study_1530_split_library_seqs.fna.gz,/home/shared/emp-isme14-additional/study_1030_split_library_seqs_and_mapping/study_1030_split_library_seqs.fna.gz
-r /home/shared/emp-isme14/ucrss_fast/29/new_refseqs.fna -o
/home/shared/emp-isme14/ucrss_fast_r2/ -aO 100 -n emp.isme14.r2. -p
/home/shared/emp-isme14/ucrss_params.txt --prefilter_refseqs_fp
/scratch/caporaso/gg_otus_4feb2011/rep_set/gg_97_otus_4feb2011.fasta

# Previous command died after first fasta file: I had thought that this script supported gzipped input, 
# but it doesn't. Picking up from where that one left off...

pick_subsampled_reference_otus_through_otu_table.py -i
/home/shared/emp-isme14-additional/study_550_split_library_seqs_and_mapping/study_550_split_library_seqs.fna,/home/shared/emp-isme14-additional/study_722_split_library_seqs_and_mapping/study_722_split_library_seqs.fna,/home/shared/emp-isme14-additional/study_714_split_library_seqs_and_mapping/study_714_split_library_seqs.fna,/home/shared/emp-isme14-additional/study_850_split_library_seqs_and_mapping/study_850_split_library_seqs.fna,/home/shared/emp-isme14-additional/study_940_split_library_seqs_and_mapping/study_940_split_library_seqs.fna,/home/shared/emp-isme14-additional/study_1530_split_library_seqs_and_mapping/study_1530_split_library_seqs.fna,/home/shared/emp-isme14-additional/study_1030_split_library_seqs_and_mapping/study_1030_split_library_seqs.fna
-r /home/shared/emp-isme14/ucrss_fast_r2/0/new_refseqs.fna -o
/home/shared/emp-isme14/ucrss_fast_r3/ -aO 150 -n emp.isme14.r3. -p
/home/shared/emp-isme14/ucrss_params.txt --prefilter_refseqs_fp
/scratch/caporaso/gg_otus_4feb2011/rep_set/gg_97_otus_4feb2011.fasta

## Killed previous command while processing study 850. That is by far the largest (Yatsuneko Global Gut) and I don't think it will finish in time. Adding a few remaining studies, and added 850 as the last one in this list. We'll see if it completes. 
pick_subsampled_reference_otus_through_otu_table.py -i /home/shared/emp-isme14-additional/study_940_split_library_seqs_and_mapping/study_940_split_library_seqs.fna,/home/shared/emp-isme14-additional/study_1530_split_library_seqs_and_mapping/study_1530_split_library_seqs.fna,/home/shared/emp-isme14-additional/study_1030_split_library_seqs_and_mapping/study_1030_split_library_seqs.fna,/home/shared/emp-isme14-additional/study_850_split_library_seqs_and_mapping/study_850_split_library_seqs.fna -r /home/shared/emp-isme14/ucrss_fast_r3/2/new_refseqs.fna -o /home/shared/emp-isme14/ucrss_fast_r4/ -aO 150 -n emp.isme14.r4. -p /home/shared/emp-isme14/ucrss_params.txt --prefilter_refseqs_fp /scratch/caporaso/gg_otus_4feb2011/rep_set/gg_97_otus_4feb2011.fasta


# Merge the initial round of 33 OTU tables. The code used here is in the EarthMicrobiomeProject/isme14 GitHub repo (commit ec19315e083a7f5899afb489a5f0ef0c42a2203b).

echo "parallel_merge_otu_tables.py -i /home/caporaso/analysis/isme14/per_study_otu_tables/otu_table_mc2_810.biom,/home/caporaso/analysis/isme14/per_study_otu_tables/otu_table_mc2_1033.biom,/home/caporaso/analysis/isme14/per_study_otu_tables/otu_table_mc2_1222.biom,/home/caporaso/analysis/isme14/per_study_otu_tables/otu_table_mc2_1031.biom,/home/caporaso/analysis/isme14/per_study_otu_tables/otu_table_mc2_776.biom,/home/caporaso/analysis/isme14/per_study_otu_tables/otu_table_mc2_662.biom,/home/caporaso/analysis/isme14/per_study_otu_tables/otu_table_mc2_925.biom,/home/caporaso/analysis/isme14/per_study_otu_tables/otu_table_mc2_1034.biom,/home/caporaso/analysis/isme14/per_study_otu_tables/otu_table_mc2_808.biom,/home/caporaso/analysis/isme14/per_study_otu_tables/otu_table_mc2_809.biom,/home/caporaso/analysis/isme14/per_study_otu_tables/otu_table_mc2_1038.biom,/home/caporaso/analysis/isme14/per_study_otu_tables/otu_table_mc2_632.biom,/home/caporaso/analysis/isme14/per_study_otu_tables/otu_table_mc2_714.biom,/home/caporaso/analysis/isme14/per_study_otu_tables/otu_table_mc2_1240.biom,/home/caporaso/analysis/isme14/per_study_otu_tables/otu_table_mc2_1039.biom,/home/caporaso/analysis/isme14/per_study_otu_tables/otu_table_mc2_1037.biom,/home/caporaso/analysis/isme14/per_study_otu_tables/otu_table_mc2_659.biom,/home/caporaso/analysis/isme14/per_study_otu_tables/otu_table_mc2_723.biom,/home/caporaso/analysis/isme14/per_study_otu_tables/otu_table_mc2_1035.biom,/home/caporaso/analysis/isme14/per_study_otu_tables/otu_table_mc2_638.biom,/home/caporaso/analysis/isme14/per_study_otu_tables/otu_table_mc2_1453.biom,/home/caporaso/analysis/isme14/per_study_otu_tables/otu_table_mc2_1036.biom,/home/caporaso/analysis/isme14/per_study_otu_tables/otu_table_mc2_1526.biom,/home/caporaso/analysis/isme14/per_study_otu_tables/otu_table_mc2_1043.biom,/home/caporaso/analysis/isme14/per_study_otu_tables/otu_table_mc2_1242.biom,/home/caporaso/analysis/isme14/per_study_otu_tables/otu_table_mc2_1289.biom,/home/caporaso/analysis/isme14/per_study_otu_tables/otu_table_mc2_1235.biom,/home/caporaso/analysis/isme14/per_study_otu_tables/otu_table_mc2_722.biom,/home/caporaso/analysis/isme14/per_study_otu_tables/otu_table_mc2_550.biom,/home/caporaso/analysis/isme14/per_study_otu_tables/otu_table_mc2_1288.biom,/home/caporaso/analysis/isme14/per_study_otu_tables/otu_table_mc2_678.biom,/home/caporaso/analysis/isme14/per_study_otu_tables/otu_table_mc2_1198.biom,/home/caporaso/analysis/isme14/per_study_otu_tables/otu_table_mc2_933.biom -o /home/caporaso/analysis/isme14/merged_otu_table/" | qsub -keo -N emp_merge -l pvmem=64gb -q memroute

parallel_alpha_diversity.py -i
/home/caporaso/outbox/isme14/per_study_otu_tables/ -o
/home/caporaso/outbox/isme14/per_study_alpha_diversity/ -m observed_species -O
50

# per library stats to determine even sampling depths for alpha diversity analyses
per_library_stats.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1030.biom.gz > /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1030per_lib_stats.txt
per_library_stats.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1031.biom.gz > /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1031per_lib_stats.txt
per_library_stats.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1033.biom.gz > /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1033per_lib_stats.txt
per_library_stats.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1034.biom.gz > /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1034per_lib_stats.txt
per_library_stats.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1035.biom.gz > /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1035per_lib_stats.txt
per_library_stats.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1036.biom.gz > /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1036per_lib_stats.txt
per_library_stats.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1037.biom.gz > /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1037per_lib_stats.txt
per_library_stats.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1038.biom.gz > /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1038per_lib_stats.txt
per_library_stats.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1039.biom.gz > /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1039per_lib_stats.txt
per_library_stats.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1043.biom.gz > /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1043per_lib_stats.txt
per_library_stats.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1198.biom.gz > /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1198per_lib_stats.txt
per_library_stats.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1222.biom.gz > /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1222per_lib_stats.txt
per_library_stats.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1235.biom.gz > /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1235per_lib_stats.txt
per_library_stats.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1240.biom.gz > /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1240per_lib_stats.txt
per_library_stats.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1242.biom.gz > /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1242per_lib_stats.txt
per_library_stats.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1288.biom.gz > /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1288per_lib_stats.txt
per_library_stats.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1289.biom.gz > /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1289per_lib_stats.txt
per_library_stats.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1453.biom.gz > /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1453per_lib_stats.txt
per_library_stats.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1526.biom.gz > /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1526per_lib_stats.txt
per_library_stats.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_550.biom.gz > /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_550per_lib_stats.txt
per_library_stats.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_632.biom.gz > /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_632per_lib_stats.txt
per_library_stats.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_638.biom.gz > /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_638per_lib_stats.txt
per_library_stats.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_659.biom.gz > /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_659per_lib_stats.txt
per_library_stats.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_662.biom.gz > /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_662per_lib_stats.txt
per_library_stats.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_678.biom.gz > /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_678per_lib_stats.txt
per_library_stats.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_714.biom.gz > /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_714per_lib_stats.txt
per_library_stats.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_722.biom.gz > /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_722per_lib_stats.txt
per_library_stats.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_723.biom.gz > /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_723per_lib_stats.txt
per_library_stats.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_776.biom.gz > /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_776per_lib_stats.txt
per_library_stats.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_808.biom.gz > /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_808per_lib_stats.txt
per_library_stats.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_809.biom.gz > /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_809per_lib_stats.txt
per_library_stats.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_810.biom.gz > /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_810per_lib_stats.txt
per_library_stats.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_925.biom.gz > /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_925per_lib_stats.txt
per_library_stats.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_933.biom.gz > /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_933per_lib_stats.txt
per_library_stats.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_940.biom.gz > /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_940per_lib_stats.txt

# review median sampling depths to choose a few even sampling depths (chose 2000, 5000, 10000, 100000)
egrep 'Median:' per_study_otu_tables/otu_table_mc2_*txt | cut -d " " -f 3
184428.0
161750.0
192244.0
115110.0
153603.0
205470.0
176121.5
174977.0
162163.0
241056.5
71323.5
253385.5
36670.0
443665.0
29766.0
209326.0
64390.5
112400.0
38381.5
176641.0
512909.0
199861.0
164048.5
64095.0
9374.5
172540.0
113837.0
160868.5
155115.0
222248.0
35.0
14518.0
195311.0
30445.0


# single rarefaction at four depths
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1030.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even2000/otu_table_mc2_1030.biom.gz -d 2000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1030.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even5000/otu_table_mc2_1030.biom.gz -d 5000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1030.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even10000/otu_table_mc2_1030.biom.gz -d 10000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1030.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even100000/otu_table_mc2_1030.biom.gz -d 100000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1031.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even2000/otu_table_mc2_1031.biom.gz -d 2000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1031.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even5000/otu_table_mc2_1031.biom.gz -d 5000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1031.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even10000/otu_table_mc2_1031.biom.gz -d 10000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1031.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even100000/otu_table_mc2_1031.biom.gz -d 100000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1033.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even2000/otu_table_mc2_1033.biom.gz -d 2000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1033.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even5000/otu_table_mc2_1033.biom.gz -d 5000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1033.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even10000/otu_table_mc2_1033.biom.gz -d 10000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1033.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even100000/otu_table_mc2_1033.biom.gz -d 100000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1034.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even2000/otu_table_mc2_1034.biom.gz -d 2000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1034.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even5000/otu_table_mc2_1034.biom.gz -d 5000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1034.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even10000/otu_table_mc2_1034.biom.gz -d 10000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1034.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even100000/otu_table_mc2_1034.biom.gz -d 100000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1035.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even2000/otu_table_mc2_1035.biom.gz -d 2000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1035.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even5000/otu_table_mc2_1035.biom.gz -d 5000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1035.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even10000/otu_table_mc2_1035.biom.gz -d 10000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1035.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even100000/otu_table_mc2_1035.biom.gz -d 100000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1036.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even2000/otu_table_mc2_1036.biom.gz -d 2000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1036.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even5000/otu_table_mc2_1036.biom.gz -d 5000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1036.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even10000/otu_table_mc2_1036.biom.gz -d 10000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1036.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even100000/otu_table_mc2_1036.biom.gz -d 100000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1037.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even2000/otu_table_mc2_1037.biom.gz -d 2000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1037.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even5000/otu_table_mc2_1037.biom.gz -d 5000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1037.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even10000/otu_table_mc2_1037.biom.gz -d 10000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1037.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even100000/otu_table_mc2_1037.biom.gz -d 100000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1038.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even2000/otu_table_mc2_1038.biom.gz -d 2000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1038.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even5000/otu_table_mc2_1038.biom.gz -d 5000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1038.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even10000/otu_table_mc2_1038.biom.gz -d 10000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1038.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even100000/otu_table_mc2_1038.biom.gz -d 100000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1039.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even2000/otu_table_mc2_1039.biom.gz -d 2000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1039.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even5000/otu_table_mc2_1039.biom.gz -d 5000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1039.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even10000/otu_table_mc2_1039.biom.gz -d 10000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1039.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even100000/otu_table_mc2_1039.biom.gz -d 100000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1043.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even2000/otu_table_mc2_1043.biom.gz -d 2000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1043.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even5000/otu_table_mc2_1043.biom.gz -d 5000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1043.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even10000/otu_table_mc2_1043.biom.gz -d 10000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1043.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even100000/otu_table_mc2_1043.biom.gz -d 100000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1222.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even2000/otu_table_mc2_1222.biom.gz -d 2000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1222.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even5000/otu_table_mc2_1222.biom.gz -d 5000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1222.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even10000/otu_table_mc2_1222.biom.gz -d 10000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1222.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even100000/otu_table_mc2_1222.biom.gz -d 100000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1235.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even2000/otu_table_mc2_1235.biom.gz -d 2000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1235.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even5000/otu_table_mc2_1235.biom.gz -d 5000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1235.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even10000/otu_table_mc2_1235.biom.gz -d 10000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1235.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even100000/otu_table_mc2_1235.biom.gz -d 100000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1240.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even2000/otu_table_mc2_1240.biom.gz -d 2000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1240.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even5000/otu_table_mc2_1240.biom.gz -d 5000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1240.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even10000/otu_table_mc2_1240.biom.gz -d 10000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1240.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even100000/otu_table_mc2_1240.biom.gz -d 100000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1242.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even2000/otu_table_mc2_1242.biom.gz -d 2000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1242.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even5000/otu_table_mc2_1242.biom.gz -d 5000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1242.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even10000/otu_table_mc2_1242.biom.gz -d 10000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1242.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even100000/otu_table_mc2_1242.biom.gz -d 100000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1288.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even2000/otu_table_mc2_1288.biom.gz -d 2000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1288.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even5000/otu_table_mc2_1288.biom.gz -d 5000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1288.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even10000/otu_table_mc2_1288.biom.gz -d 10000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1288.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even100000/otu_table_mc2_1288.biom.gz -d 100000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1289.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even2000/otu_table_mc2_1289.biom.gz -d 2000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1289.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even5000/otu_table_mc2_1289.biom.gz -d 5000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1289.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even10000/otu_table_mc2_1289.biom.gz -d 10000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1289.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even100000/otu_table_mc2_1289.biom.gz -d 100000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1453.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even2000/otu_table_mc2_1453.biom.gz -d 2000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1453.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even5000/otu_table_mc2_1453.biom.gz -d 5000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1453.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even10000/otu_table_mc2_1453.biom.gz -d 10000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1453.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even100000/otu_table_mc2_1453.biom.gz -d 100000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1526.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even2000/otu_table_mc2_1526.biom.gz -d 2000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1526.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even5000/otu_table_mc2_1526.biom.gz -d 5000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1526.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even10000/otu_table_mc2_1526.biom.gz -d 10000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_1526.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even100000/otu_table_mc2_1526.biom.gz -d 100000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_550.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even2000/otu_table_mc2_550.biom.gz -d 2000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_550.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even5000/otu_table_mc2_550.biom.gz -d 5000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_550.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even10000/otu_table_mc2_550.biom.gz -d 10000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_550.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even100000/otu_table_mc2_550.biom.gz -d 100000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_632.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even2000/otu_table_mc2_632.biom.gz -d 2000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_632.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even5000/otu_table_mc2_632.biom.gz -d 5000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_632.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even10000/otu_table_mc2_632.biom.gz -d 10000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_632.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even100000/otu_table_mc2_632.biom.gz -d 100000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_638.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even2000/otu_table_mc2_638.biom.gz -d 2000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_638.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even5000/otu_table_mc2_638.biom.gz -d 5000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_638.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even10000/otu_table_mc2_638.biom.gz -d 10000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_638.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even100000/otu_table_mc2_638.biom.gz -d 100000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_659.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even2000/otu_table_mc2_659.biom.gz -d 2000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_659.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even5000/otu_table_mc2_659.biom.gz -d 5000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_659.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even10000/otu_table_mc2_659.biom.gz -d 10000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_659.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even100000/otu_table_mc2_659.biom.gz -d 100000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_662.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even2000/otu_table_mc2_662.biom.gz -d 2000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_662.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even5000/otu_table_mc2_662.biom.gz -d 5000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_662.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even10000/otu_table_mc2_662.biom.gz -d 10000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_662.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even100000/otu_table_mc2_662.biom.gz -d 100000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_678.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even2000/otu_table_mc2_678.biom.gz -d 2000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_678.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even5000/otu_table_mc2_678.biom.gz -d 5000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_678.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even10000/otu_table_mc2_678.biom.gz -d 10000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_678.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even100000/otu_table_mc2_678.biom.gz -d 100000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_714.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even2000/otu_table_mc2_714.biom.gz -d 2000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_714.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even5000/otu_table_mc2_714.biom.gz -d 5000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_714.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even10000/otu_table_mc2_714.biom.gz -d 10000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_714.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even100000/otu_table_mc2_714.biom.gz -d 100000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_722.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even2000/otu_table_mc2_722.biom.gz -d 2000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_722.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even5000/otu_table_mc2_722.biom.gz -d 5000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_722.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even10000/otu_table_mc2_722.biom.gz -d 10000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_722.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even100000/otu_table_mc2_722.biom.gz -d 100000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_723.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even2000/otu_table_mc2_723.biom.gz -d 2000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_723.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even5000/otu_table_mc2_723.biom.gz -d 5000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_723.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even10000/otu_table_mc2_723.biom.gz -d 10000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_723.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even100000/otu_table_mc2_723.biom.gz -d 100000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_776.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even2000/otu_table_mc2_776.biom.gz -d 2000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_776.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even5000/otu_table_mc2_776.biom.gz -d 5000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_776.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even10000/otu_table_mc2_776.biom.gz -d 10000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_776.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even100000/otu_table_mc2_776.biom.gz -d 100000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_808.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even2000/otu_table_mc2_808.biom.gz -d 2000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_808.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even5000/otu_table_mc2_808.biom.gz -d 5000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_808.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even10000/otu_table_mc2_808.biom.gz -d 10000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_808.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even100000/otu_table_mc2_808.biom.gz -d 100000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_809.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even2000/otu_table_mc2_809.biom.gz -d 2000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_809.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even5000/otu_table_mc2_809.biom.gz -d 5000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_809.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even10000/otu_table_mc2_809.biom.gz -d 10000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_809.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even100000/otu_table_mc2_809.biom.gz -d 100000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_810.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even2000/otu_table_mc2_810.biom.gz -d 2000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_810.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even5000/otu_table_mc2_810.biom.gz -d 5000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_810.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even10000/otu_table_mc2_810.biom.gz -d 10000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_810.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even100000/otu_table_mc2_810.biom.gz -d 100000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_925.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even2000/otu_table_mc2_925.biom.gz -d 2000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_925.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even5000/otu_table_mc2_925.biom.gz -d 5000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_925.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even10000/otu_table_mc2_925.biom.gz -d 10000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_925.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even100000/otu_table_mc2_925.biom.gz -d 100000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_933.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even2000/otu_table_mc2_933.biom.gz -d 2000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_933.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even5000/otu_table_mc2_933.biom.gz -d 5000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_933.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even10000/otu_table_mc2_933.biom.gz -d 10000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_933.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even100000/otu_table_mc2_933.biom.gz -d 100000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_940.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even2000/otu_table_mc2_940.biom.gz -d 2000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_940.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even5000/otu_table_mc2_940.biom.gz -d 5000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_940.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even10000/otu_table_mc2_940.biom.gz -d 10000
single_rarefaction.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/otu_table_mc2_940.biom.gz -o /home/caporaso/outbox/isme14/per_study_otu_tables_even100000/otu_table_mc2_940.biom.gz -d 100000

# alpha diversity on full otu table and evenly sampling otu tables
parallel_alpha_diversity.py -i /home/caporaso/outbox/isme14/per_study_otu_tables/ -o /home/caporaso/outbox/isme14/per_study_alpha_diversity/ -m observed_species -O 50

parallel_alpha_diversity.py -i /home/caporaso/outbox/isme14/per_study_otu_tables_even2000/ -o /home/caporaso/outbox/isme14/per_study_alpha_diversity_even2000/ -m observed_species -O 50
parallel_alpha_diversity.py -i /home/caporaso/outbox/isme14/per_study_otu_tables_even5000/ -o /home/caporaso/outbox/isme14/per_study_alpha_diversity_even5000/ -m observed_species -O 50
parallel_alpha_diversity.py -i /home/caporaso/outbox/isme14/per_study_otu_tables_even10000/ -o /home/caporaso/outbox/isme14/per_study_alpha_diversity_even10000/ -m observed_species -O 50
parallel_alpha_diversity.py -i /home/caporaso/outbox/isme14/per_study_otu_tables_even100000/ -o /home/caporaso/outbox/isme14/per_study_alpha_diversity_even100000/ -m observed_species -O 50

parallel_align_seqs_pynast.py -i /home/caporaso/outbox/isme14/new_refseqs.fna
-o /home/caporaso/outbox/isme14/new_refseqs_pynast_aligned/ -O 200

echo "filter_alignment.py -i
/home/caporaso/outbox/isme14/new_refseqs_pynast_aligned/new_refseqs_aligned.fasta
-o /home/caporaso/outbox/isme14/new_refseqs_pynast_aligned/" | qsub -keo -N
emp_align -l pvmem=64gb -q memroute

echo "export OMP_NUM_THREADS=8; cd
/home/caporaso/outbox/isme14/new_refseqs_pynast_aligned/;
/home/mcdonald/bin/FastTreeMP -nt -gamma -fastest -no2nd -spr 4 -pseudo
new_refseqs_aligned_pfiltered.fasta > new_refseqs_aligned_pfiltered.tre" |
qsub -k oe -N emptree -l pvmem=64gb -q memroute

parallel_assign_taxonomy_rdp.py -i
/home/shared/emp-isme14/ucrss_fast_r5/new_refseqs.fna -o
/home/shared/emp-isme14/rdp_assigned_tax_c0.5/ -c 0.50 -t
/scratch/caporaso/gg_otus_4feb2011/taxonomies/greengenes_tax_rdp_train_w_genus.txt
-O 200


cd /Users/caporaso/outbox/isme14/per_study_otu_tables; add_taxa.py -i otu_table_mc2_1030.biom -o otu_table_mc2_1030_w_tax.biom -t /home/shared/emp-isme14/rdp_assigned_tax_c0.5/new_refseqs_tax_assignments.txt; gzip otu_table_mc2_1030_w_tax.biom
cd /Users/caporaso/outbox/isme14/per_study_otu_tables; add_taxa.py -i otu_table_mc2_1031.biom -o otu_table_mc2_1031_w_tax.biom -t /home/shared/emp-isme14/rdp_assigned_tax_c0.5/new_refseqs_tax_assignments.txt; gzip otu_table_mc2_1031_w_tax.biom
cd /Users/caporaso/outbox/isme14/per_study_otu_tables; add_taxa.py -i otu_table_mc2_1033.biom -o otu_table_mc2_1033_w_tax.biom -t /home/shared/emp-isme14/rdp_assigned_tax_c0.5/new_refseqs_tax_assignments.txt; gzip otu_table_mc2_1033_w_tax.biom
cd /Users/caporaso/outbox/isme14/per_study_otu_tables; add_taxa.py -i otu_table_mc2_1034.biom -o otu_table_mc2_1034_w_tax.biom -t /home/shared/emp-isme14/rdp_assigned_tax_c0.5/new_refseqs_tax_assignments.txt; gzip otu_table_mc2_1034_w_tax.biom
cd /Users/caporaso/outbox/isme14/per_study_otu_tables; add_taxa.py -i otu_table_mc2_1035.biom -o otu_table_mc2_1035_w_tax.biom -t /home/shared/emp-isme14/rdp_assigned_tax_c0.5/new_refseqs_tax_assignments.txt; gzip otu_table_mc2_1035_w_tax.biom
cd /Users/caporaso/outbox/isme14/per_study_otu_tables; add_taxa.py -i otu_table_mc2_1036.biom -o otu_table_mc2_1036_w_tax.biom -t /home/shared/emp-isme14/rdp_assigned_tax_c0.5/new_refseqs_tax_assignments.txt; gzip otu_table_mc2_1036_w_tax.biom
cd /Users/caporaso/outbox/isme14/per_study_otu_tables; add_taxa.py -i otu_table_mc2_1037.biom -o otu_table_mc2_1037_w_tax.biom -t /home/shared/emp-isme14/rdp_assigned_tax_c0.5/new_refseqs_tax_assignments.txt; gzip otu_table_mc2_1037_w_tax.biom
cd /Users/caporaso/outbox/isme14/per_study_otu_tables; add_taxa.py -i otu_table_mc2_1038.biom -o otu_table_mc2_1038_w_tax.biom -t /home/shared/emp-isme14/rdp_assigned_tax_c0.5/new_refseqs_tax_assignments.txt; gzip otu_table_mc2_1038_w_tax.biom
cd /Users/caporaso/outbox/isme14/per_study_otu_tables; add_taxa.py -i otu_table_mc2_1039.biom -o otu_table_mc2_1039_w_tax.biom -t /home/shared/emp-isme14/rdp_assigned_tax_c0.5/new_refseqs_tax_assignments.txt; gzip otu_table_mc2_1039_w_tax.biom
cd /Users/caporaso/outbox/isme14/per_study_otu_tables; add_taxa.py -i otu_table_mc2_1043.biom -o otu_table_mc2_1043_w_tax.biom -t /home/shared/emp-isme14/rdp_assigned_tax_c0.5/new_refseqs_tax_assignments.txt; gzip otu_table_mc2_1043_w_tax.biom
cd /Users/caporaso/outbox/isme14/per_study_otu_tables; add_taxa.py -i otu_table_mc2_1222.biom -o otu_table_mc2_1222_w_tax.biom -t /home/shared/emp-isme14/rdp_assigned_tax_c0.5/new_refseqs_tax_assignments.txt; gzip otu_table_mc2_1222_w_tax.biom
cd /Users/caporaso/outbox/isme14/per_study_otu_tables; add_taxa.py -i otu_table_mc2_1235.biom -o otu_table_mc2_1235_w_tax.biom -t /home/shared/emp-isme14/rdp_assigned_tax_c0.5/new_refseqs_tax_assignments.txt; gzip otu_table_mc2_1235_w_tax.biom
cd /Users/caporaso/outbox/isme14/per_study_otu_tables; add_taxa.py -i otu_table_mc2_1240.biom -o otu_table_mc2_1240_w_tax.biom -t /home/shared/emp-isme14/rdp_assigned_tax_c0.5/new_refseqs_tax_assignments.txt; gzip otu_table_mc2_1240_w_tax.biom
cd /Users/caporaso/outbox/isme14/per_study_otu_tables; add_taxa.py -i otu_table_mc2_1242.biom -o otu_table_mc2_1242_w_tax.biom -t /home/shared/emp-isme14/rdp_assigned_tax_c0.5/new_refseqs_tax_assignments.txt; gzip otu_table_mc2_1242_w_tax.biom
cd /Users/caporaso/outbox/isme14/per_study_otu_tables; add_taxa.py -i otu_table_mc2_1288.biom -o otu_table_mc2_1288_w_tax.biom -t /home/shared/emp-isme14/rdp_assigned_tax_c0.5/new_refseqs_tax_assignments.txt; gzip otu_table_mc2_1288_w_tax.biom
cd /Users/caporaso/outbox/isme14/per_study_otu_tables; add_taxa.py -i otu_table_mc2_1289.biom -o otu_table_mc2_1289_w_tax.biom -t /home/shared/emp-isme14/rdp_assigned_tax_c0.5/new_refseqs_tax_assignments.txt; gzip otu_table_mc2_1289_w_tax.biom
cd /Users/caporaso/outbox/isme14/per_study_otu_tables; add_taxa.py -i otu_table_mc2_1453.biom -o otu_table_mc2_1453_w_tax.biom -t /home/shared/emp-isme14/rdp_assigned_tax_c0.5/new_refseqs_tax_assignments.txt; gzip otu_table_mc2_1453_w_tax.biom
cd /Users/caporaso/outbox/isme14/per_study_otu_tables; add_taxa.py -i otu_table_mc2_1526.biom -o otu_table_mc2_1526_w_tax.biom -t /home/shared/emp-isme14/rdp_assigned_tax_c0.5/new_refseqs_tax_assignments.txt; gzip otu_table_mc2_1526_w_tax.biom
cd /Users/caporaso/outbox/isme14/per_study_otu_tables; add_taxa.py -i otu_table_mc2_550.biom -o otu_table_mc2_550_w_tax.biom -t /home/shared/emp-isme14/rdp_assigned_tax_c0.5/new_refseqs_tax_assignments.txt; gzip otu_table_mc2_550_w_tax.biom
cd /Users/caporaso/outbox/isme14/per_study_otu_tables; add_taxa.py -i otu_table_mc2_632.biom -o otu_table_mc2_632_w_tax.biom -t /home/shared/emp-isme14/rdp_assigned_tax_c0.5/new_refseqs_tax_assignments.txt; gzip otu_table_mc2_632_w_tax.biom
cd /Users/caporaso/outbox/isme14/per_study_otu_tables; add_taxa.py -i otu_table_mc2_638.biom -o otu_table_mc2_638_w_tax.biom -t /home/shared/emp-isme14/rdp_assigned_tax_c0.5/new_refseqs_tax_assignments.txt; gzip otu_table_mc2_638_w_tax.biom
cd /Users/caporaso/outbox/isme14/per_study_otu_tables; add_taxa.py -i otu_table_mc2_659.biom -o otu_table_mc2_659_w_tax.biom -t /home/shared/emp-isme14/rdp_assigned_tax_c0.5/new_refseqs_tax_assignments.txt; gzip otu_table_mc2_659_w_tax.biom
cd /Users/caporaso/outbox/isme14/per_study_otu_tables; add_taxa.py -i otu_table_mc2_662.biom -o otu_table_mc2_662_w_tax.biom -t /home/shared/emp-isme14/rdp_assigned_tax_c0.5/new_refseqs_tax_assignments.txt; gzip otu_table_mc2_662_w_tax.biom
cd /Users/caporaso/outbox/isme14/per_study_otu_tables; add_taxa.py -i otu_table_mc2_678.biom -o otu_table_mc2_678_w_tax.biom -t /home/shared/emp-isme14/rdp_assigned_tax_c0.5/new_refseqs_tax_assignments.txt; gzip otu_table_mc2_678_w_tax.biom
cd /Users/caporaso/outbox/isme14/per_study_otu_tables; add_taxa.py -i otu_table_mc2_714.biom -o otu_table_mc2_714_w_tax.biom -t /home/shared/emp-isme14/rdp_assigned_tax_c0.5/new_refseqs_tax_assignments.txt; gzip otu_table_mc2_714_w_tax.biom
cd /Users/caporaso/outbox/isme14/per_study_otu_tables; add_taxa.py -i otu_table_mc2_722.biom -o otu_table_mc2_722_w_tax.biom -t /home/shared/emp-isme14/rdp_assigned_tax_c0.5/new_refseqs_tax_assignments.txt; gzip otu_table_mc2_722_w_tax.biom
cd /Users/caporaso/outbox/isme14/per_study_otu_tables; add_taxa.py -i otu_table_mc2_723.biom -o otu_table_mc2_723_w_tax.biom -t /home/shared/emp-isme14/rdp_assigned_tax_c0.5/new_refseqs_tax_assignments.txt; gzip otu_table_mc2_723_w_tax.biom
cd /Users/caporaso/outbox/isme14/per_study_otu_tables; add_taxa.py -i otu_table_mc2_776.biom -o otu_table_mc2_776_w_tax.biom -t /home/shared/emp-isme14/rdp_assigned_tax_c0.5/new_refseqs_tax_assignments.txt; gzip otu_table_mc2_776_w_tax.biom
cd /Users/caporaso/outbox/isme14/per_study_otu_tables; add_taxa.py -i otu_table_mc2_808.biom -o otu_table_mc2_808_w_tax.biom -t /home/shared/emp-isme14/rdp_assigned_tax_c0.5/new_refseqs_tax_assignments.txt; gzip otu_table_mc2_808_w_tax.biom
cd /Users/caporaso/outbox/isme14/per_study_otu_tables; add_taxa.py -i otu_table_mc2_809.biom -o otu_table_mc2_809_w_tax.biom -t /home/shared/emp-isme14/rdp_assigned_tax_c0.5/new_refseqs_tax_assignments.txt; gzip otu_table_mc2_809_w_tax.biom
cd /Users/caporaso/outbox/isme14/per_study_otu_tables; add_taxa.py -i otu_table_mc2_810.biom -o otu_table_mc2_810_w_tax.biom -t /home/shared/emp-isme14/rdp_assigned_tax_c0.5/new_refseqs_tax_assignments.txt; gzip otu_table_mc2_810_w_tax.biom
cd /Users/caporaso/outbox/isme14/per_study_otu_tables; add_taxa.py -i otu_table_mc2_925.biom -o otu_table_mc2_925_w_tax.biom -t /home/shared/emp-isme14/rdp_assigned_tax_c0.5/new_refseqs_tax_assignments.txt; gzip otu_table_mc2_925_w_tax.biom
cd /Users/caporaso/outbox/isme14/per_study_otu_tables; add_taxa.py -i otu_table_mc2_933.biom -o otu_table_mc2_933_w_tax.biom -t /home/shared/emp-isme14/rdp_assigned_tax_c0.5/new_refseqs_tax_assignments.txt; gzip otu_table_mc2_933_w_tax.biom
cd /Users/caporaso/outbox/isme14/per_study_otu_tables; add_taxa.py -i otu_table_mc2_940.biom -o otu_table_mc2_940_w_tax.biom -t /home/shared/emp-isme14/rdp_assigned_tax_c0.5/new_refseqs_tax_assignments.txt; gzip otu_table_mc2_940_w_tax.biom
