# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 19:08:01 2020

@author: akash
"""

##############################################################################


from flask import Flask,render_template
app = Flask(__name__)


#def home():
#   return "<h1>Home Page</h1>"

"""def home():
    return "<!doctype html>

        </html>"
"""
# we can use this but then the size of code gets bigger and its looks ugly 
# we are using Templates directory to store all html templates in that


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