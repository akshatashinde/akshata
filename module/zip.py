import zipfile
z = zipfile.ZipFile("All_scr.zip")
for name in z.namelist():
    print name
