import os
import glob
import collections

os.chdir(r"/home/avhaleraj/akshata")
cnt=collections.Counter()
x=glob.glob("*.*")
for i in x:
    name, ext = os.path.splitext(i)
    cnt[ext]+=1
print "\n" 
print cnt
    
    
