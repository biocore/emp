

```python
import pandas as pd
import os.path
```


```python
path_root = '/media/barnacle/projects/emp/'
resultsFile = '/home/sjanssen/Desktop/observations.tsv'
masterMappingFile = path_root + '/00-qiime-maps/merged/emp_qiime_mapping_refined_20160627.tsv'

bioms = {
    'gg'       : {'label': 'cr_gg_seqs',
                  'biomsummary': path_root + '03-otus/01-closed-ref-greengenes/emp_cr_gg_13_8.summary.txt',
                  'biomfile':    path_root + '03-otus/01-closed-ref-greengenes/emp_cr_gg_13_8.biom'},
    'silva'    : {'label': 'cr_silva_seqs',
                  'biomsummary': path_root + '03-otus/01-closed-ref-silva-16S/emp_cr_silva_16S.summary.txt',
                  'biomfile':    path_root + '03-otus/01-closed-ref-silva-16S/emp_cr_silva_16S.biom'},                
    'openref'  : {'label': 'or_gg_seqs',
                  'biomsummary': path_root + '03-otus/02-open-ref-greengenes/emp_or.summary.txt',
                  'biomfile':    path_root + '03-otus/02-open-ref-greengenes/emp_or.biom'},                  
    'deblur100': {'label': 'deblur_100nt_seqs',
                  'biomsummary': path_root + '03-otus/04-deblur/emp.100.min25.deblur.withtax.summary.txt',
                  'biomfile':    path_root + '03-otus/04-deblur/emp.100.min25.deblur.withtax.biom'},                  
    'deblur150': {'label': 'deblur_150nt_seqs',
                  'biomsummary': path_root + '03-otus/04-deblur/emp.150.min25.deblur.withtax.summary.txt',
                  'biomfile':    path_root + '03-otus/04-deblur/emp.150.min25.deblur.withtax.biom'},
}
fasta = {
    'split-libraries' : {'label': 'split-libraries',
                         'dir': path_root + '01-split-libraries',  
                         'fnaFile': 'seqs.fna',          
                         'logfile': 'split_library_log.txt'},
    'adaptor-clean-up': {'label': 'adaptor-clean-up',
                         'dir': path_root + '02-adaptor-clean-up', 
                         'fnaFile': 'filtered_seqs.fna', 
                         'filterFnaFile': 'seqs_to_filter.fna',
                         'logfile': ''},
}
```


