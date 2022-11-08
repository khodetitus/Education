// 1.install tools for backup and restore in mongodb:
yay -S mongodb_tools

// 2.get backup in all databases
mongodump
// limit databases:
mongodump -d database_name

// 3.restore in path directory dump:
mongorestore
