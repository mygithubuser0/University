import os
from dotenv import load_dotenv
import pymongo
from pymongo import MongoClient
import json
import asyncio
import base64
from student import student

# harel = student("Harel Choen", 123, 22, "05400000", "harel@mail.com")
# student("David Choen", 1234, 55555, "105400000", "David@mail.com")
# david = student("David Choen", 1234, 32, "105400000", "David@mail.com")

# harel.add_grade(100)
# harel.add_grade(98)
#harel.get_average()

# harel.add_grade(96)
# harel.add_grade(90)
#harel.get_average()






# pylint: disable=E0001

# vali = { 
#    validator: { '$jsonSchema': { 
#       bsonType: "object", 
#       required: [ "name", "surname", "email" ], 
#       properties: { 
#          name: { 
#             bsonType: "string", 
#             description: "required and must be a string" }, 
#          surname: { 
#             bsonType: "string", 
#             description: "required and must be a string" }, 
#          email: { 
#             bsonType: "string", 
#             pattern: "^.+\@.+$", 
#             description: "required and must be a valid email address" }, 
#          year_of_birth: { 
#             bsonType: "int", 
#             minimum: 1900, 
#             maximum: 2018,
#             description: "the value must be in the range 1900-2018" }, 
#          gender: { 
#             enum: [ "M", "F" ], 
#             description: "can be only M or F" } 
#       }
#    }
# }}


# validator = {
#     'validator' : {
#         '$jsonSchema' : {
#             'bsonType' : "object",
#             'additonalProperties' : 'false',
#             'required' : ["name"],
#             'properties' : {
#                 'name' : {
#                     'bsonType': "string",
#                     'description': "Name is required"
#                 },
#                 'age': {
#                     'bsonType': "int",
#                     'description': "Your age"
#                 },
#                 'prof': {
#                     'bsonType': ["array"],
#                     'minItems': 1,
#                     'additonalProperties': 'false',
#                     'description': "The student professions",
#                     'properties': {
#                         "name": {
#                             'bsonType': "string",
#                             'description': "The name of professions"
#                         },
#                         "grade": {
#                             'bsonType': "int",
#                             'minimum': 0,
#                             'maximum': 100,
#                             'description': "The studet grade"
#                         }
#                     }
#                 }
#             }
#         }
#     }    
# }

# schema = json.dumps(validator)
#print(schema)




# async def get_name(name):
#     # if collection.find_one({ "professions.name": name}) !=None:
#     #     return True
#     # else:
#     #     return False
#     return collection.find({ "professions.name": name})

# person = {
#     "name": "Asaf",
#     "email": "AAA@email.com",
#     "age": 16,
#     "professions" : [
#         {"name" : "Bio", "grade" : 90},
#         {"name" : "Com", "grade" : 90}
#     ]
# }

# person2 = {
#     "name": "David",
#     "email": "bbb@email.com",
#     "age": 17,
#     "professions" : [
#         {"name" : "Bio", "grade" : 90},
#         {"name" : "Com", "grade" : 90}
#     ]
# }

# person3 = {
#     "name": "Roi",
#     "email": "ccc@email.com",
#     "age": 17,
#     "professions" : [
#         {"name" : "Math", "grade" : 90},
#         {"name" : "Car", "grade" : 90}
#     ]
# }


# with open("image.jpg", "rb") as imageFile:
#     str_image = base64.b64encode(imageFile.read())


# person4 = {
#     "name": "Itamar",
#     "email": "III@email.com",
#     "age": 17,
#     "professions" : [
#         {"name" : "Math", "grade" : 90},
#         {"name" : "Car", "grade" : 90}
#     ],
#     "Image": str_image
# }



#print(inserted.inserted_id)
# result = asyncio.run(get_name("Bio"))
# for i in result:
    # print(i)
