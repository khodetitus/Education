// set schema validator:
// db.createCollection("name_collection",<option>)

// 1.first option in create collection is validator,validate with json schema:
// db.createCollection("name_collection",validator:$jsonSchema:<document>)
// ex:
db.createCollection("users", {
    validator: {
        $jsonSchema: {
            required:["name","age"],
            properties: {
                name: {
                    bsonType:"string",
                    description:"must be a string and is required",
                },
                age: {
                    bsonType:"double",
                    minimum:0,
                    maximum:99,
                    description:"must be a integer and is required",
                },
                married:{
                    enum:["yes","no"],
                    description:"must be yes or no",
                }
            }
        }
    }

})

// 2.show information collections:
// db.getCollectionInfos(<query>)
// ex:
db.getCollectionInfos({name:"users"})

// 3.create a new data:
1.db.users.insert({name:"masoud",age:NumberInt(25)})
2.db.users.insert({name:"kimiya",age:NumberInt(23),married:"yes"})

// 4.second option in create collection is validationAction:
db.createCollection("users", {
    validator: {
        $jsonSchema: {
            required:["name","age"],
            properties: {
                name: {
                    bsonType:"string",
                    description:"must be a string and is required",
                },
                age: {
                    bsonType:"double",
                    minimum:0,
                    maximum:99,
                    description:"must be a integer and is required",
                },
                married:{
                    enum:["yes","no"],
                    description:"must be yes or no",
                }
            }
        }
    },
    validationAction: "warn",
})

// 5.path log files:
// 1.sudo su -
// 2.cat /etc/mongodb.config
// 3.go to systemLog
// 4.copy path
// 5.cd to path or /var/log/mongodb/
// 6.cat mongod.log


