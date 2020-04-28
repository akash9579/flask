# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 10:52:46 2020

@author: akash
"""


from flask import Flask
app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return "<h1>Home Page</h1>"

@app.route("/about")
def about():
    return "<h1>Welcome to about page</h1>"

