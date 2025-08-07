import zipfile
zip_path = input("Enter the path: ")
with zipfile.ZipFile(zip_path,'r') as zipf:
    if 'foo.txt' in zipf.namelist():
        print("Found!")
    else:
        print("Missing!")
