# Simple blog with Python, Django and Jinja templating

Clone project from https://github.com/KyryloKireiev/women_blog_site

For use blog site you need install Python 3.10 or higher.

Install all requirements:
+ use command: "pip install -r requirements.txt" in the root directory of the project

Create a database:
+ use command: "python manage.py migrate"
+ you need to enter the commands in the directory coolsite, where manage.py is

To start server:
+ use command: "python manage.py runserver"
+ server starts on the local host: "http://127.0.0.1:8000/"

Also, you can use commands from Makefile:
+ "make run" - to start server
+ "make mdb" - to make migrations
+ "make db" - to migrate

You can see all endpoints of project in README.md in the root directory of the project

You can use api with admin panel:
+ go to "http://127.0.0.1:8000/admin"
+ to use admin panel you need to create superuser  
+ you can create new super user with command "python manage.py createsuperuser"
  or in admin panel, if you already have superuser.
