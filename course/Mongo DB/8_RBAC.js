//1. view users:
show users
// or
db.getUsers()
// -------------------------------------------------------------------------------------------
// 2.view roles database:
show roles
// -------------------------------------------------------------------------------------------
// 3.enable role access control:
// first: create a user:
// db.createUser(
//         {user:"choose username",
//          pwd:"choose password" or passwordPrompt(),
//          roles:[{role:"choose role",db:"choose database"},...]
//
//         }
// )
// ex for head admin:
db.createUser(
        {user:"khodetitus",
         pwd:"Saeid 13766",
         roles:[{role:"userAdminAnyDatabase",db:"admin"}]

        }
)

// ex for member admin:
db.createUser(
        {user:"rezaamin",
         pwd:"akbar1234",
         roles:[{role:"read",db:"blog"}]

        }
)

// second:pwd:open file and scroll down and uncomment security
// sudo micro etc/mongodb.conf

// third:copy and paste bottom text with 2 space,under security:
  authorization: enabled
//
// fourth:restart mongo db with command bottom:
sudo systemctl restart mongodb
//
// fifth:command bottom,for singin your mongodb local:
// mongo -u username -p password
// mongo -u username -p password --authenticationDatabase name_database
// ex for signin head admin:
mongo -u khodetitus -p Saeid 13766

// ex for signin member admin:
mongo -u rezaamin -p akbar1234 --authenticationDatabase shop


// **remove admin:
// db.removeUser("username")
// db.drop("username")
// ex:
db.removeUser("khodetitus")
db.drop("khodetitus")

// **change password admin:
// db.changeUserPassword("username","new password")
ex:
db.changeUserPassword("khodetitus","kimiya 1234")

// **change roles for member admin:
// db.grantRolesToUser("username","roles")
db.grantRolesToUser("khodetitus",[{role:"readwrite",db:"shop"},{role:"read",db:"blog"}])

// **remove roles for member admin:
// db.revokeRolesFromUser("username","roles")
db.revokeRolesFromUser("khodetitus",[{role:"read",db:"blog"}])

