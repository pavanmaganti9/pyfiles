#!d:/Python27/python
print "Content-type: text/html"
print
print ("Pavan")
print "<br><br>"

import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))
print "<br><br>"

import urlparse
url = 'http://example.com/?q=abc&p=123'
par = urlparse.parse_qs(urlparse.urlparse(url).query)
print par['q'], par['p']

import MySQLdb

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="",  # your password
                     db="gold")        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# Use all the SQL you like
cur.execute("SELECT * FROM tbl_banner")

# print all the first cell of all the rows
for row in cur.fetchall():
    print row[0]

db.close()