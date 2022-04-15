#import libraries
from datetime  import datetime
from datetime import timedelta

t2=timedelta(days=345,minutes=20)
print(t2.days)


fil1=open('file1.txt','w+')
fil1.write("hi dileep")

fil2=open('file2.txt','w+')
fil2.write("hey golla")

import zipfile
comprfile=zipfile.ZipFile('comprfile.zip','w')
comprfile.write('file1.txt',compress_type=zipfile.ZIP_DEFLATED)
comprfile.write('file2.txt',compress_type=zipfile.ZIP_DEFLATED)
zip_obj=zipfile.ZipFile('comprfile.zip','r')
zip_obj.extractall("extracted")

