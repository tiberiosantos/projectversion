#!/usr/bin/env python
#--*-- coding: utf-8 --*--

from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname' : 'Miguel'}
    return template("index.html", title="Home", user = user)
