#!/usr/bin/env python

"""
get_v4_region.py

Extract the V4 region of a full-length (or longer than V4) 16S rRNA sequence.

Original script by Jenya Kopylova. Modified by Amnon Amir for command line interface 
and trimming the primer sequences.
"""

__version__ = "1.3"

import argparse

#from cogent.parse.fasta import MinimalFastaParser
#import skbio

import sys
import re

def GetV4(inputname, fprimer, rprimer, length, remove_ambig, keep_primers, skip_reverse, output_mismatch=False):
    fplen=0
#    fafile=open(inputname)
#    for seqid, cseq in MinimalFastaParser(fafile):
#    it=skbio.io.read(inputname, format='fasta')
#    for cdat in it:
#        seqid=cdat.metadata['id']
#        cseq=str(cdat)
    for cseq, seqid in iterfastaseqs(inputname):
        cseq=cseq.upper()

        reverse_primer_seq=''
        # find the start of the primer and output all following sequence
        try:
            match=re.search(fprimer, cseq)
            if keep_primers:
                forward_primer_seq = cseq[match.start():]
                fplen=match.end()-match.start()
            else:
                forward_primer_seq = cseq[match.end():]
        except AttributeError:
            forward_primer_seq = ''
            if output_mismatch:
                    print(">%s\n%s" % (seqid, cseq))

        # if sequence can be amplified, search for reverse primer
        if forward_primer_seq != '':
            if not skip_reverse:
                # find the reverse primer and output all following sequence
                try:
                    match=re.search(rprimer, forward_primer_seq)
                    if keep_primers:
                        reverse_primer_seq = forward_primer_seq[:match.end()]
                    else:
                        reverse_primer_seq = forward_primer_seq[:match.start()]
                except AttributeError:
                    reverse_primer_seq = ''
            else:
                reverse_primer_seq=forward_primer_seq[:length+fplen]

            # if sequence can be amplified, convert back to original strand direction
            if reverse_primer_seq != '':
                if length>0:
                    if keep_primers:
                        reverse_primer_seq=reverse_primer_seq[:length+fplen]
                    else:
                        reverse_primer_seq=reverse_primer_seq[:length]
                printit=True
                if output_mismatch:
                    printit=not printit
                if remove_ambig:
                    if 'N' in reverse_primer_seq:
                        printit=False
                if printit:
                    print(">%s\n%s" % (seqid, reverse_primer_seq))


def iterfastaseqs(filename):
    """
    iterate a fasta file and return header, sequence
    input:
    filename - the fasta file name

    output:
    seq - the sequence
    header - the header
    """

    fl=open(filename, "rU")
    cseq=''
    chead=''
    for cline in fl:
        if cline[0]=='>':
            if chead:
                yield(cseq, chead)
            cseq=''
            chead=cline[1:].rstrip()
        else:
            cseq+=cline.strip()
    if cseq:
        yield(cseq, chead)
    fl.close()


def main(argv):
    parser=argparse.ArgumentParser(description='Extract an amplified region from a set of primers (version ' + __version__ + ')')
    parser.add_argument('-i', '--input', help='name of input fasta file')
    #parser.add_argument('-d', '--indir', help='input directory of fastq files (instead of -i)', default="")
    parser.add_argument('-f', '--fprimer', help='forward primer sequence (default is V4f)', default='GTGCCAGC[AC]GCCGCGGTAA')
    #parser.add_argument('-r', '--rprimer', help='reverse primer sequence', default='GGACTAC[ACT][ACG]GGGT[AT]TCTAAT')
    parser.add_argument('-r', '--rprimer', help='reverse primer sequence (in reverse complement) (default is V4r)', default='ATTAGA[AT]ACCC[CGT][AGT]GTAGTCC')
    parser.add_argument('-l', '--length', help='trim all sequences to length (0 for full length)', default='0')
    parser.add_argument('-n', '--remove_ambig', help='remove seqs containing ambiguous characters (N)', action='store_true')
    parser.add_argument('-s', '--skip_reverse', help='do not look for reverse primer', action='store_true')
    parser.add_argument('-k', '--keep_primers', help="do not remove the primer sequences", action='store_true')
    parser.add_argument('-m', '--output_mismatch', help="show sequences with no primer instead", action='store_true')

    args=parser.parse_args(argv)

    # if len(args.indir)>0:
    #     fasta=[]
    #     filelist=[f for f in listdir(args.indir) if isfile(join(args.indir, f))]
    #     for cfile in filelist:
    #         if cfile[-6:]=='.fastq':
    #             fasta.append(join(args.indir, cfile))
    # else:
    # # otherwise use the file list
    #     fasta=[args.infile]

    GetV4(args.input, args.fprimer, args.rprimer, int(args.length), args.remove_ambig, args.keep_primers, args.skip_reverse, args.output_mismatch)

if __name__ == "__main__":
    main(sys.argv[1:])
