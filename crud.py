"""CRUD operations."""

from model import db, User, Like, Listing, Property, connect_to_db
from flask import request
import requests


# Functions start here!

def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    return user

def get_users():
    """Return all users."""

    return User.query.all()


def get_user_by_id(user_id):
    """Return a user by primary key."""

    return User.query.get(user_id)

def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter(User.email == email).first()

    

# def add_property(property_id):
#     """Create and return a new movie."""

#     theproperty = Listing(
#         property_id=property_id,
#     )

#     return theproperty

def get_search_properties():
    """Search for properties in a particular area"""
    city = request.args.get('city', '')
    state = request.args.get('state', '')
    zipcode = request.args.get('zipcode', '')
    proptype = request.args.get('proptype', '')
   
    

    url = "https://realty-in-us.p.rapidapi.com/properties/list-for-rent"

    querystring = {'state_code': state, 
                   'city': city,
                   'offset':'0',
                   "limit":'100',
                   'sort': 'relevance',
                   'postal_code': zipcode,
                   'prop_type': proptype}
    headers = {
    "X-RapidAPI-Host": "realty-in-us.p.rapidapi.com",
	"X-RapidAPI-Key": "ad06cc1ec2mshf405726e1df988dp12ad4bjsn96ac2fc85cba"}

    response = requests.request("GET", url, headers=headers, params=querystring)
    search_results = response.json()
    
    
    # serach_results is a list of dictionary
    return search_results

def get_property_by_id(property_id):
    """Return a properties."""
    url = "https://realty-in-us.p.rapidapi.com/properties/v2/detail"

    querystring = {"property_id":property_id}

    headers = {
        "X-RapidAPI-Host": "realty-in-us.p.rapidapi.com",
        "X-RapidAPI-Key": "ad06cc1ec2mshf405726e1df988dp12ad4bjsn96ac2fc85cba"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()
    return data


def get_properties():
    """Return all properties."""

    return Property.query.all()

def create_properties(address, price, size, date_lis):

    """Return a new property."""
    newproperty = Property(address=address, price=price, size=size, date_lis =date_lis)

    return newproperty

# def create_like(listing_id, user_id):
#     """Create and return a new movie."""

#     thelike = Like(
#         listing_id=listing_id,
#         user_id=user_id
#     )

#     return thelike

def get_likes_by_user(user_id):
    """Create and return a new movie."""

    return Like.query.filter(User.user_id == user_id).all()



# def get_property_by_id(property_id):
#     """Return a movie by primary key."""

#     return Property.query.get(property_id)


# def create_rating(user, theproperty, score):
#     """Create and return a new rating."""
#     rating = Rating(user=user, theproperty=theproperty, score=score)
#     return rating


if __name__ == '__main__':
    from server import app
    connect_to_db(app)