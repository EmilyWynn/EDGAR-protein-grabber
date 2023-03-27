#! /usr/bin/env python3
import csv

with open('input.csv', 'r') as input_file, open('output.csv', 'w', newline='') as output_file:
    input_reader = csv.reader(input_file)
    output_writer = csv.writer(output_file)
    header_row = next(input_reader)
    output_writer.writerow(header_row)

    for row in input_reader:
        processed_row = list(filter(None, [cell.split(', ')[0].strip() for cell in row]))
        output_writer.writerow(processed_row)
