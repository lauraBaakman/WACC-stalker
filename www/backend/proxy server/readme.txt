# How to use HAProxy to load balance the calls to the api server.
These  instructions work on the OS X 10.10 (Yosemite) and can differ from other operating systems.

The default config file expects three api servers running on ports: 5000, 5001, 5002. If you don't change anything in the config file you can safely start with step 2 otherwise 1. 

1. Check the config file by running the following command.

	haproxy -c -f config.conf

2. In order to start the haproxy server run the following command.

	haproxy -f config.conf

3. Done.