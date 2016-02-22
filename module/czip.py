import zipfile
import os.path
zipFileNameSrc = 'All_scr.zip'
zipFile = open(zipFileNameSrc, 'rb')
unzippedFile = zipfile.ZipFile(zipFile)
imgList = [(s, unzippedFile.read(s)) for s in unzippedFile.namelist() if (".png" or ".PNG")]
for i in range(1,5):
    zipFileName = os.path.join('<some location>','ziptest_' + str(i) + '.zip')
    print('Creating ', zipFileName)
    zipOut = zipfile.ZipFile(zipFileName, 'w')
    for j in range(25):
        ind = (i-1)*25 + j
        fileNameAndPath = imgList[ind][0]
        actualFile = imgList[ind][1]
        zipOut.writestr(fileNameAndPath, actualFile)
    zipOut.close()
