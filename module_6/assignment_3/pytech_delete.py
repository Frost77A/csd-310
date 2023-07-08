""" 
    Title: pytech_delete.py
    Author: Amro Taha
    Date: 25 June 2023
    Description: Test program for delete documents from the pytech collection
"""

import pymongo

# Connect to the Pytech database
client = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0.g9e2son.mongodb.net/")
db = client["Pytech"]
students = db["students"]

# Find all documents in the students collection
results = students.find()

# Print the documents to the terminal window
for result in results:
    print(result)

# Insert a new document into the pytech collection with student_id 1010
new_student = {
    "student_id": 1010,
    "first_name": "John",
    "last_name": "Doe",
    "email": "john.doe@pytech.edu",
    "gender": "Male",
    "date_of_birth": "1990-01-01",
    "_class": "Freshman",
}
students.insert_one(new_student)

# Find the document with student_id 1010
found_student = students.find_one({"student_id": 1010})

# Print the document to the terminal window
print(found_student)

# Delete the document with student_id 1010
students.delete_one({"student_id": 1010})

# Find all documents in the students collection again
results = students.find()

# Print the documents to the terminal window
for result in results:
    print(result)
