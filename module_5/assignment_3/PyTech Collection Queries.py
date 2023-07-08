""" 
    Title: pytech_queries.py
    Author: Amro Taha
    Date: 19 June 2023
    Description: Test program for querying the students collection.
"""
# PyTech: Collection Queries
from pymongo import MongoClient

# Connect to the MongoDB server
client = MongoClient ("mongodb+srv://admin:admin@cluster0.g9e2son.mongodb.net/")

# Access the pytech database
db = client.pytech

# Access the students collection
students = db.students

# Rest of the code for inserting and querying documents
# ...

from pymongo import MongoClient

# Connect to the MongoDB server
client = MongoClient("mongodb+srv://admin:admin@cluster0.g9e2son.mongodb.net/")

# Access the pytech database
db = client.pytech

# Access the students collection
students = db.students

# Create three new student documents
student1 = {
    "student_id": 1007,
    "first_name": "John",
    "last_name": "Doe"
}

student2 = {
    "student_id": 1008,
    "first_name": "Jane",
    "last_name": "Smith"
}

student3 = {
    "student_id": 1009,
    "first_name": "Michael",
    "last_name": "Johnson"
}

# Insert the new student documents
student1_id = students.insert_one(student1).inserted_id
student2_id = students.insert_one(student2).inserted_id
student3_id = students.insert_one(student3).inserted_id

# Display the returned student IDs
print("Inserted student IDs:")
print(student1_id)
print(student2_id)
print(student3_id)

from pymongo import MongoClient

# Connect to the MongoDB server
client = MongoClient("mongodb+srv://admin:admin@cluster0.g9e2son.mongodb.net/")

# Access the pytech database
db = client.pytech

# Access the students collection
students = db.students

# Display all documents in the collection
print("All documents in the collection:")
docs = students.find({})
for doc in docs:
    print(doc)

# Display a single document by student ID
print("\nSingle document by student ID:")
student_id = 1007
doc = students.find_one({"student_id": student_id})
print(doc)
