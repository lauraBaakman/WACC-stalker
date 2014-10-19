#!/bin/bash
# API test script

clear

api_host=http://localhost:5000

echo -e "Testing GET methods \n"

echo -e "Search Resource: \n"
curl $api_host/search
echo -e "\n"

echo -e "Stalker Resource: \n"
curl $api_host/stalker
echo -e "\n"

echo -e "Victim Resource: \n"
curl $api_host/victim
echo -e "\n"

echo -e "Testing POST methods \n"

echo -e "Search Resource: "

curl -X POST -H "Content-Type: application/json" -d '{"stalker": "0002", "lat": 50.0, "long": 60.0, "victim": "0001"}' $api_host/search

curl $api_host/search

echo -e "\n"

echo -e "Stalker Resource: "

curl -X POST -H "Content-Type: application/json" -d '{"stalker_id": "0002", "relationship_status": "single", "birthdate": "23-03-1990", "gender": "female"}' $api_host/stalker
curl $api_host/stalker

echo -e "\n"

echo -e "Victim Resource: "

curl -X POST -H "Content-Type: application/json" -d '{"victim_id": "0004"}' $api_host/victim

curl $api_host/victim

echo -e "Test PUT Methods"

curl -X PUT -d "stalker_id=0001" $api_host/stalker