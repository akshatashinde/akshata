import os
import fnmatch

for root, dir, files in os.walk("."):
    print root
    print " "
    for items in fnmatch.filter(files,"*"):
            print "..." + items
    print "\t" 
