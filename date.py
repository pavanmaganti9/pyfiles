#!c:/Python27/python
print "Content-type: text/html"
print
import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))
print "<br><br>"