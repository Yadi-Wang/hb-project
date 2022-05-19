"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system("dropdb housing")
os.system('createdb housing')

model.connect_to_db(server.app)
model.db.create_all()

# with open('data/properties50.json') as f:
#     property_data = json.loads(f.read())

# # Create properties, store them in list so we can use them
# # to create fake ratings later
# properties_in_db = []
# for theproperty in property_data:
#     address, price, size = (theproperty["formattedAddress"], theproperty["price"], theproperty["squareFootage"])
#     date_lis = (theproperty["listedDate"])

#     db_property = crud.create_properties(address, price, size, date_lis)
#     properties_in_db.append(db_property)

# model.db.session.add_all(properties_in_db)
# model.db.session.commit()


for n in range(10):
    email = f'user{n}@test.com'  # Voila! A unique email!
    password = 'test'

    # TODO: create a user here
    db_user = crud.create_user(email, password)
    model.db.session.add(db_user)

    # TODO: create 10 ratings for the user
    # for x in range(10):
      
    #   db_rating = crud.create_rating(db_user, choice(properties_in_db), randint(1,6))
    #   model.db.session.add(db_rating)

model.db.session.commit()