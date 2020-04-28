# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 10:13:54 2020

@author: akash
"""



from flask import Flask
app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Home Page</h1>"


