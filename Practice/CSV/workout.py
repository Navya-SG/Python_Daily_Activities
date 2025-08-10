# read csv file data
import csv
with open("data.csv","r") as f:
    reader = csv.reader(f)
    for i in reader:
        print(i)

#write single row mutiple times
import csv
with open("data.csv","w") as f:
    writer = csv.writer(f)
    writer.writerow(["name","age"])
    writer.writerow(["navya",22])

#write multiple rows single time
import csv
data = [["name","age"],["navya",22],["bob",32]]
with open("data.csv","w") as f:
    writer = csv.writer(f)
    writer.writerows(data)

#write dict data to csv file
import csv
data = [{"Name": "Alice", "Age": 30, "City": "New York"},{"Name": "Bob", "Age": 25, "City": "London"}]
with open("data.csv","w") as f:
    writer = csv.DictWriter(f,fieldnames=["Name","Age","City"])
    writer.writeheader()
    writer.writerows(data)

#read with delimiter (if wrong given, return single string 'Name,Age,City')
import csv
with open("data.csv","r") as f:
    reader = csv.reader(f,delimiter=";")
    for i in reader:
        print(i)

#write with delimeter (to tell how to seperate data)
import csv
data = [["Name", "Age", "City"], ["Alice", 30, "New York"]]
with open("output.csv", mode="w") as f:
    writer=csv.writer(f, delimiter='\t') #(, ; | \t)
    writer.writerows(data)

#quoting write
#QUOTE_ALL(all),QUOTE_NONNUMERIC(non numeric only),QUOTE_NONE(quote nothing),QUOTE_MINIMAL("New, Year","New \n Year")
import csv
data = [["Name", "Age", "City"], ["Alice", 30, "New York"]]
with open("output.csv", mode="w") as f:
    writer=csv.writer(f,quotechar="$",quoting=csv.QUOTE_MINIMAL) 
    writer.writerows(data)

#read quote,escape char
#data.csv
"Name","Comment"
"Alice","He said, \"Hello!\""
"Bob","Path is C:\\Users\\Bob"
#code
import csv
with open("data.csv","r") as f:
    reader = csv.reader(f,quotechar='"',escapechar="\\")
    for i in reader:
        print(i)
#output
['Name', 'Comment']
['Alice', 'He said, "Hello!"']
['Bob', 'Path is C:\\Users\\Bob']

#print non-empty rows
import csv
with open("data.csv","r") as f:
    reader = csv.reader(f)
    for i in reader:
        if i:
            print(i) 

import csv
with open("data.csv","r") as f:
    reader = csv.reader(f)
    for i in reader:
        if any(field.strip() for field in i):
            print(i) 

#skip header
import csv
with open("data.csv","r") as f:
    reader = csv.reader(f)
    next(reader)
    for i in reader:
        print(i)

# read as list
import csv
with open("data.csv","r") as f:
    reader = csv.reader(f)
    data = reader #<_csv.reader object at 0x0000015BA0256740>
    data = list(reader) #[['Name', 'Age'], ['Alice', '30'], ['Bob', '25']]
print(data) 

#line_num
import csv
with open("data.csv","r") as f:
    reader = csv.reader(f)
    for i in reader:
        print(reader.line_num,i)

# read data as dict
import csv
with open("data.csv","r") as f:
    reader = csv.DictReader(f)
    for i in reader:
        print(i)

# read particular data as dict
import csv
with open("data.csv","r") as f:
    reader = csv.DictReader(f)
    for i in reader:
        print(i["Name"],i["Age"])

#column names - fieldnames
import csv
total = 0
with open("data.csv","r") as f:
    reader = csv.DictReader(f)
    print(reader.fieldnames)


#act1
import csv
total = 0
with open("data.csv","r") as f:
    reader = csv.DictReader(f)
    for i in reader:
        total += float(i["Amount"])
print(total)

import csv
total = 0
with open("data.csv", "r") as f:
    reader = csv.reader(f)
    header = next(reader)
    index = header.index("Amount") 
    for i in reader:
        total += float(i[index])
print(total)

#act2
import csv
with open("data.csv","r") as f:
    reader = csv.reader(f)
    head = next(reader)
    with open("output.csv","w") as f1:
        writer = csv.writer(f1)
        writer.writerow([head[0],f"-{head[1]}-",head[2]])
        for j in reader:
            writer.writerow([j[0],f"-{j[1]}-",j[2]])

#act3
import csv
with open("data.csv", newline='') as f:
    sample = f.read(1024)
    f.seek(0)
    sniffer = csv.Sniffer()
    dialect = sniffer.sniff(sample)
    has_header = sniffer.has_header(sample)
    print("Delimiter:", dialect.delimiter)
    print("Quote char:", dialect.quotechar)
    print("Has Header:", has_header)
