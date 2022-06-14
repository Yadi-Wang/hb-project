import requests
import json



import time
import googlemaps # pip install googlemaps
import pandas as pd # pip install pandas

def miles_to_meters(miles):
    try:
        return miles * 1_609.344
    except:
        return 0
        
API_KEY = 'AIzaSyBEqKcxHpYcXy26vXDUFySKYx0RqcOevmc'
map_client = googlemaps.Client(API_KEY)

address = '333 Market St, San Francisco, CA'
geocode = map_client.geocode(address=address)
(lat, lng) = map(geocode[0]['geometry']['location'].get, ('lat', 'lng'))


search_string = 'ramen'
distance = miles_to_meters(2)
business_list = []

response = map_client.places_nearby(
    location=(lat, lng),
    keyword=search_string,
    radius=distance
)   

business_list.extend(response.get('results'))
next_page_token = response.get('next_page_token')

while next_page_token:
    time.sleep(2)
    response = map_client.places_nearby(
        location=(lat, lng),
        keyword=search_string,
        radius=distance,
        page_token=next_page_token
    )   
    business_list.extend(response.get('results'))
    next_page_token = response.get('next_page_token')

df = pd.DataFrame(business_list)
df['url'] = 'https://www.google.com/maps/place/?q=place_id:' + df['place_id']
df.to_excel('{0}.xlsx'.format(search_string), index=False)


# {"matching_results":111,"restaurants":[{"id":23643084,"restaurantName":"Nusr-et Steakhouse Beverly Hills","address":"84 -88 N Canon Drive Los Angeles California","zipCode":"90210","phone":"+1 310-921-5935","website":"http:\/\/nusr-et.com.tr","email":"","latitude":"34.06809","longitude":"-118.39924","stateName":"CA","cityName":"Beverly Hills","hoursInterval":"","cuisineType":"European,Turkish,Fusion"},{"id":23624322,"restaurantName":"The Lobby Lounge","address":"9850 Wilshire Blvd","zipCode":"90210","phone":"+1 310-860-6566","website":"https:\/\/www.waldorfastoriabeverlyhills.com\/dining\/lobby-lounge\/","email":"","latitude":"34.06673","longitude":"-118.4113","stateName":"CA","cityName":"Beverly Hills","hoursInterval":"","cuisineType":"Restaurant"},{"id":12549619,"restaurantName":"Jean-Georges","address":"9850 Wilshire Blvd Waldorf Astoria Beverly Hills","zipCode":"90210","phone":"+1 310-860-6566","website":"https:\/\/www.waldorfastoriabeverlyhills.com\/dining\/jean-georges\/","email":"","latitude":"34.06673","longitude":"-118.4113","stateName":"CA","cityName":"Beverly Hills","hoursInterval":"Sun - Thu (7:00 AM - 10:30 AM) | Sun - Sat (11:45 AM - 3:30 PM) | Fri - Sat (8:00 AM - 10:30 AM)","cuisineType":"American"},{"id":6378194,"restaurantName":"Comoncy","address":"413 N Bedford Dr.","zipCode":"90210","phone":"+1 424-285-8874","website":"https:\/\/www.comoncy.com\/","email":"info@comoncy.com","latitude":"34.0681","longitude":"-118.405205","stateName":"CA","cityName":"Beverly Hills","hoursInterval":"Mon - Fri (8:00 AM - 4:00 PM) | Sat (9:00 AM - 3:00 PM)","cuisineType":"American,Cafe,Healthy"},{"id":4811993,"restaurantName":"Subway","address":"9673 Wilshire Blvd","zipCode":"90210","phone":"+1 310-276-1562","website":"https:\/\/restaurants.subway.com\/united-states\/ca\/beverly-hills\/9673-wilshire-blvd","email":"","latitude":"34.066917","longitude":"-118.404594","stateName":"CA","cityName":"Beverly Hills","hoursInterval":"Mon - Fri (6:00 AM - 7:00 PM) | Sat - Sun (8:30 AM - 6:00 PM)","cuisineType":"Restaurant"},{"id":11800337,"restaurantName":"Washer Restaurant","address":"178 Miller Rd","zipCode":"90210","phone":"+1 419-366-9450","website":"","email":"Washwash67@gmail.com","latitude":"34.09442","longitude":"-118.37702","stateName":"CA","cityName":"Beverly Hills","hoursInterval":"","cuisineType":"Seafood"},{"id":348073,"restaurantName":"Polo Lounge at the Beverly Hills Hotel","address":"9641 Sunset Blvd","zipCode":"90210","phone":"+1 310-887-2777","website":"https:\/\/www.dorchestercollection.com\/en\/los-angeles\/the-beverly-hills-hotel\/restaurants-bars\/the-polo-lounge\/","email":"info.bhh@dorchestercollection.com","latitude":"34.081528","longitude":"-118.41421","stateName":"CA","cityName":"Beverly Hills","hoursInterval":"Sun - Thu (7:00 AM - 10:00 PM) | Fri - Sat (7:00 AM - 11:00 PM)","cuisineType":"American"},{"id":20327751,"restaurantName":"Gucci Osteria da Massimo Bottura","address":"347 North Rodeo Drive","zipCode":"90210","phone":"+1 424-600-7490","website":"https:\/\/gucciosteria.com\/en\/beverlyhills","email":"","latitude":"34.068604","longitude":"-118.402695","stateName":"CA","cityName":"Beverly Hills","hoursInterval":"Wed - Sun (11:30 AM - 2:00 PM)","cuisineType":"Restaurant"},{"id":348164,"restaurantName":"Le Pain Quotidien","address":"9630 S Santa Monica Blvd","zipCode":"90210","phone":"+1 310-859-1100","website":"https:\/\/www.lepainquotidien.com\/us\/en\/locations\/beverly_hills\/9630-s-santa-monica-blvd","email":"bonjour@lepainquotidien.com","latitude":"34.06947","longitude":"-118.40591","stateName":"CA","cityName":"Beverly Hills","hoursInterval":"Sun - Sat (7:00 AM - 3:30 PM)","cuisineType":"French,European,Cafe"},{"id":348125,"restaurantName":"The Palm - Beverly Hills","address":"267 North Canon Drive Suite A7","zipCode":"90210","phone":"+1 310-550-8811","website":"https:\/\/www.thepalm.com\/restaurants\/beverly-hills\/","email":"customercare@thepalm.com","latitude":"34.06886","longitude":"-118.39954","stateName":"CA","cityName":"Beverly Hills","hoursInterval":"Sun (4:00 PM - 9:00 PM) | Mon - Thu (11:30 AM - 9:00 PM) | Fri (11:30 AM - 10:00 PM) | Sat (5:00 PM - 10:00 PM)","cuisineType":"American,Steakhouse"}]}

# data = json.loads(response.text)
# j = json.dumps(data)
# print(j)

# The code works:
# for theproperty in properties:
#     address = theproperty.get("formattedAddress")
#     price = theproperty.get("price")
#     print(f"{address}:{price}")

