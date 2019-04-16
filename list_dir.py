#!c:/Python27/python
print "Content-type: text/html"
print
#from __future__ import print_function
import os
 
path = '.'
 
files = os.listdir(path)
for name in files:
    print name,'<br>'