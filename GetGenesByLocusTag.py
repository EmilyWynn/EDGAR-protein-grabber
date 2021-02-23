#! /usr/bin/env python3
import os, sys, csv
from collections import deque
from itertools import islice
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna

# This script takes the formatted EDGAR output from prepEDGAR.py and uses it to get the amino acid sequences of each locus.
# While EDGAR has an output option for amino acid sequences, this script allows for more flexiblity in analysis.
# EDGAR output can be sorted in any way, for example the shared core genomes between multiple species, and this script can be used to extract amino acid sequences.
# For this script to run properly, GFF annotation files for all genomes in the EDGAR output must be available in the same directory

InputFilename = input("Input csv file from prepEDGAR.py: ")
OutputFilename = InputFilename.replace(".csv", "_AA.fasta")
GFFpath = input("Input path to GFF files: ")

# Skips last 3 lines of the GFF file, so that only annotation data is read
def skip_last_n(iterator, n=3):
    it = iter(iterator)
    prev = deque(islice(it, n), n)
    for item in it:
        yield prev.popleft()
        prev.append(item)

# Gets the name of the gene from GFF file
def GeneProdName(inputChunk):
    return inputChunk[inputChunk.index(";product=")+9:inputChunk.index(";inference")]
# Gets the locus tag of the gene from GFF file
def GeneProdLocus(inputChunk):
    return inputChunk[inputChunk.index(";locus_tag=")+11:inputChunk.index(";locus_tag=")+22]
# Gets the amino acid translation of the gene from GFF file    
def GeneProdTranslation(inputChunk):
    return inputChunk[inputChunk.index(";translation=")+13:inputChunk.index(";locus")]
    
with open(OutputFilename, "w") as Outfile:
    with open(InputFilename) as CoreFile:
        corereader = csv.reader(CoreFile, delimiter = ",")
        for corerow in corereader:
            with open(GFFpath + corerow[0].replace(" ","") + ".gff") as GFFinput:
                reader = csv.reader(GFFinput, delimiter="	")
                csv.field_size_limit(sys.maxsize)
                featureType = []
                start = []
                stop = []
                direction = []
                geneProd = []
                locustag = []
                translation = []
                species = []
                next(reader)
                iteration = 0
                numHyp = 0
# Loads GFF annotations into lists
                for row in skip_last_n(reader):
                    if row[2] == "CDS":
                        species.append(row[0])
                        start.append(int(row[3]))
                        stop.append(int(row[4]))
                        direction.append(row[6])
# Numbers the hypothetical proteins, so that each has a unique name
# Note, this will not give consistent names to the same hypothetical proteins in different genomes
                        try:
                            if GeneProdName(row[8]) == "hypothetical protein":
                                geneProd.append(GeneProdName(row[8]) + " " + str(numHyp))
                                numHyp += 1
                            else:
                                geneProd.append(GeneProdName(row[8]).replace("'",""))
                            iteration += 1
                        except:
                            print("CDS product on line number " + str(iteration+1) + "is formatted weird")
                        try:
                            locustag.append(GeneProdLocus(row[8]))
                        except:
                            print("problem with locustag")
                        try:
                            translation.append(GeneProdTranslation(row[8]))
                        except:
                            print("Problem with translation at " + corerow[0] + " " + GeneProdLocus(row[8]))

                    else:
                        pass
# Loops through locus tags from formatted EDGAR output and finds the amino acid sequence in GFF file
            for z in range(1,len(corerow)):
# Ensures that empty cells of formatted EDGAR csv are skipped
                if len(corerow[z]) > 5:
                    loc = corerow[z]
                    for i in range(len(locustag)):
                        if str(loc) == str(locustag[i]):
                            try:
                                print(">" + str(species[i]) + "_" + corerow[0] + "_" + loc + "_" + str(start[i]) + "_" + str(stop[i]) + "_" + geneProd[i].replace(" ","_"), file = Outfile)
                                print(translation[i], file = Outfile)
                            except:
                                pass
                    
                    
                    
