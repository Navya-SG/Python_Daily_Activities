import zipfile
with zipfile.ZipFile('archive.zip','r') as zipf:
    zipf.extractall('extracted_files')