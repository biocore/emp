#!/usr/bin/env Rscript

# Copyright 2016 IBM Corp. 
# Robert J. Prill <rjprill@us.ibm.com>
#
# Reads otu_sample_value.txt and writes co-occurrence network 
# thresholded by Z score.

rm(list=ls())

infile = "output/otu_sample_value.txt"

library("Matrix")  # sparseMatrix()

d = read.table(infile, header=T, sep="\t", colClasses=c(rep("character", 2), "numeric"))
otus = read.table("output/row_metadata.txt", header=T, sep="\t", colClasses=rep("character", 9))
samples = read.table("output/column_metadata.txt", header=T, sep="\t", colClasses=rep("character", 2))

# extract row / column indices
I = as.integer(gsub("otu_", "", d$OTU)) + 1        # add 1 to convert 0-index to 1-index
J = as.integer(gsub("sample_", "", d$SAMPLE)) + 1  # add 1 to convert 0-index to 1-index

# sparse OTU matrix
X = sparseMatrix(i=I, j=J, x=d$VALUE)
rownames(X) = otus$ID
colnames(X) = samples$ID

# sparse bipartitie adjacency matrix
Y = (X > 0) * 1

# We need to pick a managable number of OTUs to manipulate the OTU co-occurrence network
# using the code here.

# Pick OTUs that belong to a few prominent phyla
selected.otus = rbind(
  subset(otus, otus$PHYLUM == "p__Proteobacteria", ID),
  subset(otus, otus$PHYLUM == "p__Bacteroidetes", ID),
  subset(otus, otus$PHYLUM == "p__Firmicutes", ID)
)
idx = as.numeric(row.names(selected.otus))
Z = Y[idx,]  # otu-sample adjacency matrix

# Pick OTUs with prevalence of at least 10 samples
idx = rowSums(Z) > 9
Z = Z[idx,]  # otu-sample adjacency matrix

# Order matrix rows by prevalence, high to low
o = order(rowSums(Z), decreasing=T)
Z = Z[o,]
prevalence = rowSums(Z)  # handy to use this later

# OTU co-occurrence graph, entries are the number of shared samples
G = as.matrix(Z %*% t(Z))  # dense matrix
diag(G) = NA

# Prevalence (the number of samples that an OTU occurs in) is a strong driver of 
# co-occurrence. We need some notion of the degree of co-occurrence expected by chance
# given the prevalence of OTU_i and OTU_j. We model the probability of co-occurrence 
# using the binomial distribution. The binomial distribution describes the number of 
# successes in n draws with probability of success p, with replacement.

# binomial null model lookup table
throws = sort(unique(prevalence))
Mu    = matrix(ncol=length(throws), nrow=length(throws))
Sigma = matrix(ncol=length(throws), nrow=length(throws))
N = ncol(Z)
for (i in 1:length(throws)) {
  for (j in i:length(throws)) {
    p = throws[i] / N
    n = throws[j]
    mu = n * p
    sigma = sqrt(n * p * (1-p))
    Mu[i, j] = mu
    Mu[j, i] = mu
    Sigma[i, j] = sigma
    Sigma[j, i] = sigma
  }
}

# Mu and Sigma matrices of the same dimention as G
idx = unlist(lapply(prevalence, function(x) {
  which(throws == x)
}))
MU = Mu[idx,idx]
SIGMA = Sigma[idx,idx]

# Z score
Q = (G - MU) / SIGMA
diag(Q) = NA

# draw a histogram of Z score for a few OTUs to get an idea of a reasonable cutoff
# for (i in seq(1, 100, by=10)) {
#   hist(Q[i,], 100)
# }

H = triu(Q, k=1)  # upper triangle of the symmetric matrix

# prepare and write network file (for rendering in Cytoscape)

k = 20  # Z-score threshold for drawing the figure

sum(H > 20)  # how many edges are in the figure

q = which(H > k, arr.ind=T)  # OTUs with Z score above threshold
a = rownames(H)[q[,1]]
b = rownames(H)[q[,2]]
c = G[q]  # co-occurrence
z = H[q]  # z-score

idx_a = as.integer(gsub("otu_", "", a)) + 1  # add 1 to convert 0-index to 1-index
idx_b = as.integer(gsub("otu_", "", b)) + 1  # add 1 to convert 0-index to 1-index

e = otus[idx_a, "PHYLUM"]
f = otus[idx_b, "PHYLUM"]

# order by z score
o = order(z, decreasing=T)
a = a[o]
b = b[o]
c = c[o]
z = z[o]
e = e[o]
f = f[o]

results = data.frame(SOURCE=a, TARGET=b, ZSCORE=z, COOCCURRENCE=c, PHYLUM_1=e, PHYLUM_2=f)
outfile = paste("../output/otu-co-occurrence-network-z", k, ".txt", sep="")
write.table(results, file=outfile, quote=F, sep="\t", row.names=F, col.names=T)

