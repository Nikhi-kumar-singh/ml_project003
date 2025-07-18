from pymongo import MongoClient

client=MongoClient("localhost",27017)

db=client.college

students=db.students

students.insert_one({
    "name":"manish modanwal",
    "age":23,
    "degree":"B.Tech"    
})

for student in students.find():
    print(student)