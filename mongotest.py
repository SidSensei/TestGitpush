import pymongo

client = pymongo.MongoClient("mongodb+srv://siddharthadeb:9755408244@cluster-sid01.ylcne.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)

d = {
    "name" : "siddhartha",
    "email":"siddharthadeb92@gmil.com",
    "surname" : "deb"
}
d = {
    "name" : "siddhartha",
    "email":"siddharthadeb92@gmil.com",
    "surname" : "deb"
}
d = {
    "name" : "siddhartha",
    "email":"siddharthadeb92@gmil.com",
    "surname" : "deb"
}

db1 = client['mongotest']
#collection
coll = db1['test']
#insert dictionary
coll.insert_one(d)