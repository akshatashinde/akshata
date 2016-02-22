import glob
import os

for filename in glob.glob('home/**/*.py', recursive=True):
    print(filename)
