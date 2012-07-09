#!/usr/bin/env python
# -*- coding: utf-8 -*-

import env
from opencnam import Phone

creds = env.prefix('opencnam_')

def phone(number):
    return Phone(number, api_user=creds['user'], api_key=creds['key'])