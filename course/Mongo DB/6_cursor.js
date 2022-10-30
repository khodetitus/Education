// cursor method:
// 1.count()
// cursor.count()
// ex:
db.users.find().count()

// 2.limit()
// cursor.limit()
// ex:
db.users.find().limit(2)

// 3.pretty()
// cursor.pretty()
// ex:
db.users.find().pretty()

// 4.explain()
// cursor.explain()
// ex:
db.users.find().explain()

// 5.map()
// cursor.map(function)
// ex:
db.users.find().map(function(input){return input.age})

// 6.toArray()
// cursor.toArray()
// ex:
db.users.find().toArray()

// 7.sort()
// cursor.sort(filter)
// ex:
db.users.find().sort({age:1 or -1})

