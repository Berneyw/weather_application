import requests, json

def get_weather(API, lattitude, longitude):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "appid": API,
        "lat": lattitude,
        "lon": longitude,
        "units": "metric"
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return response.status_code
