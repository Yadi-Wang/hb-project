"""Models for house searching app."""

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """A user."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True,)
    # last_name = db.Column(db.String)
    # first_name = db.Column(db.String)
    # created_at = db.Column(db.DateTime)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    # likes = db.relationship("Like", backref="user")

    
    def __repr__(self):
        return f'<User user_id={self.user_id} email={self.email}>'


class Like(db.Model):
    """A property."""

    __tablename__ = 'likes'

    like_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True,)
    property_id = db.Column(db.Integer, db.ForeignKey("properties.property_id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    
    user = db.relationship("User", backref="likes")
    theproperty = db.relationship("Property", backref="likes")
    
    def __repr__(self):
        return f'<LIke like_id={self.like_id} property_id={self.property_id}>'


class Property(db.Model):
    """Listings for a property."""

    __tablename__ = 'properties'

    property_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True,)
    address = db.Column(db.String)
    price = db.Column(db.Integer)
    size = db.Column(db.Integer)
    date_lis = db.Column(db.String)


    def __repr__(self):
        return f'<Property property_id={self.property_id}>'

        

class Listing(db.Model):
    """A listing."""

    __tablename__ = 'listings'

    listing_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True,)
    property_id = db.Column(db.Integer)

    def __repr__(self):
        return f'<Listing listing_id={self.listing_id}>'



def connect_to_db(flask_app, db_uri="postgresql:///housing", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)
