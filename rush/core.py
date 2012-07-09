# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request, Response, redirect, url_for

from flask_heroku import Heroku
from flask_sslify import SSLify
from raven.contrib.flask import Sentry
from flask.ext.celery import Celery

from .data import table
from .cnam import phone

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

def update_number(number):
    namespace = 'numbers:{0}'.format(number)

    p = phone(number)
    table[namespace]['number'] = p.number or None
    table[namespace]['cnam'] = p.cnam or None



@app.route('/numbers/<number>')
def number_info(number):

    # Sanity check.
    if len(number) != 10:
        return 'Invalid length.', 400

    namespace = 'numbers:{0}'.format(number)
    t = table[namespace]
    if (not t.get('cnam')) or 'force' in request.args:
        t = update_number(number)
        return redirect(url_for('number_info', number=number))

    else:

        return jsonify(t)


def area_code():
    pass

def area_exchange():
    pass

@app.route('/normalize')
def normalize_number():
    p = phone(request.args.get('number'))

    if p:
        return redirect(url_for('number_info', number=p.number))
    else:
        return '', 404
