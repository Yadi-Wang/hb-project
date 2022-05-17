"""Server for housing searching app."""
import os

from flask import Flask, render_template, request, flash, session, redirect, make_response

from model import connect_to_db, db

import crud
import requests
from jinja2 import StrictUndefined

app = Flask(__name__)

app.secret_key = os.environ.get('SECRET_KEY')
# app.secret_key = "DEV"


app.jinja_env.undefined = StrictUndefined


# Replace this with routes and view functions!
@app.route('/')
def index():
    """go to homepage"""
    if "user_email" in session:
        return redirect ("/myhomepage")
    
    return render_template("homepage.html")


@app.route('/myhomepage')
def show_my_homepage():
    """show user's homepage"""

    return render_template("myhomepage.html")

@app.route('/myproperties')
def show_my_favorites():
    """show user's liked listings"""
    
    # liked_properties = crud.get_likes_by_user(user_id)
    
    return render_template("myproperties.html")


@app.route('/addtofavorites')
def add_to_likes():
    like = crud.create_like(listing_id, user_id)
    db.session.add(like)
    db.session.commit()
    flash("You saved it")
    return redirect("/myproperties")


# @app.route('/allproperties')
# def get_properties():
#     """go to properties"""
#     properties = crud.get_properties()
#     return render_template("all_properties.html", properties = properties)

@app.route('/properties')
def search_properties():
    """go to search bar for properties"""
    
    return render_template("search-form.html")

@app.route('/properties/search')
def show_search_properties():
    """search for properties"""
    search_data = crud.get_search_properties()
    properties_list = search_data["listings"]
   
    return render_template("search-results.html", search_results = search_data, properties_list = properties_list)

@app.route('/properties/<property_id>')
def show_property(property_id):
    """show details on a particular property"""
    data = crud.get_property_by_id(property_id)
    property_details = data["properties"][0]
    address_details = property_details['address']
    photos = property_details['photos']
    schools = property_details['schools']
    return render_template("property_details.html", property_details = property_details, address_details = address_details, photos = photos, schools = schools)

@app.route("/users")
def all_users():
    """View all users."""

    users = crud.get_users()

    return render_template("all_users.html", users=users)

@app.route("/users", methods=["POST"])
def register_user():
    """Create a new user."""

    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)
    if user:
        flash ("Email already exists. Try again.")
       
    else:
        user = crud.create_user(email, password)
        db.session.add(user)
        db.session.commit()
        flash("Account created! Please log in.")
    return redirect("/")
    

@app.route("/welcome")
def welcome():
    return render_template("welcome.html")

@app.route("/login", methods=["POST"])
def process_login():
    """Process user login."""

    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)
    if not user or user.password != password:
        flash("The email or password you entered was incorrect.")
    else:
        # Log in user by storing the user's email in session
        session["user_email"] = user.email
        flash(f"Welcome back, {user.email}!")

    return redirect("/")


if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
