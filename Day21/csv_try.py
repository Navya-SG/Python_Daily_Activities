
#read and print
import csv
with open("data.csv") as f:
    read = csv.reader(f)
    for row in read:
        print(row)

#header is skipped
import csv
with open("data.csv") as f:
    read = csv.reader(f)
    next(read)
    for row in read:
        print(row)

#within a list
import csv
with open("data.csv",newline='') as f:
    read = csv.reader(f)
    data = list(read)
print(data)

#rows as dict
import csv
with open("data.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)