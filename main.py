#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/<username>')
@app.route('/<username>/<int:post_id>')
def home(username="", post_id=0):
	if username and post_id:
		return "Hello %s - %d" % (username, 50 / 0)
	if username:
		return "Hello %s" % username
	else:
		return "Hello Stranger"

app.debug = True
app.run()
