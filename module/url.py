import urllib

testfile = urllib.URLopener()
testfile.retrieve("http://randomsite.com/file.gz", "file1.gz")
