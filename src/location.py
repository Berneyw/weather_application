from geopy.geocoders import Nominatim
from time import sleep

app = Nominatim(user_agent="test")
def get_user_location(address):
    sleep(1)
    try:
        return app.geocode(address)
    except:
        return get_user_location(address)
