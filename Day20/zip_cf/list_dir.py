# import os 
# files = os.listdir("Day20")
# print(files)

import zipfile
zip_path = input("Enter the zip file:")
with zipfile.ZipFile(zip_path, 'r') as zipf:
    print(zipf.namelist()) 
    target= input("Enter the file from the above listed files:")
    print(zipf.extract(target))




