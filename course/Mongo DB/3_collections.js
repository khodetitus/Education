// 1.remove a collection:
// db.collection_name.drop()
db.users.drop()
//--------------------------------------------------------------------------------------------
// 2.create a collcction:
// db.createCollection("name",option)
// 1.size option:
db.createCollection("users",{size:12})

// 2.max option:
db.createCollection("users",{max:2})

// 3.capped option:
db.createCollection("users",{capped:true})

// 4.expireAfterSeconds option:
db.createCollection("users",{expireAfterSeconds:true}
// -------------------------------------------------------------------------------------------
// 3.count method:
// db.collection_name.count()
db.users.count()
// -------------------------------------------------------------------------------------------
// 4.dataSize method:
// db.collection_name.dataSize()
db.users.dataSize()
// -------------------------------------------------------------------------------------------
// 5.isCapped method:
// db.collection_name.isCapped()
db.users.isCapped()
// -------------------------------------------------------------------------------------------
// 6.insertOne mehtod(create a document):
// db.collection_name.insertOne({key:value})
db.users.insertOne({name:"masoud"})
// -------------------------------------------------------------------------------------------
// 7.insertMany mehtod(create many documents):
// db.collection_name.insertMany({key1:value1},{key2:value2},...)
db.users.insertOne({name:"kimiya"},{name:"soheil"})
// -------------------------------------------------------------------------------------------
// 8.deleteOne method(delete a document):
// db.collection_name.deleteOne({key:value})
db.users.deleteOne({name:"masoud"})
// -------------------------------------------------------------------------------------------
// 9.deleteMany method(delete many documents):
// db.collection_name.deleteMany({key1:value1},{key2:value2},...)
db.users.deleteMany({name:"kimiya"},{name:"soheil"})
// -------------------------------------------------------------------------------------------
 // 10.remove method(remove one and  many documents):
// db.collection_name.remove({key1:value1},boolean)
db.users.remove({name:"kimiya"},true)
