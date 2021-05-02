# Hotel Check-in
This project build for NIIT University's Capstone Project

This is a CRUD operation based Hotel Check-in which wil help the user to Create record of the customer entering or exiting from a hotel, Retrieve the data from the database, Update or make anychanges to it & can Delete it from the database. 

## Prerequisites of the system
The system should have the following things installed:
- Python
- pip
- Any text/code editor 

#### To check if they are installed in the system you can use the following commands:

- To check for python:
```
python --version
```
- To check for pip:
```
pip --version
```
If they are installed in your system, the current version of theirs will be shown. In case, any of the above mentioned things is not there, it is adviced to install it first.  

## Prerequisites
- Python 3.6 
- Django
- SQLite DB
- HTML
- CSS
- Bootstrap

## How to run
To get the app running:

- Creation of a virtual environments done by executing the command venv:
``` 
$ python3 -m venv env/
```
- Activate the virtual environment:
```
env/Scripts/activate
```
- Install django:
```
pip install django
```
- Open VS Code or any text editor
- Start a project:
```
django-admin startproject <name of your project>
```
- Go to the folder:
```
cd <name of the project>
```
- Make an app as per your requiremnt:
```
python manage.py startapp <name of the app or folder>
```
- Create your application by editing the files in the folder like views.py, models.py, urls.py etc. You can also create your own files or templates.

- Finally run the app:
```
python manage.py runserver
```
Copy the link http://127.0.0.1:8000/ and paste it on your browser's address bar. The website will run on that url.
