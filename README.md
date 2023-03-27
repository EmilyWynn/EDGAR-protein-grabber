# EDGAR-protein-grabber
EDGAR (https://edgar.computational.bio.uni-giessen.de/) is a bioinformatic tool that can find the genes in the  pangenome or coregenome of a set of genomes. EDGAR can output amino acid sequences. However, if you want to sort a pangenome to find the shared core genome of multiple species, there in no easy way to export that subset of amino acid sequences. This python script allows you to sort an EDGAR output file to find any permutation of shared or unique core genomes and extract the amino acid sequences.

If the pangenome analysis in EDGAR is done on a small number of genomes, the pangenome spreadsheet will be a csv file. Use prepEDGAR_CSV.py to format the file to the correct format. To run EDGAR-protein-grabber.py, the names of the genomes on the header row must be the same as the gff files that correspond with those genomes.

If the pangenome analyis in EDGAR is done on a large number of genomes, the pangenome spreadsheet will be a tsv file. Use prepEDGAR_TSV.py to format the file to the correct format. To run EDGAR-protein-grabber.py, the names of the genomes on the header row must be the same as the gff files that correspond with those genomes.
