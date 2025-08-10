#
'{"name":["Alice","Bob"],"Age":[30,25],"City":["New York","Bob"]}'

#
print("{}hello,{}!".format("Alice",42)) #Alicehello,42!
print("{n1} Hello, {n2}!".format(n2='Alice',n1=42)) #42 Hello, Alice!
print("{2} scored {0} marks in {1}".format(85,"Maths","Alice")) #Alice scored 85 marks in Maths
print("{%d} Hello, {%s}!" % (42, 'Alice')) #{42} Hello, {Alice}!

#
user="ravi"
score=87.5
print(f"{user=},{score=},{score/100=:.2%}") #user='ravi',score=87.5,score/100=87.50%

#
import pandas as pd
help(pd)

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

#column names
import csv
with open("data.csv", newline='') as f:
    reader = csv.DictReader(f)
    print(reader.fieldnames)  # Output: ['Name', 'Amount']

#rewrites the file
import csv
with open("data.csv","w",newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name","Age","City"])
    writer.writerow(["Eve",40,"Paris"])

#rewrite with multiple rows
import csv
rows = [
    ["Name", "Age", "City"],
    ["Alice", 30, "New York"],
    ["Bob", 25, "London"]]
with open("data.csv",mode="w") as f:
    writer = csv.writer(f)
    writer.writerows(rows)

#writing csv as dict
import csv
data = [
    {"Name": "Alice", "Age": 30, "City": "New York"},
    {"Name": "Bob", "Age": 25, "City": "London"}]
with open("data.csv", mode="w", newline='') as f:
    writer = csv.DictWriter(f, fieldnames=["Name", "Age", "City"])
    writer.writeheader()
    writer.writerows(data)     

#delimeter read
import csv
with open("data.csv") as f:
    reader = csv.DictReader(f, delimiter=";")
    for row in reader:
        print(row)  

#delimeter write
import csv
with open("data.csv", mode="w") as f:
    data = [["Name", "Age", "City"], ["Alice", 30, "New York"]]
    writer = csv.writer(f, delimiter=';')
    writer.writerows(data)