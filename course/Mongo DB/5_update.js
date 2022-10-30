// 1.db.collection_name.updateOne(<filter>,<update>,<options>)

// operators update:
// 1.set:
db.users.updateOne({name:"masoud"},{$set:{age:27}})

// 2.rename:
db.users.updateOne({name:"masoud"},{$rename:{"contact.phone":"contact.mobile"}})

// 3.unset:
db.users.updateOne({name:"masoud"},{$unset:{age:27}})

// 4.currentDate:
db.users.updateOne({name:"erfan"},{$currentDate:{created:{$type:"date"}}})

// options:
db.users.updateOne({name:"iman"},{$set:{age:26}},{upsert:true})

// -------------------------------------------------------------------------------------------------------------
// 2.db.collection_name.updateMany(<filter>,<update>,<options>)

// -------------------------------------------------------------------------------------------------------------
// 3.db.collection_name.replaceOne(<filter>,<replacement>,<options>)

db.users.replaceOne(
     {name:"erfan"},
     {name:"anna",age:98}
);
