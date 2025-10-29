## Django

Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.

### Creating a project

```bash
django-admin startproject mysite djangotutorial
```

after running this command, you will get a project structure in the following manner

```bash
djangotutorial/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```

`manage.py` - is the file that lets you manage your server like running the server or creating new app, super users and other desired tasks
`mysite/` - This is the main python package of your project.
`mysite/settings.py` - Settings/configuration for this Django project
`mysite/urls.py`- The URL declarations for this Django project;

> Now, inorder to run your application use the command `python manage.py runserver`

### Our project Relevance

in our project we have improved the project code maintainence by dividing the code into two types of folders.

- `recommendation_server` - which is like the main server which will be handling apis like recommend me my next anime
- `crud_server` - which the server which will be handling CRUD apis.

<!-- TODO(ADHEESH): HOW ROUTING WAS MANAGED -->

### DATABASE SETUP

the database used in our project is sqlite and now our main task is to create the database modeling for the project.

<!-- TODO(ADHEESH): COMPLETE THE DATABASE SETUP STEPS -->

### Creating the database Models

so now when we were creating users, in python these models are usually class based modelings and inorder for us to do them we created a class named `User`

The user class has various fields inside of it and the following properties can be provided to the charField data and this is what it means.

- `max_length` - the maximum length that attribute can contain
- `unique` - no duplicated
- `editable` - once the value is set then it cannot be changed further
- `db_index` - creating a database index for faster reads
- `default` - to set a default value

for dateTime field

- `auto_now` - whenever the user row is changed or updated automatically the last update time is recorded using this function
- `auto_now_add` - just like `auto_now` but runs only once when we initialize the row

For enumerations in django models, we use a function called `RegexValidator` using which we will be able to rank the users based on their ratings

- `choices` - is the field that helps us to define an enumeration
