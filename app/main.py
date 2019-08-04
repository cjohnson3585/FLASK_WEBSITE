# -*- coding: utf-8 -*-

'''Entry point to all things to avoid circular imports.'''
from app import app, freezer

@app.route('/')
def home():
    return 'Hello Home'

'''
|__movies
     |__run.py
     |__app
        ├── templates
        │   └── index.html
        │   └── signup.html
        └── __init__.py
        └── routes.py
        '''
