
import csv
with open("data.csv","r") as f:
    reader = csv.reader(f)
    next(reader)
    next(reader)
    for i in reader:
        print(i)