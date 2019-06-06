# Time Tracker

A time tracking application that allows a user to save times from an online stopwatch.
The user may also be able to edit their descriptions. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

The user will need the following python packages installed from PIP to run the project
```
Django==2.2.2
pytz==2019.1
sqlparse==0.3.0
```

### Installing
The instructions assume user is using a UNIX-based environment

1. Have Python 3 installed.
Check with the following command 
```
python --version or python3 --version
```

2. Install the packages with the following command using the requirements file
(recommended to install packages to a virtual environment)
```
pip3 install -r requirements.txt
```

3. Create the database for usage with application
```
python3 manage.py migrate
```

4. Run with the following command
```
python3 manage.py runserver
```

5. Go to the server address Django shows in the console
(eg. http://127.0.0.1:8000/)


## Built With

* [Python](https://www.python.org/) - programming language
* [Django](https://www.djangoproject.com/) - Web Framework
* [sqlite3](https://www.sqlite.org/index.html) - Database
* [Bootstrap](https://getbootstrap.com) - CSS Framework 

* **Karan Joshi** - *Initial work* 

