import json
import requests
import pandas as pd
from geopy.distance import geodesic


# Load Esso data from your local JSON file
with open('fuel-prices-data.json', 'r') as file:
    esso_data = json.load(file)

with open('tesco-fuel-prices-data.json', 'r') as file:
    tesco_data = json.load(file)

# Combine both datasets into a single list of stations
all_stations = esso_data['stations'] + tesco_data['stations']

# Your target latitude and longitude
target_location = (53.79512792965181, -2.7353053587023575)

# Variable to store the closest station
closest_station = None
min_distance = float('inf')

# Iterate through all stations
for station in all_stations:
    station_location = (station['location']['latitude'], station['location']['longitude'])
    # Calculate the distance from the target location
    distance = geodesic(target_location, station_location).kilometers
    
    # If this station is closer, update the closest_station
    if distance < min_distance:
        min_distance = distance
        closest_station = {
            'address': station.get('address', 'No address'),
            'postcode': station.get('postcode', 'No postcode'),
            'brand': station.get('brand', 'Unknown brand'),
            'distance_km': distance,
            'prices': station.get('prices', 'No prices available')
        }

# Output the closest station
if closest_station:
    print(f"Closest Station: {closest_station['brand']} at {closest_station['address']}, {closest_station['postcode']}")
    print(f"Distance: {closest_station['distance_km']} km")
    print(f"Prices: {closest_station['prices']}")
else:
    print("No stations found.")
