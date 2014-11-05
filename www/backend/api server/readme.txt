# How to start an api server instance.
These  instructions work on the OS X 10.10 (Yosemite) and can differ from other operating systems.

For a list of available options type

	python stalkerAPI.py -h

## Only one instance of the API server (Use port 8000)

1. Start an api server instance typing the following command

	python stalkerAPI.py -H localhost -P 8000 -r

## When using HAProxy

1. Start an api server instance typing the following command

	python stalkerAPI.py -H localhost -P 5000

2. Repeat step 1 for the other ports when using the HAProxy server. (5000, 5001, 5002)
