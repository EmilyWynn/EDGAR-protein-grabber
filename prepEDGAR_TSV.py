import csv

with open('input.tsv', 'r') as input_file:
    input_data = [row for row in csv.reader(input_file, delimiter='\t')]

def get_odd_columns(row):
    return row[::2]

output_data = [get_odd_columns(row) for row in input_data]

with open('output.csv', 'w', newline='') as output_file:
    csv.writer(output_file).writerows(output_data)
