def get_weather_icon(condition):
    condition = condition.lower()
    if "clear" in condition:
        return "☀️"
    elif "cloud" in condition:
        return "☁️"
    elif "rain" in condition:
        return "🌧️"
    elif "drizzle" in condition:
        return "🌦️"
    elif "thunder" in condition:
        return "⛈️"
    elif "snow" in condition:
        return "❄️"
    elif "mist" in condition or "fog" in condition:
        return "🌫️"
    else:
        return "🌍"

def print_weather(data):
    weather_list = data["weather"]
    temp = data["main"]["temp"]
    feels = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    windspeed = data["wind"]["speed"]

    # Collect icons and descriptions for all weather states
    icons = " ".join(get_weather_icon(w["main"]) for w in weather_list)
    descriptions = ", ".join(w["description"] for w in weather_list)

    print(f"Overall weather: {descriptions} {icons}")
    print(f"Temperature: {temp}°C")
    print(f"Feels like: {feels}°C")
    print(f"Humidity: {humidity}%")
    print(f"Wind speed: {windspeed} m/s")