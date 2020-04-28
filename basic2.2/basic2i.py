# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 10:03:26 2020

@author: akash
"""


##############################################################################


from flask import Flask,render_template,url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html' , posts=posts)   # posts1 is the argument passing to the templates
                                                         # posts is the name of the directory


@app.route("/about")
def about():
    return render_template('about.html')