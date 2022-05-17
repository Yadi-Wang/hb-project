import requests
import json


url = "https://realty-in-us.p.rapidapi.com/properties/list-for-sale"
querystring = {'state_code': "NY", 'city': "New York City",
                   'offset':'0',
                   "limit":'5',
                   'sort': 'relevance'}
headers = {
    "X-RapidAPI-Host": "realty-in-us.p.rapidapi.com",
	"X-RapidAPI-Key": "ad06cc1ec2mshf405726e1df988dp12ad4bjsn96ac2fc85cba"}

response = requests.request("GET", url, headers=headers, params=querystring)
results = response.json()  #this is a list of dictionary


print(results["listings"])

# {'bathrooms': 2, 'bedrooms': 2, 'price': 374900, 'rawAddress': '9707 Anderson Mill Rd Apt 23, Austin, Texas 78750', 'squareFootage': 1512, 'county': 'Williamson County', 'propertyType': 'Single Family', 'addressLine1': '9707 Anderson Mill Rd', 'addressLine2': 'Apt 23', 'city': 'Austin', 'state': 'TX', 'zipCode': '78750', 'formattedAddress': '9707 Anderson Mill Rd, Apt 23, Austin, TX 78750', 'lastSeen': '2022-05-06T06:02:46.620Z', 'listedDate': '2022-04-30T08:44:06.785Z', 'status': 'Active', 'removedDate': None, 'daysOnMarket': 6, 'createdDate': '2022-04-30T08:44:06.785Z', 'id': '9707-Anderson-Mill-Rd,-Apt-23,-Austin,-TX-78750', 'latitude': 30.446312, 'longitude': -97.792828}

# print(response.text)

# data = json.loads(response.text)
# j = json.dumps(data)
# print(j)

# The code works:
# for theproperty in properties:
#     address = theproperty.get("formattedAddress")
#     price = theproperty.get("price")
#     print(f"{address}:{price}")

