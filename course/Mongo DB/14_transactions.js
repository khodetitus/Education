// 1.create start function for transaction with js language:
let session = db.getMongo().startSession()

// 2.start transaction:
session.startTransaction()

// 3.create database and create collection with transaction:
let users = session.getDatabase("blog").getCollection("users")

// 4.create document with transaction:
users.insert({name:"jane",age:32})

// 5.commit transaction:
session.commitTransaction()

// 6.stop transaction:
session.abortTransaction()
