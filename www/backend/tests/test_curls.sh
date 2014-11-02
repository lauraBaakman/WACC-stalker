#!/bin/bash
# API test script

# Dependencies (MAC):
#  brew install jsawk && brew install jsonpp

# Dependencies (NOT MAC):
#  - No idea probably the same ;-)

clear

# Set the default url 
API=http://localhost:8000

echo -e "Checking for a clean slate. Everything should be empty. \n"
# GET all the searches (Should return an array)
curl -s -X GET $API/searches | jsawk -a 'if(this.length != 0) { return this; } else { return "Searches is empty"; }'

# GET all stalkers
curl -s -X GET $API/stalkers | jsawk -a 'if(this.length != 0) { return this; } else { return "Stalkers is empty"; }'

# GET all victims
curl -s -X GET $API/victims | jsawk -a 'if(this.length != 0) { return this; } else { return "Victims is empty"; }'

echo -e "\nThe first thing that should happen: The user signing in with his Facebook account. Here we can create a new stalker.\n"

echo -e 'INPUT:\n{"stalker_id": "0002", "birthdate": "23-03-1990", "gender": "female"}'

# POST a new stalker to the api
echo 'OUTPUT: ' 

curl -s -X POST -H "Content-Type: application/json" -d '{"stalker_id": "0002", "relationship_status": "single", "birthdate": "23-03-1990", "gender": "female"}' $API/stalkers

echo -e "\nAfter a user is signed in this user can use the search field to search. When the search button is clicked we can save the search.\n"

echo -e 'INPUT:\n{"stalker": "0002", "latitude": 50.0, "longitude": 60.0, "country_code": "NED"}'

# POST a new search to the api, this will respond in a message including the id of the search we need to update it.
ID=$(curl -s -X POST -H "Content-Type: application/json" -d '{"stalker_id": "0002", "latitude": 50.0, "longitude": 60.0, "country_code": "NED"}' $API/searches | jsawk 'return this.data;')

echo -e "\nGET on all the data to see what is inserted.\n (victims should still be empty and search should not have a victim_id)"

curl -s -X GET $API/searches | jsawk -a 'if(this.length != 0) { return this; } else { return "Searches is empty"; }' | jsonpp

# GET all stalkers
curl -s -X GET $API/stalkers | jsawk -a 'if(this.length != 0) { return this; } else { return "Stalkers is empty"; }' | jsonpp

# GET all victims
curl -s -X GET $API/victims | jsawk -a 'if(this.length != 0) { return this; } else { return "Victims is empty"; }'

echo -e "\nNow creating a victim and updating the just created search.\n"

echo -e 'INPUT: \n {"victim_id": "0004"}'

echo -e "OUTPUT: "
curl -s -X POST -H "Content-Type: application/json" -d '{"victim_id": "0004"}' $API/victims

echo -e '\nUdating search with INPUT: $ID and {"victim_id":"0004"}'

echo -e "OUTPUT:"

curl -s -X PUT -H "Content-Type: application/json" -d '{"victim_id": "0005"}' $API/search/$ID

echo -e "\nFinal database state: \n"

curl -s -X GET $API/searches | jsawk -a 'if(this.length != 0) { return this; } else { return "Searches is empty"; }' | jsonpp

# GET all stalkers
curl -s -X GET $API/stalkers | jsawk -a 'if(this.length != 0) { return this; } else { return "Stalkers is empty"; }' | jsonpp

# GET all victims
curl -s -X GET $API/victims | jsawk -a 'if(this.length != 0) { return this; } else { return "Victims is empty"; }' | jsonpp
