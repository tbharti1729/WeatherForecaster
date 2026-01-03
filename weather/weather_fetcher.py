import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()


API_KEY = os.getenv("OPENWEATHER_API_KEY")

if not API_KEY:
    raise ValueError("OPENWEATHER_API_KEY not found. Check your .env file.")

WEATHER_URL = "http://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "http://api.openweathermap.org/data/2.5/forecast"
HISTORY_FILE = "weather_history.json"

def get_weather(city_name):
    """Fetch current weather for a city."""
    params = {"q": city_name, "appid": API_KEY, "units": "metric"}
    try:
        response = requests.get(WEATHER_URL, params=params)
        response.raise_for_status()
        data = response.json()
        weather = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"]
        }
        save_history(weather)
        return weather
    except requests.exceptions.HTTPError:
        return None
    except Exception as e:
        print("Error:", e)
        return None

def get_forecast(city_name, days=3):
    """Fetch multi-day forecast."""
    params = {"q": city_name, "appid": API_KEY, "units": "metric", "cnt": days*8}
    try:
        response = requests.get(FORECAST_URL, params=params)
        response.raise_for_status()
        data = response.json()
        forecast = []
        for item in data["list"]:
            forecast.append({
                "datetime": item["dt_txt"],
                "temp": item["main"]["temp"],
                "description": item["weather"][0]["description"]
            })
        return forecast
    except:
        return None

def save_history(weather):
    """Save search history to JSON."""
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            history = json.load(f)
    else:
        history = []

    history.append(weather)
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=4)

def load_history():
    """Load search history from JSON."""
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    return []

if __name__ == "__main__":
    city = input("Enter city name: ")
    weather = get_weather(city)
    if weather:
        print(f"{weather['city']}: {weather['temperature']}°C, {weather['description']}")
    else:
        print("City not found or API error.")
