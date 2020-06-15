"""A file to import csv files."""

import csv

with open('ExcelVorlage.csv', 'r') as csv_file
    csv_reader = csv.reader(csv_file)

    print(csv_reader)
