#!/usr/bin/env python


"""
Filter otus from a biom table keeping only ones which are present in a corresponding tree file.
Useful for removing non-16s otus following negative mode deblurring
"""

# amnonscript

__version__ = "1.0"

import biom
import skbio.tree

import argparse
import sys


def filterbiombytree(tablefilename,treefilename,outfilename,nomatchfilename=None):
	print('loading tree data from file %s' % treefilename)
	treedat=skbio.tree.TreeNode.read(treefilename)

	table=biom.load_table(tablefilename)

	print('getting sequences')
	seqlist=[]
	for ctip in treedat.tips():
		seqlist.append(ctip.name)
	print('found %d tips' % len(seqlist))
	print('filtering')
	ftable=table.filter(seqlist,axis='observation',inplace=False)
	print('saving')
	with biom.util.biom_open(outfilename, 'w') as f:
		ftable.to_hdf5(f, "filterbiombytree")
	if nomatchfilename is not None:
		table=biom.load_table(tablefilename)
		table.filter(seqlist,axis='observation',invert=True)
		print('saving non matches')
		with biom.util.biom_open(nomatchfilename, 'w') as f:
			table.to_hdf5(f, "filterbiombytree nomatch")


def main(argv):
	parser=argparse.ArgumentParser(description='Filter otus from biom table keeping only ones present in a tree. Version '+__version__)
	parser.add_argument('-t','--treefile',help='tree file file name')
	parser.add_argument('-i','--inputtable',help='input biom table file name')
	parser.add_argument('-o','--output',help='output biom file name')
	parser.add_argument('--nomatch',help='filename for non matching sequences')

	args=parser.parse_args(argv)

	filterbiombytree(args.inputtable,args.treefile,args.output,args.nomatch)

if __name__ == "__main__":
	main(sys.argv[1:])
