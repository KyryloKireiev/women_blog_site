# Simple blog with Python, Django and Jinja templating

Clone project from https://github.com/KyryloKireiev/women_blog_site

To use blog site you need to install Python 3.10 or higher.

Install all requirements:
+ use command: "pip install -r requirements.txt" in the root directory of the project
+ also, you can use Make commands. Use command: ```make requirements```

Create a database:
+ use command: ```python manage.py migrate``` 
+ you need to enter the commands in the directory /coolsite/, where manage.py is
+ also, you can use Make command: ```make db``` in the root directory of the project

To start server:
+ use command: "python manage.py runserver"
+ or use Make command ```make run```
+ server starts on the local host: "http://127.0.0.1:8000/"

Makefile commands:
+ ```make help``` - get all Makefile commands
+ ```make run``` - to start server
+ ```make mdb``` - to make migrations
+ ```make db``` - to migrate
+ ```make shell``` - enter Django app shell

You can see all endpoints of project in README.md in the root directory of the project

You can use blog with admin panel:
+ go to "http://127.0.0.1:8000/admin"
+ to use admin panel you need to create superuser  
+ you can create new superuser with command "python manage.py createsuperuser"
  or in admin panel, if you already have superuser.
