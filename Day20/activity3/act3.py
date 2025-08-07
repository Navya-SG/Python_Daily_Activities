import zipfile
with zipfile.ZipFile('act3_archive.zip', mode='w',compression=zipfile.ZIP_BZIP2) as zf:
    zf.write('f1.txt')
    zf.write('f2.txt')
    zf.write('f3.txt')

    inf_zip = zf.infolist()
    for info in inf_zip:
        print(f"{info.filename} => {info.compress_size} bytes")

          
