#!/usr/bin/env python
# -*- coding: utf-8 -*-

import env
from opencnam import Phone, InvalidPhoneNumberError

creds = env.prefix('opencnam_')

def phone(number, dict=False):
    try:
        p = Phone(number, api_user=creds['user'], api_key=creds['key'])
    except InvalidPhoneNumberError:
        return None

    if dict:
        return {'number': p.number, 'cnam': p.cnam}
    else:
        return p