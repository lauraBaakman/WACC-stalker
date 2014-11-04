# How to run MongoDB
These  instructions work on the OS X 10.10 (Yosemite) and can differ from other operating systems.

## Single instance

1. Start a new process on port 27017 (which is the default) by entering the following command

	mongod --port 27017

## Multiple instances (Replica set)

1. Start three mongod processes with the following commands. In order to change the location of the databases, change the part behind --dbpath <custom path>. The name of the replica set can't be changed without changing the code of the api server, so it is best to leave this to be the preset value.

	mongod --port 27017 --dbpath /data/db/replicas/db1 --replSet rs_wacc --smallfiles --oplogSize 128

	mongod --port 27018 --dbpath /data/db/replicas/db2 --replSet rs_wacc --smallfiles --oplogSize 128 

	mongod --port 27019 --dbpath /data/db/replicas/db3 --replSet rs_wacc --smallfiles --oplogSize 128

2. We now need to initiate the replica set. Open a new terminal and type the following command to open a connection with one of the mongod instances (This case 27017, but it doesn't matter which one of the three you choose).

	mongo --port 27017

3. Initiate the replica set with the following command.

	rs.initiate()

4. Look at the "me" field for the host and add the host followed by the ports of the other two instances between quotes using the following commands.

	rs.add("host:27018")
	rs.add("host:27019")

5. The replica set is now up and running. You can now exit the connection with the mongod instance

	quit()

6. Done
