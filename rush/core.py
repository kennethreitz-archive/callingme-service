# -*- coding: utf-8 -*-

from flask import Flask, jsonify

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

    descr = {
        'resources': {
            '/numbers/:number': 'Returns data about the given number.',
            '/areas/:area': 'Returns data about a given area code.',
            '/areas/:area/:exchange': 'Returns data about a given exchange.',
            '/normalize?number=:number': 'Returns a normalized Phone number.'
        }
    }
    return jsonify(descr)

@app.route('/numbers/<number>')
def function():
    pass


def area_code():
    pass

def area_exchange():
    pass

def normalize_number():
    pass