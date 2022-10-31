from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.blog
collection = db.users
user1 = {
    "name": "masoud",
    "age": 25
}
collection.insert_one(user1)
# print(collection.find_one())

user2 = {
    "name": "kimiya",
    "age": 25}

id_user2 = collection.insert_one(user2).inserted_id
# print(id_user2)
data = collection.find()
print(list(data))
