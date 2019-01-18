#!c:/Python27/python
print "Content-type: text/html"
print
import MySQLdb
DEBUG = True
db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="",  # your password
                     db="gold")        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# Use all the SQL you like

def allrecords():
	qry = """SELECT * FROM tbl_banner"""
	cur.execute(qry)
	record = cur.fetchall()
	
	for row in record:
		print "Id: ",row[0], ", BannerName : ",row[1]," <br> "

def myfunc(x):
	
	qry = """SELECT * FROM tbl_banner where bnr_id = %s"""
	cur.execute(qry,(x,))
	record = cur.fetchall()
	
	for row in record:
		print "Id: ",row[0], ", BannerName : ",row[1]," <br> "
		
def records():
	qry = """SELECT * FROM tbl_banner"""
	cur.execute(qry)
	print(cur.rowcount)
	
def limit(x):
	qry = """SELECT * FROM tbl_banner"""
	fetching_size = x
	cur.execute(qry)
	record = cur.fetchmany(fetching_size)
	
	for row in record:
		print "Id: ",row[0], ", BannerName : ",row[1]," <br> "
		
def singerecord():
	qry = """SELECT * FROM tbl_banner ORDER BY bnr_id DESC"""
	cur.execute(qry)
	record = cur.fetchone()
	print (record[1])
	
myfunc(2)
print "<br><br>"
print "No of records - "
records()
print "<br><br>"
allrecords()
print "<br><br>"
limit(2)
print "<br><br>"
singerecord()

db.close()