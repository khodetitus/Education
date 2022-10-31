// 1.got to path mongodb.conf with bottom command:
sudo micro /etc/mongodb.conf

// 2.uncomment replication

// 3.write command under with scoop:
  replSetName: choose_name

// 4.reset seystem:
sudo systemctl restart mongodb

// 5.call function initiate:
rs.initiate()

// 6.show information data:
rs.status()

