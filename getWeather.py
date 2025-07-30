import requests

weather_codes = {
    #01
    0: "Clear sky",
    #02
    1: "Mainly clear",
    2: "Partly cloudy",
    #03
    3: "Overcast",
    #09
    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Dense drizzle",
    #10
    61: "Slight rain",
    63: "Moderate rain",
    65: "Heavy rain",
    66: "Freezing rain (light)",
    67: "Freezing rain (heavy)",
    80: "Slight rain showers",
    81: "Moderate rain showers",
    82: "Violent rain showers",
    #13
    71: "Slight snow fall",
    73: "Moderate snow fall",
    75: "Heavy snow fall",
    77: "Snow grains",
    85: "Slight snow showers",
    86: "Heavy snow showers",
    #11
    95: "Thunderstorm",
    96: "Thunderstorm with hail",
    99: "Severe thunderstorm with hail",
}

def getWeather(lat,lon):
    try:
        url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        res=requests.get(url)
        res.raise_for_status()
        data=res.json()
        dataa=data.get('current_weather')
        degrees=dataa.get("temperature")
        weatherCode=dataa.get('weathercode')
        isDay=dataa.get('is_day')
        desc=weather_codes.get(weatherCode)
        return degrees,weatherCode, isDay , desc

    except requests.exceptions.RequestException as e:
        print("Error while getting the weather",e)
        return 
