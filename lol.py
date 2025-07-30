weather_codes = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Depositing rime fog",
    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Dense drizzle",
    61: "Slight rain",
    63: "Moderate rain",
    65: "Heavy rain",
    80: "Slight rain showers",
    95: "Thunderstorm",
}

def get_weather(lat, lon):
    import requests
    try:
        url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        res = requests.get(url, timeout=5)
        res.raise_for_status()
        data = res.json()
        weather = data['current_weather']
        code = weather['weathercode']
        description = weather_codes.get(code, "Unknown")
        print(f"{description}, {weather['temperature']}°C")
        return description, weather['temperature']
    except Exception as e:
        print("Error:", e)
        return None, None

# Example for Lahore
get_weather(31.5204, 74.3587)
