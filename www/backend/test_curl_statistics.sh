#!/bin/bash
clear
# Set the default url 
API=http://localhost:5000/statistics

echo -e "\n --- BEGIN --- \n"

echo -e "Testing the $API paths\n"

echo -e " --- TEST #1 /location/frequncy--- \n"

curl -s -X GET $API/location/frequency 

echo -e "\n\n --- TEST #2 /relationship/frequency  --- \n"

curl -s -X GET $API/relationship/frequency 

echo -e "\n\n --- TEST #3 /gender/relationship/frequency/male --- \n"

curl -s -X GET $API/gender/relationship/frequency/male 

echo -e "\n\n --- TEST #4 gender/relationship/frequency/female --- \n"

curl -s -X GET $API/gender/relationship/frequency/female 

echo -e "\n\n --- TEST #5 gender/location/frequency/ --- \n"

curl -s -X GET $API/gender/location/frequency

echo -e "\n\n --- END --- "
