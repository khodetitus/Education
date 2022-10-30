//1. view databases:
show dbs
// -------------------------------------------------------------------------------------------
// 2.view active databases:
db
// -------------------------------------------------------------------------------------------
// 3.create and switch a data base:
use dataBase_name
// ex:
use shop
// -------------------------------------------------------------------------------------------
// 4.create a collection:
db.createCollection("name_collection")
// ex:
db.createCollection("users")
// -------------------------------------------------------------------------------------------
// 5.show the collcctions:
show collections
// -------------------------------------------------------------------------------------------
// 6.search and find and make a query:
db.collection_name.find()
// ex:
db.users.find()
// -------------------------------------------------------------------------------------------
// 7.customize the mongosh prompt:

first :
pwd:home/khodetitus/.mongorc.js --->hidden file

second:open with micro or nano and show the empty files

third:copy and paste bottom js code to .mongorc.js file

prompt = function(){
	return db + '> ';
}
// -------------------------------------------------------------------------------------------
