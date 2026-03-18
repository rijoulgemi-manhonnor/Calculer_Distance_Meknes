import time
import requests
import openrouteservice
from geopy.geocoders import Nominatim
from config import ORS_API_KEY, MEKNES_COORDS, REQUEST_DELAY

class DistanceCalculator:
    def __init__(self):
        self.geolocator = Nominatim(user_agent="meknes_distances_bot")
        self.ors_client = openrouteservice.Client(key=ORS_API_KEY)
        self.meknes = MEKNES_COORDS

    def geocode_commune(self, search_name):
        try:
            location = self.geolocator.geocode(search_name)
            if location:
                return location.latitude, location.longitude
            return None, None
        except Exception:
            return None, None

    def calculate_route_distance(self, lat, lon):
        try:
            coords = [[self.meknes["lon"], self.meknes["lat"]], [lon, lat]]
            route = self.ors_client.directions(coordinates=coords, profile='driving-car', format='geojson')
            summary = route['features'][0]['properties']['summary']
            return round(summary['distance'] / 1000, 2), round(summary['duration'] / 60, 1)
        except Exception:
            return self.calculate_route_distance_fallback(lat, lon)

    def calculate_route_distance_fallback(self, lat, lon):
        try:
            url = f"http://router.project-osrm.org/route/v1/driving/{self.meknes['lon']},{self.meknes['lat']};{lon},{lat}?overview=false"
            data = requests.get(url).json()
            if data['code'] == 'Ok':
                route = data['routes'][0]
                return round(route['distance'] / 1000, 2), round(route['duration'] / 60, 1)
            return None, None
        except Exception:
            return None, None
