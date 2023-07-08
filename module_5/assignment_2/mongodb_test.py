""" 
    Title: mongodb_test.py
    Author: Amro Taha
    Date: 19 June 2023
    Description: Test program for connecting to a 
                 MongoDB Atlas cluster
"""
#mongodb_test.py 

from pymongo import MongoClient

# Get the connection string from MongoDB Atlas
url = "mongodb+srv://admin:admin@cluster0.g9e2son.mongodb.net/"

# Create a MongoClient object
client = MongoClient(url)

# Get the database object
db = client.pytech

# Print the list of collections in the database
print(db.list_collection_names())