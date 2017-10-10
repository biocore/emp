#!/usr/bin/env python
#!/home/amam7564/qiime_software/python-2.7.3-release/bin/python
# -*- coding: utf-8 -*-
"""
deblur a directory of .fasta sequences in parallel
IGNORES MEAN READ ERROR!!!
Created on Fri Dec 27 17:09:10 2013
@author: amnon
"""

__version__ = "1.3"

import argparse

import stat
import sys
import os
from os.path import join
from subprocess import call
import time

# write to log
def WriteLog(logfilename,what):
    with open(logfilename,'a') as logFile:
        logFile.write(what+'\n')

# split directory to parts and run clean_SRBactDB.sh on them in parallel
# then wait for all processes to finish before ending
# input:
# dirname - the directory to clean
# numprocs - the number of processes
# readlen - lenght to trim sequences (99)
# readerror - the upper limit for read error (0.01)
# meanerror - the mean read error (0.01)
# logfilename - filename for the log
# keeptmp - if true don't delete temporary files
# indelprob - the probability for indel occuring (constant for number of indels...)
# indelmax - the maximal indel allowable
# pyroseq - if true, use the pairwise alignment for pyrosequencing mode
def CleanDirParallel(dirname,numprocs,readlen,readerror,meanerror,errordist,logfilename,keeptmp,indelprob,indelmax,pyroseq,usecompy):
    WriteLog(logfilename,'Preparing to clean parallel using '+str(numprocs)+' processes')
    WriteLog(logfilename,'Current directory is:'+os.getcwd())
    WriteLog(logfilename,'Directory to clean is:'+dirname)
    # prepare the file list in the directory
    fileList=[f for f in os.listdir(dirname) if f.endswith('.fasta')]
    WriteLog(logfilename,'Number of files:'+str(len(fileList)))

    if len(fileList)==0:
        WriteLog(logfilename,'0 files!!!! exiting')
        return

    # don't need more processes than files
    if len(fileList)<numprocs:
        numprocs=len(fileList)
        WriteLog(logfilename,'More processes than files - corrected !')
    # calculate how many files per process and store it in procFiles
    # we round up
    filesPerProcess=int(0.9999999+float(len(fileList))/numprocs)
    tfiles=0
    procFiles=[]
    for cproc in range(numprocs):
        numfiles=min(filesPerProcess,len(fileList)-tfiles)
        if (numfiles<0):
            numfiles=0
        procFiles.append(numfiles)
        tfiles+=procFiles[cproc]
        # don't create too many processes
        if numfiles==0:
            numprocs=min(numprocs,cproc)

    # now create a script for moving the files to the subdir and running clean on it
    scriptFileName=join(dirname,'RunParallel.sh')
    with open(scriptFileName,'w') as scriptFile:
        listpos=0
        for cproc in range(numprocs):
            WriteLog(logfilename,'Process:'+str(cproc)+' has '+str(procFiles[cproc])+' files')
            # create the process directory
            pDirName=join(dirname,'parallel_clean_'+str(cproc))
            scriptFile.write('mkdir '+pDirName+'\n')
            # move all the files to the process directory
            for cfile in range(procFiles[cproc]):
                scriptFile.write('mv '+join(dirname,fileList[listpos])+' '+join(pDirName,fileList[listpos])+'\n')
                listpos+=1

            # see what qsub to use (different between compy and barnacle)
            if usecompy:
                qsubStr='qsub -d $PWD -V -k oe -q friendlyq -N clean_'+dirname+'_p_'+str(cproc)
            else:
                qsubStr='qsub -d $PWD -V -k oe -l walltime=48:00:00,nodes=1:ppn=1,pmem=8gb -N clean_'+dirname+'_p_'+str(cproc)

            if pyroseq:
                scriptFile.write('echo "/home/amam7564/scripts/clean_indel_pyro.sh '+pDirName+' '+str(readlen)+' '+str(readerror)+' '+str(meanerror)+' '+str(errordist)+' '+str(indelprob)+' '+str(indelmax)+'" | '+qsubStr+'\n')
            else:
                scriptFile.write('echo "/home/amam7564/scripts/clean_indel.sh '+pDirName+' '+str(readlen)+' '+str(readerror)+' '+str(meanerror)+' '+str(errordist)+' '+str(indelprob)+' '+str(indelmax)+'" | '+qsubStr+'\n')

    # and make the script executable
    cstat=os.stat(scriptFileName)
    os.chmod(scriptFileName,cstat.st_mode | stat.S_IEXEC)

    # now run the script
    WriteLog(logfilename,'Preparing to run script file:'+scriptFileName)
    call(scriptFileName,shell=True)
    WriteLog(logfilename,'Script run, waiting for processes to finish'+scriptFileName)


    # and wait for all processes to finish (note this can hang!!!)
    done = 0
    while not done:
        # wait a sleep interval (30 secs)
        time.sleep(30)
        # check if all processes finished
        done=1
        for cproc in range(numprocs):
            pDirName=join(dirname,'parallel_clean_'+str(cproc))
            if not os.path.exists(join(pDirName,'process.finished')):
                done=0
    WriteLog(logfilename,'* Script Finished !')

    # now copy all the resulting files to main directory
    scriptFileName=join(dirname,'CopyBack.sh')
    with open(scriptFileName,'w') as scriptFile:
        for cproc in range(numprocs):
            pDirName=join(dirname,'parallel_clean_'+str(cproc))
            scriptFile.write('mv '+pDirName+'/*.ref.fa '+dirname+'/\n')
            scriptFile.write('mv '+pDirName+'/*.ref.t.fa '+dirname+'/\n')
            scriptFile.write('mv '+pDirName+'/*.log '+dirname+'/\n')
            scriptFile.write('mv '+pDirName+'/*.fasta '+dirname+'/\n')
            scriptFile.write('mv '+pDirName+'/*.fasta.tuni '+dirname+'/\n')
            scriptFile.write('mv '+pDirName+'/*.fasta.ptuni '+dirname+'/\n')
            # if we set the keeptmp flag, don't delete the old directory
            if not keeptmp:
                scriptFile.write('rm -r '+pDirName+'\n')

    # and make the script executable
    cstat=os.stat(scriptFileName)
    os.chmod(scriptFileName,cstat.st_mode | stat.S_IEXEC)

    # now run the script
    WriteLog(logfilename,'Preparing to run the move .ref.fa files script file: '+scriptFileName)
    call(scriptFileName,shell=True)
    WriteLog(logfilename,'Script finished')
    WriteLog(logfilename,'***Done.')


