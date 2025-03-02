import requests
import os

def get_weather(destination):
    # Store API Key in an environment variable or replace directly
    api_key = os.getenv("OPENWEATHER_API_KEY", "67c879415b6ad1a120f65a0afb1d8399")  

    if not api_key or api_key == "your_api_key_here":
        return "Error: Missing API Key"

    url = f"http://api.openweathermap.org/data/2.5/weather?q={destination}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)
        
        data = response.json()
        weather = data["weather"][0]["description"].capitalize()
        temp = data["main"]["temp"]
        
        return f"🌤️ {weather}, {temp}°C"
    
    except requests.exceptions.RequestException as e:
        return f"Error fetching weather data: {e}"

