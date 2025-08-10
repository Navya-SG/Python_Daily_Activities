#data.csv
'''
Name,Age
Alice,30

Bob,25'''

import csv
with open("data.csv") as f:
    read = csv.reader(f)
    for row in read:
        if row:
            print(row)

import csv
with open("data.csv") as f:
    read = csv.reader(f)
    for row in read:
        if any(field.strip() for field in row):
            print(row)