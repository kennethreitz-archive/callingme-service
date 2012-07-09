# -*- coding: utf-8 -*-

import env
import dynamo

d = env.prefix('dynamo_')

table = dynamo.table(d['table'], (d['access_key'], d['secret_access_key']))