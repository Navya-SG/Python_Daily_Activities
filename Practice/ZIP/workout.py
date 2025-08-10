# create zip folder,add files
import zipfile
with zipfile.ZipFile("archive.zip","r") as zf:
    zf.write("file1.txt")
    zf.write("file2.txt")
    zf.write("file1.txt")

# create files and add content with code
import zipfile
for i in range(1,4):
    with open(f"file{i}.txt","w") as file:
        file.write(f"Hello from file{i}!")

#create zip folder and add the files
with zipfile.ZipFile("archive.zip","w") as zf:
    for i in range(1,4):
       zf.write(f"file{i}.txt")

#extract from zip folder to another folder
import zipfile
with zipfile.ZipFile("archive.zip","r") as zf:
    zf.extractall("extract")

# create folder
import os
os.makedirs('extract', exist_ok=True)

# .printdir()
import zipfile
with zipfile.ZipFile("archive.zip", "r") as zf:
    zf.printdir()

#info about all files in folder
import zipfile
with zipfile.ZipFile("archive.zip", "r") as zf:
    for info in zf.infolist():
       print(info.filename, info.file_size, info.compress_type)

#info about particular file
import zipfile
with zipfile.ZipFile("archive.zip", "r") as zf:
    info = zf.getinfo("file1.txt")
    print(info.filename, info.file_size, info.compress_type)

# combined
import zipfile
import os
for i in range(1,4):
    with open(f"file{i}.txt","w") as file:
        file.write(f"Hello from file{i}!")
with zipfile.ZipFile("archive.zip","w") as zf:
    for i in range(1,4):
       zf.write(f"file{i}.txt")
os.makedirs('extract', exist_ok=True)
with zipfile.ZipFile("archive.zip","r") as zf:
    zf.extractall('extract')

#contents from file in zip
import zipfile
# Open the ZIP file in read mode
with zipfile.ZipFile("archive.zip", "r") as zf:
    files = zf.namelist() # List all files in the ZIP
    for file in files:
        with zf.open(file) as f:
            content = f.read().decode("utf-8")  # decode bytes to string
            print(f"Contents of {file}:\n{content}\n")

#append
import zipfile
with open("newfile.txt", "w") as f: # Create a new file to add
    f.write("This is a new file")
with zipfile.ZipFile("archive.zip", "a") as zf:# Append to existing ZIP
    zf.write("newfile.txt")

#act1
import zipfile
with zipfile.ZipFile("archive.zip", "r") as zf:        
    if "file1.txt" in zf.namelist():
        print("found")
    else:
        print("missing")

#act2
import zipfile
with zipfile.ZipFile("archive.zip","w",compression=zipfile.ZIP_LZMA) as czf:
    for i in range(1,4):
        czf.write(f"file{i}.txt")
    for info in czf.infolist():
        print(f"{info.filename} => {info.compress_size} bytes")

