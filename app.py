#!/usr/bin/bash
# -*- coding: utf-8 -*-


from flask import Flask

from main.py import authorize
app = Flask(__name__)

AUTHORIZED = False

@app.route("/")
def home():
    if not  AUTHORIZED:
        return redirect(url_for('login'))
    return "Hello World!"

@app.route("/login")
def authorize():


