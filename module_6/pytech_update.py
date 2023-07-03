import pymongo
from pymongo import MongoClient

# Connect to the MongoDB server
client = MongoClient("mongodb+srv://admin:admin@cluster0.g9e2son.mongodb.net/")

# Access the pytech database
db = client.pytech

# Access the students collection
students = db.students

# Call the find() method and output the documents
print("Before Update:")
cursor = students.find({})
for student in cursor:
    print(student)

# Update the last name of student_id 1007
students.update_one(
    {"student_id": 1007},
    {"$set": {"last_name": "NewLastName"}}
)

# Find and output the updated document
print("\nAfter Update:")
updated_student = students.find_one({"student_id": 1007})
print(updated_student)
