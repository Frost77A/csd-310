import pymongo
from pymongo import MongoClient
client = MongoClient("mongodb+srv://admin:admin@cluster0.rluwz.mongodb.net/?retryWrites=true&w=majority")
db = client["pytech"]
collection = db["students"]
#
#################################################### pytech_update
################################################### uncomment update, updatevalue and collection lines
#update = {"First Name": "Test"}
#print(update)
#updatevalue = {"$set": {"First Name" : "Data"}}
#print(updatevalue)
#collection.update_one(update,updatevalue)
