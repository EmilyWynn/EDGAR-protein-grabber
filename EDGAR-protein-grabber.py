import csv, os

li = os.listdir(os.getcwd())
inds = filter(lambda x: ".csv" in x, li)

#set the path to the gff files, edit below to point to the folder with your GFF files
GFFpath = "/path/to/gff/files/"

for ind in inds:
    with open(ind.replace(".csv","AA.fasta"), "w") as outfile:
        with open(ind) as f:
            reader = csv.reader(f)
            for row in reader:
                gff_filename = row[0] + '.gff'
                with open(GFFpath + gff_filename) as gff_file:
                    for cell in row[1:]:
                        if cell and cell != '-':
                            for line in gff_file:
                                if cell in line:
                                    if ';translation=' in line:
                                        start = line.index(';translation=') + 13
                                        end = line.index('locus_tag=') - 1
                                        header = f">{gff_filename.split('.')[0]}_{cell}\n"
                                        sequence = line[start:end] + '\n'
                                        print(header + sequence, end='', file = outfile)
                                    break
                            gff_file.seek(0)  # reset the file pointer to the beginning of the file
