"""Yelp API."""
import os
import requests
import json



#/businesses/search      URL-- "https://api.yelp.com/v3/businesses/search"

# Define the API key, Define the Endpoint(url), and define the headers
key = os.environ.get('YELP_API_KEY')
url = 'https://api.yelp.com/v3/businesses/search'

headers = {'Authorization': 'Bearer %s' % key}

# Define the parameters
parameters = {'term':'coffee','limit': 50,'radius': 100,'location': 'San Francisco'}

# Make a request to the yelp API
response = requests.get(url, headers=headers, params=parameters)

# convert the JSON string to a Dictionary
business_data = response.json()['businesses']

print(business_data)
