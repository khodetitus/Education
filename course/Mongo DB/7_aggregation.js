load("/home/khodetitus/PycharmProjects/pythonProject/Education/course/Mongo DB/7 test files.js")
// aggregation operation:
// db.collection_name.aggregate([{<stage>}, ...],<option>)
// 1.$match:
db.users.aggregate([{$match:{country:"spain"}}],{allowDiskUse:true})
db.users.aggregate([{$match:{age:{$gt:30}}}])

// 2.$project:
db.users.aggregate([{$project:{name:1,country:1,-id:0}}])

// 3.$group:
// db.collection_name.aggregate([{$group:{_id:"$key",field:1 or 0}}])
db.users.aggregate([{$group:{_id:"$country"}}])
// fields group:
// 1.$sum:
// db.collection_name.aggregate([{$group:{_id:"$key",field_name:{$sum:1 or 0}}])
db.users.aggregate([{$group:{_id:"$country",total:{$sum:1}}])

// 4.$sort:
// db.collection_name.aggregate([{$sort:{field:1 or -1}}])
db.users.aggregate([{$sort:{age:1}}])

// 5.$limit:
// db.collection_name.aggregate([{$limit:choose number}])
db.users.aggregate([{$limit:30}])

// 6.$set:
// db.collection_name.aggregate([{$set:{newkey:newvalue}}])
db.users.aggregate([{$set:{email:"masoudpro2@gmail.com"}}])

// 7.$addFields:
// db.collection_name.aggregate([{$addFields:{newkey:newvalue}}])
db.users.aggregate([{$addFields:{email:"masoudpro2@gmail.com"}}])

// 8.$unset:
// db.collection_name.aggregate([{$unset:{key:value}}])
db.users.aggregate([{$unset:{email:"masoudpro2@gmail.com"}}])


