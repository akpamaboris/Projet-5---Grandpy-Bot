import googlemaps
from flask_googlemaps import GoogleMaps
from pprint import pprint
import gmplot

API_KEY= 'AIzaSyCFRB_ipsZztDSGoRwKOsnhXiWOKzi2YyU'

map_client = googlemaps.Client(API_KEY)

input_user = input('hey insère ton texte : ')

response = map_client.find_place([input_user], input_type ='textquery',fields=['formatted_address','photos', 'name',\
'place_id','geometry/location/lng','geometry/location/lat'])

#placeid_response = response['candidates'][0]['place_id']
pprint(response)
#print(placeid_response)
response_formatted_address= response['candidates'][0]['formatted_address']
response_latitude= response['candidates'][0]['geometry']['location']['lat']
response_longitude = response['candidates'][0]['geometry']['location']['lng']
response_html_attributions = response['candidates'][0]['photos'][0]['html_attributions']

print('the formatted address is : ',response_formatted_address)
print('the latitude is : ', response_latitude)
print('the longitude is : ', response_longitude)
print('the html response is : ', response_html_attributions[0])

#gmplot
gmap= gmplot.GoogleMapPlotter(response_latitude, response_longitude, 14 , apikey='AIzaSyCFRB_ipsZztDSGoRwKOsnhXiWOKzi2YyU')

#mark a hidden gem:
gmap.marker(37.770776, -122.461689,color='cornflowerblue')

gmap.draw('map.html')