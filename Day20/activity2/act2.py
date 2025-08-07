import zipfile
with zipfile.ZipFile('act_archive.zip', mode='w') as zf:
    zf.write('file1.txt')
    zf.write('file2.txt')
    zf.write('file3.txt')
            
with zipfile.ZipFile('act_archive.zip', 'r') as zipf:
    files = zipf.namelist()
    for file in files:
        print(file)
        with zipf.open(file) as f:
            content = f.read()
            print(content)