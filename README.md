# Simple blog using Django and Jinja templating

Blog site allows you to create and edit articles. The user can register on the site and create, edit, read,
or delete articles. Unregistered user can only read articles. Also, you can register as superuser and
manage the site by the admin panel. The app is written in Python using 
Django and Jinja templating.

## Features

| Feature                          | Supported          |
|:---------------------------------|:-------------------|
| Simple blog site                 | :white_check_mark: |
| CRUD for articles                | :white_check_mark: |
| Endpoints for filtering articles | :white_check_mark: | 
| Forms for user registration      | :white_check_mark: |     
| Tested Python version            | 3.10               |
| Tested Django version            | 4.0.4              |



## The app supports operations

Endpoints:
+ GET http://127.0.0.1:8000/ - view home page
+ GET /post/<int:post_id>/ - view detail article's information
+ GET /category/<int:cat_id>/ - filtering articles by category
+ GET /about/ - get about page where you can find information about site
+ POST /add/ - you can add new article (if you sing in)
+ POST /feedback/ - you can write a letter to site admins
+ POST /sign_up/ - registration
+ POST /sign_in/ - sign in
+ POST /logout/ - logout


Tools used during development: black, flake8