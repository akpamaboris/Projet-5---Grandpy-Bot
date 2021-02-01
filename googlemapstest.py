import googlemaps
from flask_googlemaps import GoogleMaps
from pprint import pprint

API_KEY= 'AIzaSyCFRB_ipsZztDSGoRwKOsnhXiWOKzi2YyU'

map_client = googlemaps.Client(API_KEY)

response = map_client.find_place(['Openclassrooms'], input_type ='textquery',fields=['formatted_address','photos', 'name',\
'place_id','geometry/location/lng','geometry/location/lat'])

#placeid_response = response['candidates'][0]['place_id']
pprint(response)
#print(placeid_response)


