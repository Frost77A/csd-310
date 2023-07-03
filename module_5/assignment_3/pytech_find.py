import pymongo
from pymongo import MongoClient
client = MongoClient("mongodb+srv://admin:admin@cluster0.rluwz.mongodb.net/?retryWrites=true&w=majority")
db = client["pytech"]
collection = db["students"]
#
#################################################### FINDING A STUDENT
################################################### uncomment the find and print lines
#find_one = {"_id": 1010}
#print (find_one)
#results = collection.find_one({"_id": 1010})
#print(results)

