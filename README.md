# Dynamic-web-content

Requirements:

Make sure python 3.5 installed on your system

Steps:

1. run install.sh file
    - it will install all dependancy as well as creates virtual env.
    - it will create a database

2. Activate virtual environment
    - pipenv shell

3. find a manage.py file and run following commands.

    - python manage.py makemigrations api
    - python manage.py migrate
    - python manage.py runserver
    
# Api info

1.register a new user
  - api/v1/account/register
  Example payload:
    {
    "username":["This field is required."],
    "email":["This field is required."],
    "password":["This field is required."],
    "confirm_password":["This field is required."]
    }
    
2. Login
  - api/v1/account/login
  Example payload:
    {
    "email":["This field is required."],
    "password":["This field is required."]
    }
    
   - In response it will return a Token, we need to pass this token for upcomming request.
       
3. Dynamic add a pic and text for list of hotels stored on db.
    - api/v1/hotel
   Example payload:
   {
   "name":["This field is required."],
   "address":["This field is required."],
   "images":["No file was submitted."]
   }
