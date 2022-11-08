// 1.Embedded data model design:
// db.collection_name.insert({key1:value1,key2:value2,key3:{key4:value4,key5:value5}})
db.users.insert({name:"masoud",age:25,contact:{phone:0912,fax:456}})
// call data in embedded data model design:
// db.collection_name.find(<query>,<filter>)      --->filter:"key3.key4":1 or 0
db.users.find("",{name:1,"contact.phone":1})

// 2.Normalized data model design:
1.db.createCollection("users")
2.db.createCollection("contact")
3.db.users.insert({name:"akbar",age:25,id:2663})
4.db.users.insert({name:"kimiya",age:23})
5.copy _id,my choose users
6.db.contact.insert({phone:4567,fax:982,user_id:"2662"})

// 3.$lookUP aggregation:
// {
//     $lookUP:{
//         from:<collection to join>,
//         localField:<field form the input documents>,
//         foreginFiled:<field from the documents of the "from" collection>,
//         as:<output array field>
//     }
// }
// ex:
db.users.aggregate([{
    $lookup:{
        from:"contact",
        localField:"id",
        foreignField:"user_id",
        as:"contacts"
    }
}])
