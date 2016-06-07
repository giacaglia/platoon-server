## Installing Locally

Make sure you have Python [installed properly](http://install.python-guide.org).  Also, install the [Heroku Toolbelt](https://toolbelt.heroku.com/) and [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup) and [Redis](https://realpython.com/blog/python/flask-by-example-part-1-project-setup/).

```sh
$ pip install virtualenv

$ virtualenv venv

$ source venv/bin/activate

$ pip install -r requirements.txt

$ createdb python_getting_started

$ python manage.py migrate
$ python manage.py collectstatic

$ brew install redis
$ heroku local
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Running app

Run this in 3 different terminal windows:

```sh
$ redis-server
```

```sh
$ python worker.py
```

```sh
$ python manage.py runserver
```

## Deploying to Heroku

```sh
$ git push heroku master

$ heroku run python manage.py migrate
$ heroku open
```
