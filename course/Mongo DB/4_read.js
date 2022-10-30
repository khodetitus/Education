// 1.loaded files mongo command
load("path.js")
// --------------------------------------------------------------------------------------
// 2.db.collection_name.findOne(query,projection)
db.users.findOne({name:"masoud"},{name:true})
// --------------------------------------------------------------------------------------
// 3.filter with operators:
// db.collcction_name.findOne({key:{$opeartor:value}})
// 1.eq operators:
db.users.findOne({age:{$eq:30}})

// 2.gt operators:
db.users.findOne({age:{$gt:30}})

// 3.gte operators:
db.users.findOne({age:{$gte:30}})

// 4.lt operators:
db.users.findOne({age:{$lt:30}})

// 5.lte operators:
db.users.findOne({age:{$lte:30}})

// 6.ne operators:
db.users.findOne({name:{$ne:"masoud"}})

// db.collection_name.findOne({key:{opeartor:[value1,value,2,...]}})
// 7.in operators:
db.users.findOne({name:{$in:["masoud","soheil"]}})

// 8.nin operators:
db.users.findOne({name:{$nin:["masoud","soheil"]}})

// db.collection_name.findOne({$opeartor:[{key1:{$opeartor1:value1}},{key2:{opeartor2:value2}}]})
// 9.or operators:
db.users.findOne({$or: [{name:{$eq:"masoud"}}, {age:{$gt:30}}]})