```python
# Gathering all necessary information from the original files themselves is not feasible, because of IO and CPU time.
# The following method makes use of additional information that describe the BIOM tables and fasta files.
# This is fine, as long as those descriptors are up to date. Otherwise, we are screwed!
# These asumptions must hold for proper operations of this script:
#     1. each BIOM file is acompanied by a *.summary.txt file which holds the number of counts per sample starting at line 15
#     2. each seq.fasta file has its split_library_log.txt which give counts of sequences for the same sample. It can have several runs and counts might be split acros those runs.
#     3. to avoid looking into the filered_seqs.fna files we substract the number of sequences to be filtered from the number of sequences per sample of the previous computation. Thus, it is neccessary that we have up-to-date 'seqs_to_filter.fna' files.

############ STEP 1/4 ###########
print("Step 1/4: parsing summary information about BIOM " + str(len(bioms)) + " tables: ", end="")
o = {}
for name in bioms:
    print(".", end="")
    o[name] = pd.read_csv(bioms[name]['biomsummary'], sep=":", skiprows=15, index_col=0, names=["sampleID",bioms[name]['label']])
    o[name].index = o[name].index.map(str.upper) # use upper case 
observations = pd.concat([ o[name] for name in o], axis=1, join='outer')
print(" done.")


############ STEP 2/4 ###########
field = 'split-libraries'
logs = []
path = fasta[field]['dir']
filename= fasta[field]['logfile']
logfiles = !find "$path" -name "$filename"
tmpfile = "/tmp/sampleIDs"
print("Step 2/4: parsing " + str(len(logfiles)) + " '" + filename + "' files: ", end="")
for logfile in logfiles:
    print(".", end="")
    studyID = logfile.split("/")[-2]
    #a logfile can contain several entries, thus it is necessary to grep only the sampleID lines in a pre-processing step
    !grep "^$studyID" "$logfile" > "$tmpfile"
    log = pd.read_csv(tmpfile, sep="\t", index_col=0, names=['sampleID', fasta[field]['label']])
    log.index = log.index.map(str.upper) # use upper case 
    log = log.reset_index().groupby(log.index).sum() #counts might be spread over several runs, thus we need to sum them here
    logs.append(log)
logs = pd.concat(logs, axis=0)
observations = observations.merge(logs, left_index=True, right_index=True, how="outer")
print(" done.")


############ STEP 3/4 ###########
if fasta['split-libraries']['label'] in observations:
    field = 'adaptor-clean-up'
    path = fasta[field]['dir']
    filename = fasta[field]['filterFnaFile']
    tmpfile = "/tmp/sampleIDs"
    filenames_filterSeqs = !find "$path" -name "$filename"
    pdsFiltered = []
    print("Step 3/4: parsing " + str(len(filenames_filterSeqs)) + " '" + filename + "' files: ", end="")
    for file in filenames_filterSeqs:
        print(".", end="")
        studyID = logfile.split("/")[-2]
        !grep "^>" "$file" | cut -d "_" -f 1 | sort | tr -d ">" | uniq -c | sed "s/^[ \t]*//" > "$tmpfile" 
        nrs = pd.read_csv(tmpfile, sep=" ", index_col=1, names=[fasta[field]['label'] + "-remove", 'sampleID'])
        nrs.index = nrs.index.map(str.upper) # use upper case 
        pdsFiltered.append( nrs )

    pdsFiltered = pd.concat(pdsFiltered, axis=0)

    #use the counted numbers of sequences that have been filtered to compute the number of remaining sequences
    x = observations.merge(pdsFiltered, left_index=True, right_index=True, how="outer")
    x.fillna(0, inplace=True)
    observations[fasta['adaptor-clean-up']['label']] = observations[fasta['split-libraries']['label']] - x[fasta['adaptor-clean-up']['label']+"-remove"]
    print(" done.")
else:
    print("Field '" + fasta['split-libraries']['label'] + "' is missing in the observations table. First compute this field, before computing the number of filtered sequences!")
    

############ STEP 4/4 ###########
print("Step 4/4: add sample names identical to master mapping file '" + str(masterMappingFile) + "': ", end="")
metadata = pd.read_csv(masterMappingFile, sep="\t", usecols=[0])
metadata['UC'] = metadata['#SampleID'].map(str.upper) # use upper case
metadata.set_index("UC", inplace=True)
observations = observations.merge(metadata, left_index=True, right_index=True, how="inner")
observations.set_index('#SampleID', inplace=True)
print(" done.")


#store results in one file
print("\nResults have been written to '" + resultsFile + "'.")
observations.to_csv(resultsFile, sep="\t")
```

    Step 1/4: parsing summary information about BIOM 5 tables: ..... done.
    Step 2/4: parsing 97 'split_library_log.txt' files: ................................................................................................. done.
    Step 3/4: parsing 97 'seqs_to_filter.fna' files: ................................................................................................. done.
    Step 4/4: add sample names identical to master mapping file '/media/barnacle/projects/emp//00-qiime-maps/merged/emp_qiime_mapping_refined_20160627.tsv':  done.
    
    Results have been written to '/home/sjanssen/Desktop/observations.tsv'.



```python
#the slow method: go through the content of the fasta files and aggregate the header lines. Takes a few hours, even on barnacle!
print("Execute the following command on 'barnacle' and transfer the resulting files somewhere you have access to! If you do this on your local machine ~0.5TB must be transfered via network.")
for field in ['split-libraries', 'adaptor-clean-up']:
    path = fasta[field]['dir']
    file = fasta[field]['fnaFile']
    tmpFile = '/tmp/' + field + ".counts"
    cmd = "\tfor f in `find '" + path + "/' -name '" + file + "' | cut -d '_' -f 1 | sort | uniq -c | tr -d '>' | sed 's/^[ ]*//' >> '" + tmpFile + "'; done"
    print(cmd + "\n")

obs = observations
for field in ['split-libraries', 'adaptor-clean-up']:
    tmpFile = '/media/barnacle/home/sjanssen/' + field + ".counts"
    if os.path.isfile(tmpFile):
        x = pd.read_csv(tmpFile, sep=" ", index_col=1, names=["INFASTA_" + field, "sampleID"])
        x.index = x.index.map(str.upper) # use upper case
        obs = obs.merge(x, left_index=True, right_index=True, how="outer")
obs.to_csv(resultsFile, sep="\t")
```

    Execute the following command on 'barnacle' and transfer the resulting files somewhere you have access to! If you do this on your local machine ~0.5TB must be transfered via network.
    	for f in `find '/media/barnacle/projects/emp/01-split-libraries/' -name 'seqs.fna' | cut -d '_' -f 1 | sort | uniq -c | tr -d '>' | sed 's/^[ ]*//' >> '/tmp/split-libraries.counts'; done
    
    	for f in `find '/media/barnacle/projects/emp/02-adaptor-clean-up/' -name 'filtered_seqs.fna' | cut -d '_' -f 1 | sort | uniq -c | tr -d '>' | sed 's/^[ ]*//' >> '/tmp/adaptor-clean-up.counts'; done
    

