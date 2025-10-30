def print_weather(data):
    base = data["weather"][0]["main"]
    temp = data["main"]["temp"]
    feels = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    windspeed = data["wind"]["speed"]

    print(f"🌤 Overall weather: {base}")
    print(f"Average temperature: {temp}")
    print(f"Feels like: {feels}")
    print(f"Humidity: {humidity}")
    print(f"Average windspeed: {windspeed}")

    return 0