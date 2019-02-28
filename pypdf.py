#!c:/Python27/python
print "Content-type: text/html"
print
import PyPDF2
object = open('test.pdf','rb')
reader = PyPDF2.PdfFileReader(object)
pages = reader.numPages

page = reader.getPage(1)
pr = page.extractText()

print pr