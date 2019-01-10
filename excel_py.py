#!c:/Python27/python
print "Content-type: text/html"
print
import MySQLdb
import xlrd

#open the workbook and define the worksheet
book = xlrd.open_workbook("MentorMindWork.xlsx")
sheet = book.sheet_by_name("Sheet1")
#sheet = book.sheet_by_index(0)

#Establish mysql connection
db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="",  # your password
                     db="python")        # name of the data base
#Get cursor, which is used to traverse the database line by line
cursor = db.cursor()
#create insert into sql query
query = """INSERT INTO workbook(date,task) VALUES(%s,%s)"""
#create for loop to iterate through each row in xlsx file starting at row2 to skip headers
for r in range(1, sheet.nrows):
    date = sheet.cell(r,0).value
    task = sheet.cell(r,1).value
    #Assign values  from each row
    values = (date,task)
    #Execute sql query
    cursor.execute(query,values)

#close the cursor
cursor.close()
#commit the transaction
db.commit()
#close db
db.close()
#print results
print ""
print "All Done Pavan!"
print ""
columns = str(sheet.ncols)
rows = str(sheet.nrows)
print "Imported" + columns + "columns and " + rows + "rows"