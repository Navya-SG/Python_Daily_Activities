'''import csv
with open("data.csv","r+") as f:
    writer=csv.writer(f,fieldnames=["Age"] quoting = csv.QUOTE_MINIMAL ,quotechar="-")
    for row in writer:
        row_f = [row[0],f"-{row[1]}-",row[2]]
        writer.writerow(row_f)


import csv
with open("data.csv", "r") as inf, open("output.csv", "w", newline='') as out:
    reader = csv.reader(inf)
    writer = csv.writer(out, quoting=csv.QUOTE_NONNUMERIC, quotechar='-', delimiter=',')
    for row in reader:
        writer.writerow(row)

import csv
with open("data.csv", "r") as inf, open("output.csv", "w", newline='') as out:
    reader = csv.DictReader(inf)
    next(reader)
    fieldnames = reader.fieldnames
    writer = csv.DictWriter(out, fieldnames=["Age"], quoting=csv.QUOTE_NONNUMERIC, quotechar='-', delimiter=',')
    writer.writeheader()
    for row in reader:
        writer.writerow(row)'''


import csv
with open("data.csv", "r") as inf, open("output.csv", "w", newline='') as outf:
    reader = csv.DictReader(inf)
    writer = csv.writer(outf)
    writer.writerow(["Name", "Age", "City"])
    for row in reader:
        writer.writerow([row["Name"], f'-{row["Age"]}-',row["City"]])
        