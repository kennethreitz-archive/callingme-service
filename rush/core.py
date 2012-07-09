# -*- coding: utf-8 -*-

from flask import Flask
from flask_heroku import Heroku
from flask_sslify import SSLify
from raven.contrib.flask import Sentry
from flask.ext.celery import Celery

from .data import table

app = Flask(__name__)

heroku = Heroku(app)
sentry = Sentry(app)
sslify = SSLify(app)
celery = Celery(app)

app.debug = True

@app.route('/')
def describe_api():
    """Returns a description of the API."""
    return 'yay!'

@app.route('/numbers/<number>')
