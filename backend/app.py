from flask import Flask, request, jsonify, render_template, redirect, url_for, session, flash, Response, abort
from search import search
from filter import Filter
from storage import DBstorage
import html
from flask_sqlalchemy import SQLAlchemy
import sqlite3
import pandas as pd
from flask_cors import CORS, cross_origin
import numpy as np

#from flask.ext.reqarg import request_args
#from flask_navigation import Navigation
db = SQLAlchemy()
app = Flask(__name__)
app.secret_key = "hello"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.sqlite3"
db.__init__(app)    
CORS(app)

    
#app.add_url_rule("/", endpoint="index")
#nav = Navigation(app)



search_template = """
<form action="/" method="post">
    <input type="text" name="query">
    <input type="submit" value="search">
</form>

<div>
    <a href="/login">Login</a>

    <a href="/register">Register</a>
</div>


"""

result_template = """

<p class="site">{rank}: {link} <span class="rel-button" onclick='relevant("{query}", "{link}");'>Relevant</span></p>
<a href="{link}">{title}</a>
<p class="snippet">{snippet}</p>
"""
 
register_template = """

<form action="/register method="post">
    
    <label for="username"><b>Username</b></label>
    <input type="text" placeholder="Enter username" name="username" required>
    
    <label for="password"><b>Password</b></label>
    <input type="password" placeholder="Enter Password" name="password" required>

    <button type="submit">Register</button>
    <label>
        <input type="checkbox" checked="checked" name="remember"> Remember me </label>
</form>

"""

login_tempate = """

<form action="/login method="post">
    <label for="username"><b>Username</b></label>
    <input type="text" placeholder="Enter username" name="username" required>
    
    <label for="password"><b>Password</b></label>
    <input type="password" placeholder="Enter Password" name="password" required>

    <button type="submit">Login</button>
    <label>
        <input type="checkbox" checked="checked" name="remember"> Remember me </label>
</form>

"""

def show_registration_form():
    return register_template

def show_search_form():
    return search_template

def run_search(query):
    results = search(query)
    fi = Filter(results)
    results = fi.filter()
    rendered = search_template
    results["snippet"] = results["snippet"].apply(lambda x: html.escape(x))
    for index, row in results.iterrows():
        rendered += result_template.format(**row)
    return rendered



@app.route("/", methods=["GET", "POST"])
def search_form():
    if request.method == "POST":
        query = request.form["query"]
        return run_search(query)
    else:
        return show_search_form()


# CHANGE TO BE INSIDE A URL
@app.route("/relevant", methods=["POST"])
def mark_relevant():
    data = request.get_json()
    query = data["query"]
    link = data["link"]
    storage = DBstorage()
    storage.update_relevance(query, link , 10)
    return jsonify(success=True)

def show_login_form():
    return login_tempate

@app.route('/success/<name>')
def success(name):
    user_page = 'welcome %s' % name
    
    return user_page

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get("password")
    
        storage = DBstorage()
        found_user = storage.find_user(username)
       
        print(found_user)

        if not found_user : 
            flash('please register')
            return show_search_form()


        session["username"] = found_user[0]
        user_arr = np.array(found_user)
        page = request.args.get('username')
        
        return 'logged in'
        
    elif  "userId" in session:
            flash("Already Logged In!")
            return show_search_form()

    else:
        return show_login_form()



@app.route("/register", methods = ["POST", "GET"])
def register():

    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        if not username: 
            flash("Username is required!")
        elif not password:
            flash("Password is required!")

        else:
            page = request.args.get('username')
            cur = DBstorage()
            cur.register_user(username, password)
            return redirect(url_for('success', name = page ))
    
    return show_registration_form()
       


# @app.route("/member", methods=["POST", "GET"])
# def user():

#     password = None
#     if "user" in session:
#         user = session["user"]

#         if request.method == "POST":
#             password = request.form["password"]
#             session["password"] = password
#             found_user = user.query.filter_by(username=user).first()
#             found_user.password = password
#             db.session.commit()

            
#             flash("password was saved")
#         else:
#             if "password" in session:
#                 password = session["password"]

#             return render_template("memeber.html", password=password)
#     else:
#         flash("You are not loged in!")
#         return redirect(url_for("login"))
    
#return {"members": ["Member1", "Member2", "Member3"]}

@app.route("/logout")
def logout():
    flash("You have been logged out!", "info")
    session.pop("user", None)
    session.pop("username", None)
    return redirect(url_for("login"))


if __name__ == '__main__':
    db.create_all()
    app.run(port=5000, debug=True)
