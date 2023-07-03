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

# Update the last name of the student with student_id 1007 to "Smith"
update_result = students.update_one({"student_id": 1007}, {"$set": {"last_name": "Smith"}})

# Print the updated document to the terminal window
updated_result = students.find_one({"student_id": 1007})
print(updated_result)
