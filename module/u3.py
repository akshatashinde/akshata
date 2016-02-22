import requests
import os
import shutil

global dump

def download_file():
    global dump
    url = "http://randomsite.com/file.gz"
    file = requests.get(url, stream=True)
    dump = file.raw

def save_file():
    global dump
    location = os.path.abspath("/home/avhaleraj/akshata/file.gz")
    with open("file.gz", 'wb') as location:
        shutil.copyfileobj(dump, location)
    del dump
    
download_file()
save_file()
print "url download successfully"
    
    
