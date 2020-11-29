# import asyncio
import pymongo
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

try:
    cluster = MongoClient(os.getenv("CON_STRING")) #Connect MONGO
    cluster.server_info()
    print("Connected!")
except pymongo.errors.OperationFailure as err:
    print("Connection failed")


db = cluster["University"] #Connect to University DB
db.drop_collection("Student")
#db.create_collection("Student")
collection = db["Student"] #Connect to Student collection

collection.create_index("id", unique = True)
collection.create_index("phone number", unique = True)
collection.create_index("email", unique = True)

class student:

    def __init__(self, full_name, id, age, phone_number, email):
        if 0 <= age <= 120:
            self.full_name = full_name
            self.id = id
            self.age = age
            self.phone_number = phone_number
            self.email = email
            # self.profession = profession
            self.add_student()

        else:
            self.exit_class()

    def exit_class(self):
        print("Age out range")

    def add_student(self):
        all_student_data = {
            "_id": collection.count_documents({}) + 1, #return the doc in collection
            "student number": collection.count_documents({"type": "student"}) + 1, #return the student number in collection
            "type": "student",
            "name": self.full_name,
            "id": self.id,
            "age": self.age,
            "phone number": self.phone_number,
            "email": self.email,
            "grades": [],
            "GPA": "No grades"
        }

        try:
            collection.insert_one(all_student_data)
            print("Inserted!")
        except pymongo.errors.DuplicateKeyError:
            print("Duplicated!")

    def add_grade(self, grade):
        collection.update(
            {"id": self.id},
            { "$push": { "grades": grade } }
            )
        print("Add grade: ", grade)
        self.get_average()

    def get_average(self):
        results = collection.find_one({"id": self.id})
        if results != None:
            collection.update_one(
                {"id": self.id},
                {"$set": {"GPA": (sum(results["grades"]) / len(results["grades"]))}}
                )
            print("New GPA is: ", (sum(results["grades"]) / len(results["grades"])))
        else:
            return "No grades"
