Demo site for learning purposes. Register, login, and join the meeting.

The information below is for myself so I can keep track of the commands and things I learned.

Commands used:
$ export PYTHONPATH= | Clear python path, apparantly this is important for the venv
$ virtualenv virtual | Create virtual env, note sure what difference is between python -m ...
$ python -i | Start python interpreter on Git Bash
$ import secrets | import secret module into python interpreter
$ secrets-token_hex(16) | create random hexadecimal dumber for SECRET_KEY

start psql:
# create database wordcount_dev;
\c DATABASE;
truncate TABLE;

$ python -m pip install psycopg2==2.8.4 Flask-SQLAlchemy===2.4.1 Flask-Migrate==2.5.2
$ python -m pip install Flask-Script==2.0.6
$ python manage.py db init
$ python manage.py db migrate
$ python manage.py db upgrade

$ python -m pip install gunicorn==20.0.4 | Don't forget
$ python -m pip freeze > requirements.txt | Don't forget

$ heroku pg:info | Check postgres version

Pushing local db to remote:
$ export PATH=$PATH:"C:\Program Files\PostgreSQL\12\bin" | Set psql to PATH in order to push local db to remote
---> Pushing local database to remote: https://stackoverflow.com/questions/15576064/the-local-psql-command-could-not-be-located
$ heroku pg:reset postgresql-convex-45291 | Even though my remote db was empty, it prompted me with reset.
  Interesting fact: It seems to re-create constraints and such, so this could be another way to update your remote db,
  not just a requirement for pushing data.
$ PGUSER=postgres PGPASSWORD=password heroku push mylocaldb HEROKU_POSTGRESQL_MAGENTA --app sushi | Push local data to remote.

Things learned:
$ export PYTHONPATH= clears python path which matters for the venv apparantly. Now pip freeze works as intended.

Problem with migration, it didn't find any changes, I added 'from website.models.models import Leden' to the env.py
file in migrations folder. I also had to comment out all the code that had to do with the login manager in models.py
because that started loading the whole code and because I deleted my database, the fields were not yet there so
it threw an error. Related: https://stackoverflow.com/questions/51783300/flask-migrate-no-changes-detected-to-schema-on-first-migration
In the end it had to do with the code in __init__.py where my db was defined. because it is imported from there,
the code in that file runs, and some of it was depended on the db. So i had to comment that code out. To prevent this
it's probably better to separate login_manager and db handling.

Sublime text: Use cntrl + d to highlight next instance of same word and create multiple cursor for it.
Very handy for editing multiple instances of a word.

Import module from a directory which is exactly one level above the current directory: from .. import module
(use dots to specifiy number of directories above)

To query from your db model: SomeModel.query.all(). Use Model.SomeAttribute to access table columns/rows


web: gunicorn app:app The first app represents the name of the python file that runs your application or the 
name of the module it is in. The second app represents the app name that is named in your .py file. 
Just wanted to add because it helps clarify the contents of the procfile and it's syntax. E.g. your 
appname would be my_awesome_app in the following code: if __name__ == '__main__': my_awesome_app.run()

Never run your website in debug mode when you are running it for production. The debug mode gives away too much
info when it catches an error. If someone has the Debug pin he could figure out emails and such.
 
Flask-login extension documentation: https://flask-login.readthedocs.io/en/latest/