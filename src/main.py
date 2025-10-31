from location import get_user_location
from weather import get_weather
from cache import load_cache, save_cache, is_valid_cache
from utils import print_weather
from dotenv import load_dotenv
from time import time
from os import getenv


load_dotenv()
API = getenv("OPENWEATHER_API_KEY")
if not API:
    raise RuntimeError("OPENWEATHER_API_KEY not found")

if __name__ == "__main__":
    address = input("Enter your location\ne.g. (Tokyo, Japan): ")

    cache = load_cache()
    if address in cache and is_valid_cache(cache[address]):
        print("✅ Using cached data...")
        data = cache[address]["data"]
    else:
        print("🌐 Requesting data from API...")
        location = get_user_location(address)
        if location:
            data = get_weather(API, location.latitude, location.longitude)
            cache[address] = {"data": data, "timestamp": time()}
            save_cache(cache)
        else:
            print("Location not found")
            exit()

    print_weather(data)