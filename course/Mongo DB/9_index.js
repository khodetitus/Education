// 1.create indexes collection:
// db.collection_name.createIndex({key:1 or -1})
db.users.createIndex({user_id:1})

// 2.remove indexes collection:
// db.collection_name.dropIndex({key:1 or -1})
db.users.dropIndex({user_id:1})
