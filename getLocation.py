import json
import requests

def getLocation():
    try:
        res=requests.get("https://ipinfo.io/json")
        res.raise_for_status()
        data=res.json()
        loc=data.get("loc")
        city=data.get("city")
        return city,loc
    except requests.exceptions.RequestException as e:
        print("Error fetching location:", e)
        return None
    

getLocation()