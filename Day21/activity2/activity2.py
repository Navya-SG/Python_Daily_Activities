#
import csv
total = 0.0
with open("data.csv") as f:
    read = csv.DictReader(f)
    for row in read:
        total += float(row["Amount"])
print(total)

#
import csv
total = 0
with open("data.csv") as f:
    read = csv.reader(f)
    next(read)
    for row in read:
        total += float(row[1])
print(total)