def main(argv):
    parser=argparse.ArgumentParser(description='Clean a directory of split illumina reads in parallel')
    parser.add_argument('dirname',help='input dir (containing .fasta files for each sample)')
    parser.add_argument('-l','--readlen',help='read length',default=99,type=int)
    parser.add_argument('-e','--readerror',help='max read error fraction',default=0.01,type=float)
    parser.add_argument('-m','--meanerror',help='the mean error rate for peak normalization (default same as readerror)',default=-1,type=float)
    parser.add_argument('-d','--errordist',help='a comma separated list of error probabilities for each edit distance (min length=10)',default=0)
    parser.add_argument('-n','--numprocs',help='number of processes',default=1,type=int)
    parser.add_argument('-o','--logfile',help='log file name',default='parallel.log')
    parser.add_argument('--indelmax',help='maximal indel number',default=3)
    parser.add_argument('-i','--indelprob',help='indel probability (same for N indels)',default=0.01)
    parser.add_argument('--keeptmp',help="don't delete temporary files",action='store_true')
    parser.add_argument('-p','--pyroseq',help='Use pairwise alignment for pyrosequencing (slower)',action='store_true')
    parser.add_argument('--compy',help='Use the compy qsub instead of barnacle',action='store_true')

    args=parser.parse_args(argv)
    if (args.meanerror<0):
        args.meanerror=args.readerror

    CleanDirParallel(args.dirname,args.numprocs,args.readlen,args.readerror,args.meanerror,args.errordist,args.logfile,args.keeptmp,args.indelprob,args.indelmax,args.pyroseq,args.compy)

if __name__ == "__main__":
    main(sys.argv[1:])
