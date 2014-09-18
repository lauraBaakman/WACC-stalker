#WACC-stalker
This is the project for the course Web and Cloud Computing.

##Assignment

### Project Description
We have opted to do project 22, which was described as:
>Project 22: Social Media APIs
Use multiple APIs from social media applications to combine information in order to create a global profile of a specific person.
	
### Requirements
The project requirements presented during the first lecture.
####UI
- Single Page Application
- CSS
- AJAX
- server-side events
- future/promise pattern
- modular organization of code
- (at least a small bit of) testing

###Back-end and Database
- A noSQL database must be used or noSQL on top of SQL database.
- Usage of coordination protocol is a plus.

## Technology Stack

### Frontend
- Angularjs
	- Bower?
- Bootstrap
- Require.js?

#### Testing
- Jasmine Angular unit testing 

### Backend
- Python
	- Virtualenv
	- Pip

- [Flask](http://www.flask.pocoo.org)
	- [Flask-PyMongo](http://flask-pymongo.readthedocs.org/en/latest/)
	- [Flask RESTful](http://flask-restful.readthedocs.org/en/latest/)

- [OpenReplica](http://openreplica.org/)

#### Database
- [MongoDB](http://www.mongodb.org/)

#### Testing
- Python Unittest
- Flask RESTful testsuite
- 

# APIs

## Facebook API

### User search
Input:
>search?q="Rick van Veen"&type=user

Output:
>{
  "data": [
    {
      "name": "Rick Van der Veen", 
      "id": "629307900522293"
    }, 
    {
      "name": "Rick van der Veen", 
      "id": "337260969775811"
    }
    ]
}

### General information
Input:
>/user_id

Output:
>{
  "id": "629307900522293", 
  "first_name": "Rick", 
  "last_name": "Van der Veen", 
  "link": "https://www.facebook.com/app_scoped_user_id/629307900522293/", 
  "name": "Rick Van der Veen", 
  "updated_time": "2012-05-23T23:03:02+0000"
}

### Picture
Input:
>user_id/picture?redirect=false

Output:
>{
  "data": {
    "url": "https://fbcdn-profile-a.akamaihd.net/hprofile-ak-xpf1/v/t1.0-1/c15.0.50.50/p50x50/954801_10150002137498316_604636659114323291_n.jpg?oh=7dabc8b1a257f2403ceacdadcd6910e0&oe=5496C2F7&__gda__=1422939042_adda3bd91729fcb6dc6d9e6d7c060a3c", 
    "is_silhouette": true
  }
}
