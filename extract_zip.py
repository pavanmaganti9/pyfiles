#!c:/Python27/python
print "Content-type: text/html"
print
# import zipfile
# with zipfile.ZipFile("pagination.zip","r") as zip_ref:
    # zip_ref.extractall("unzips")
	
import zipfile
zip_ref = zipfile.ZipFile("pagination.rar", 'r')
zip_ref.extractall("unzips")
zip_ref.close()