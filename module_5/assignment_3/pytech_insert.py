import pymongo
from pymongo import MongoClient
client = MongoClient("mongodb+srv://admin:admin@cluster0.rluwz.mongodb.net/?retryWrites=true&w=majority")
db = client["pytech"]
collection = db["students"]

################################################### pytech_insert
################################################### uncomment the post lines and the collection
#post1 = {"_id": 1010, "First Name": "Justin", "Last Name": "Change"}
#post2 = {"_id": 1011, "First Name": "Christian", "Last Name": "Pulisic"}
#post = {"_id": 1013, "First Name": "Test", "Last Name": "Data"}
#collection.insert_many([post1, post2, post3])