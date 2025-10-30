from location import get_user_location
from weather import get_weather
from utils import print_weather
from dotenv import load_dotenv
from os import getenv

load_dotenv()
API = getenv("OPENWEATHER_API_KEY")
if not API:
    raise RuntimeError("OPENWEATHER_API_KEY not found")

if __name__ == "__main__":
    address = input("Enter your location\ne.g. (Tokyo, Japan): ")
    location = get_user_location(address)

    if location:
        data = get_weather(API, location.latitude, location.longitude)
        print_weather(data)
    else:
        print("Location not found")