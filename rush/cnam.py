#!/usr/bin/env python
# -*- coding: utf-8 -*-

from re import sub

import env
import requests
import phonenumbers
from phonenumbers.geocoder import description_for_number
from phonenumbers.geocoder import area_description_for_number



creds = env.prefix('opencnam_')
session = requests.session()
session.headers = {'Accept': 'application/json'}


def clean(number):
    number = sub(r'\D', '', number)
    number = number[-10:]

    if not (len(number) < 10 or not (2002000000 <= long(number) <= 9999999999)):
        return number


def phone(number):
    url = 'https://api.opencnam.com/v1/phone/{0}'.format(number)
    params = {'username': creds['user'], 'api_key': creds['key']}
    r = session.get(url, params=params)

    return r.json or {}, r.status_code


def area_description(number):
    n = phonenumbers.parse(number, 'US')
    return area_description_for_number(n, 'en', region='US')

def description(number):
    n = phonenumbers.parse(number, 'US')
    return description_for_number(n, 'en', region='US')