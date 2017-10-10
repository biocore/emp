#!/usr/bin/env ruby

# Copyright 2016 IBM Corp. 
# Robert J. Prill <rjprill@us.ibm.com>
#
# Converts biom json format to tsv format (for loading into R)

require 'json'

unless ARGV.size > 1
  puts "USAGE: #{__FILE__} [otus.biom.json] [outdir]"
  exit 1
end

infile, outdir = ARGV
outdir = outdir.sub(/\/$/, "")

def peek(j)  # for debugging
  j.each do |k, v|
    puts [k, v.class].join("\t")
  end
  puts "--------------------------------------------------"
  puts j[:data][0..9].map { |x| x.join(", ") }
  puts "--------------------------------------------------"
  puts j[:rows][0..9]
  puts "--------------------------------------------------"
  puts j[:columns][0..9]
end

str = File.readlines(infile).join
j = JSON.parse(str, symbolize_names: true)

# peek(j)  # for debugging

outfile = "#{outdir}/otu_sample_value.txt"
STDERR.puts "writing #{outfile}"
File.open(outfile, "w") do |f|
  f.puts %w[OTU SAMPLE VALUE].join("\t")
  j[:data].each do |x|
    otu, sample, count = x
    f.puts ["otu_#{otu}", "sample_#{sample}", count.to_i].join("\t")
  end
end

outfile = "#{outdir}/row_metadata.txt"
STDERR.puts "writing #{outfile}"
File.open(outfile, "w") do |f|
  f.puts %w[ID SEQUENCE KINGDOM PHYLUM CLASS ORDER FAMILY GENUS SPECIES].join("\t")
  j[:rows].each_with_index do |x, i|
    taxonomy = x[:metadata][:taxonomy]
    until taxonomy.size >= 7
      taxonomy << ""
    end
    f.puts (["otu_#{i}", x[:id]] + x[:metadata][:taxonomy]).join("\t")
  end
end

outfile = "#{outdir}/column_metadata.txt"
STDERR.puts "writing #{outfile}"
File.open(outfile, "w") do |f|
  f.puts %w[ID SAMPLE].join("\t")
  j[:columns].each_with_index do |x, i|
    f.puts ["sample_#{i}", x[:id]].join("\t")
  end
end

