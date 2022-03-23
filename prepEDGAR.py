#! /usr/bin/env python3
import os, sys

# This script takes the output of an EDGAR pangenome or coregenome analysis (csv old format) and formats it for use with GetGenesByLocusTag.py
# This script assumes that all genome accessions are 10 characters long (I.E "CP000947.1"). Accessions with more or less characters will need to be fixed before moving to downstream analysis.
li = os.listdir(os.getcwd())
inds = list(filter(lambda x: ".csv" in x, li))
inds.sort()

#InputFilename = input("Input file: ")
#OutputFilename = input("Output file: ")
for ind in inds:
    InputFilename = ind
    OutputFilename = ind.replace(".csv","z.csv")

    with open(InputFilename, encoding='utf-8-sig') as infile:
        with open(OutputFilename, "w") as outfile:
            matrix = []
            firstLine = infile.readline()
            firstLine = firstLine.strip().split(",")
            for x in range(len(firstLine)):
                firstLine[x] = firstLine[x]
            matrix.append(firstLine)
            print(matrix)
            for x in infile:
                line = x.replace(', ,psos,','').replace('"','')
                line = line.split(",")
                locus = []
                for y in range(len(line)):
                    locus.append(str(line[y])[:11])
                matrix.append(locus)
            transp = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
            for row in transp:
                print(str(row).replace("[","").replace("'","").replace("]","").replace(" ","").replace("\\n",""), file= outfile)