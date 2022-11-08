// 1.remove data base:
db.dropDatabase()

// 2.skip() cursor method:
// db.collection_name.find().skip(number)
db.users.find().skip(10).limit(2)

// 3.oprator $all special operator for array:
// db.collection_name.find({"key1.key2":{$all:[value1,value2,....]}})
db.users.find({"contact.phone":{$all:[912,921]}})

// 4.logical operator $and for conditional:
// db.collection_name.find({$and:[{condition1},{conditon2},...]})
db.users.find({$and:[{name:"masoud"},{age:25}]})

// 5.show the index:
// db.collection_name.getIndexes()
db.users.getIndexes()

// 6.loading queries in js files:
mongo < file_name.js
