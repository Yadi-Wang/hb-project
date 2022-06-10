"""CRUD operations."""

from model import db, User, Like, Property, Application, connect_to_db
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
    min_bath = request.args.get('min_bath', '')
    min_bed = request.args.get('min_bed', '')
    price_max = request.args.get('maxprice', '')
    sqft_min = request.args.get('sqft_min', '')
    pets = request.args.get('pets', '')
    

    url = "https://realty-in-us.p.rapidapi.com/properties/list-for-sale"

    querystring = {'state_code': state, 
                   'city': city,
                   'offset':'0',
                   "limit":'100',
                   'sort': 'relevance',
                   'postal_code': zipcode,
                   'prop_type': proptype,
                   'baths_min': min_bath,
                   'beds_min': min_bed,
                   'price_max': price_max,
                   'sqft_min': sqft_min,
                   'no_pets_allowed': pets}
    headers = {
    "X-RapidAPI-Host": "realty-in-us.p.rapidapi.com",
	"X-RapidAPI-Key": "ad06cc1ec2mshf405726e1df988dp12ad4bjsn96ac2fc85cba"}

    response = requests.request("GET", url, headers=headers, params=querystring)
    search_results = response.json()
    
    
    # serach_results is a list of dictionary
    return search_results

def request_details_by_property_id(property_id):
    """Return a properties."""
    url = url = "https://realty-in-us.p.rapidapi.com/properties/v2/detail"

    querystring = {"property_id":property_id}

    headers = {
        "X-RapidAPI-Host": "realty-in-us.p.rapidapi.com",
        "X-RapidAPI-Key": "ad06cc1ec2mshf405726e1df988dp12ad4bjsn96ac2fc85cba"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()
    return data

# def add_a_listing(property_id):
#     """Add a property in the DB."""
#     listing = Listing(property_id=property_id)

#     return listing

def get_property_by_id(property_id):
    """Get a property from the DB."""
    
    return Property.query.filter(Property.property_id == property_id).first()

def get_properties():
    """Return all properties."""

    return Property.query.all()

def get_properties_by_user_id():
    """Return all properties searched by the user."""

    return Property.query.filter()

def add_a_property(address, price, date_lis, property_id):

    """Add a new property."""
    
    theproperty = Property(address=address, price=price, date_lis =date_lis, property_id=property_id)

    return theproperty

def create_like(theproperty, user):
    """Create and return a liked property."""

    the_favorite_property = Like(
        theproperty=theproperty,
        user=user)

    return the_favorite_property

def get_likes_by_user(user_id):
    """Get a like by user_id."""

    return Like.query.filter(Like.user_id == user_id).all()

def create_application(theproperty, user):
    """Create and return an applied property."""

    the_applied_property = Application(
        theproperty=theproperty,
        user=user)

    return the_applied_property

def get_applications_by_user(user_id):
    """Get an application by user_id."""

    return Application.query.filter(Application.user_id == user_id).all()







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