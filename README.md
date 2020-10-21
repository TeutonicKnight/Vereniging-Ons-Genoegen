Commands used:
$ export PYTHONPATH= | Clear python path, apparantly this is important for the venv
$ virtualenv virtual | Create cirtual env, note sure what difference is between python -m ...
$ python -i | Start python interpreter on Git Bash
$ import secrets | import secret module into python interpreter
$ secrets-token_hex(16) | create random hexadecimal dumber for SECRET_KEY

start psql:
# create database wordcount_dev;

$ python -m pip install psycopg2==2.8.4 Flask-SQLAlchemy===2.4.1 Flask-Migrate==2.5.2
$ python -m pip install Flask-Script==2.0.6
$ python manage.py db init
$ python manage.py db migrate
$ python manage.py db upgrade

Things learned:
$ export PYTHONPATH= clears python path which matters for the venv apparantly. Now pip freeze works as intended.

Sublime text: Use cntrl + d to highlight next instance of same word and create multiple cursor for it.
Very handy for editing multiple instances of a word.

Import module from a directory which is exactly one level above the current directory: from .. import module
(use dots to specifiy number of directories above)

Never run your website in debug mode when you are running it for production. The debug mode gives away too much
info when it catches an error. If someone has the Debug pin he could figure out emails and such.

Gebleven bij ?? 7:42? Wat wil ik hier van gebruiken? https://www.youtube.com/watch?v=803Ei2Sq-Zs