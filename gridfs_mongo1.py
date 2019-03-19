from pymongo import MongoClient
from gridfs import GridFS
from bson import objectid

conn=MongoClient('mongodb://pavanip:pavanip@192.168.1.159', 27017)
db=conn.vistaar_de
fs=GridFS(db)
fs.list()
fs.put(open('test.pdf','rb'),filename='01 - Intro')