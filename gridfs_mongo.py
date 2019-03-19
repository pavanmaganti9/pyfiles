from pymongo import MongoClient
from gridfs import GridFS
from bson import objectid

client = MongoClient('mongodb://pavanip:pavanip@192.168.1.159', 27017)

# Get the sampleDB database
db = client.vistaar_de

#just to make sure we aren't crazy, check the filesize on disk:
#print os.path.getsize( r'1.docx' )

fs = GridFS(db)

#add the file to GridFS, per the pymongo documentation: http://api.mongodb.org/python/current/examples/gridfs.html
#db = MongoClient().myDB
#fs = gridfs.GridFS( db )
with open('test.pdf','rb') as f:
	invoice = fs.put(f, content_type='application/pdf', filename='test-invoice.pdf')
#fileID = fs.put( open( r'1.docx', 'rb')  )
#out = fs.get(fileID)
#print out.length
client.close()