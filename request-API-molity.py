import requests
import json


url = "https://realty-mole-property-api.p.rapidapi.com/saleListings"

querystring = {"city":"Austin","state":"TX"}

headers = {
    "X-RapidAPI-Host": "realty-mole-property-api.p.rapidapi.com",
    "X-RapidAPI-Key": "ad06cc1ec2mshf405726e1df988dp12ad4bjsn96ac2fc85cba"
}

response = requests.request("GET", url, headers=headers, params=querystring)
properties = response.json()  #this is a list of dictionary

# the code works:
# for i in range(50):
#     address = properties[i].get("formattedAddress")
#     price = properties[i].get("price")
#     print(f"{address}:{price}")

# The Grand Cyn, Austin, TX 78754:503990
# 12400 Cedar St, Austin, TX 78732:45000000
# 1210 Bruton Springs Rd, Austin, TX 78733:13000000
# 6480 Blue Bluff Rd, Austin, TX 78724:10999999
# 1904 Lauranne Ln, Austin, TX 78733:12500000
# 10301 Hwy 290 Hwy, Austin, TX 78737:15382407
# 6507 Bridge Point Pkwy, Unit Fern 2A, Austin, TX 78730:14975000
# 5705 Scenic View Dr, Austin, TX 78746:12250000
# 1505 Mount Larson Rd, Units 32 & 33, Austin, TX 78746:15000000
# 7901 Escala Dr, Austin, TX 78735:8950000
# 2707 Trail, of the Madrones, Austin, TX 78746:7495000
# 1100 River Hills Rd, Austin, TX 78733:9500000
# 5512 Cuesta Verde, Austin, TX 78746:8990000
# 1501 Ridgecrest Dr, Austin, TX 78746:10950000
# 10210 Crumley Ranch Rd, Austin, TX 78738:8500000
# 3601 Stoneridge Rd, Austin, TX 78746:11103750
# 8925 S FM 973, Austin, TX 78719:7600000
# 6507 Bridge Point Pkwy, Unit Jasmine 2B, Austin, TX 78730:8275000
# 211 Costa Bella Dr, Austin, TX 78734:8200000
# 4511 Island Cv, Austin, TX 78731:7500000
# 8503 Hillmoore Dr, Austin, TX 78744:7400000
# 3900 Pearce Rd, Austin, TX 78730:6880000
# 7100 Comanche Trl, Austin, TX 78732:6200000
# 2300 Portofino Ridge Dr, Austin, TX 78735:6840000
# 12217 Iron Bluff Pl, Austin, TX 78738:5750000
# 7500 Escala Dr, Austin, TX 78735:6450000
# 495 Whippoorwill Trl, Austin, TX 78746:5890000
# 8409 Chalk Knoll Dr, Austin, TX 78735:5999999
# 98 San Jacinto Blvd, Unit 2902, Austin, TX 78701:7250000
# 1101 N Weston Ln, Austin, TX 78733:6400000
# 15203 W Hwy, 71, Austin, TX 78738:6300000
# 303 Pleasant Dr, Austin, TX 78746:5900000
# 307 W Elizabeth St, Austin, TX 78704:5850000
# 17301 Flintrock Rd, Austin, TX 78738:5350000
# 2104 Island Wood Rd, Austin, TX 78733:5200000
# 11705 Shoreview Overlook, Austin, TX 78732:5250000
# 4804 Toreador Dr, Austin, TX 78746:5200000
# 217 Canyon Turn Trl, Austin, TX 78734:5200000
# 901 W 9th St, Apt 1101, Austin, TX 78703:5695000
# 11961 Overlook Pass, Austin, TX 78738:5000000
# 4212 Serene Hills Dr, Austin, TX 78738:5200000
# 2213 Westlake Dr, Austin, TX 78746:4995000
# 4610 Anikawi Dr, Austin, TX 78746:5195000
# 2211 Westlake Dr, Austin, TX 78746:4995000
# 112 Bella Cima Dr, Austin, TX 78734:4995000
# 9104 Atwater Cv, Austin, TX 78733:4600000
# 18520 Madrone Vista Dr, Austin, TX 78738:4990000
# 1800 Bay Hill Dr, Austin, TX 78746:4100000
# 6507 Bridge Point 3c Pkwy, Unit Wisteria, Austin, TX 78730:4575000
# 3612 Verano Dr, Austin, TX 78735:4725000

# print(properties)

# {'bathrooms': 2, 'bedrooms': 2, 'price': 374900, 'rawAddress': '9707 Anderson Mill Rd Apt 23, Austin, Texas 78750', 'squareFootage': 1512, 'county': 'Williamson County', 'propertyType': 'Single Family', 'addressLine1': '9707 Anderson Mill Rd', 'addressLine2': 'Apt 23', 'city': 'Austin', 'state': 'TX', 'zipCode': '78750', 'formattedAddress': '9707 Anderson Mill Rd, Apt 23, Austin, TX 78750', 'lastSeen': '2022-05-06T06:02:46.620Z', 'listedDate': '2022-04-30T08:44:06.785Z', 'status': 'Active', 'removedDate': None, 'daysOnMarket': 6, 'createdDate': '2022-04-30T08:44:06.785Z', 'id': '9707-Anderson-Mill-Rd,-Apt-23,-Austin,-TX-78750', 'latitude': 30.446312, 'longitude': -97.792828}

# print(response.text)

# data = json.loads(response.text)
# j = json.dumps(data)
# print(j)

# The code works:
for theproperty in properties:
    address = theproperty.get("formattedAddress")
    price = theproperty.get("price")
    print(f"{address}:{price}")

