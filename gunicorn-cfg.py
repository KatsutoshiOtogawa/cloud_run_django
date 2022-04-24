# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os

PORT = os.environ.get('PORT')

bind = '0.0.0.0' + ':' + PORT
workers = 1
accesslog = '-'


loglevel = 'debug'
capture_output = True
enable_stdio_inheritance = True
