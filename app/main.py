import os

import aiohttp
from dotenv import load_dotenv
from fastapi import FastAPI


# Get Weather API Key from .env file
load_dotenv()
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

app = FastAPI()  # Initialize app


@app.get("/")
async def root():
    """Root route that doesn't have any use."""
    return {"message": "Hello World"}


# Route for getting the current weather data based off of latitude & longitude.
@app.get("/current-data/{lat}/{lon}")
async def current_data(lat, lon):
    """Takes in latitide & longitude as path paramters, makes a request to Weather API with coordinates & returns reponse in JSON format"""
    params = {"lat": lat, "lon": lon,
              "appid": WEATHER_API_KEY, "units": "imperial"}
    async with aiohttp.ClientSession() as session, session.get("https://api.openweathermap.org/data/2.5/weather", params=params) as response:
        current_weather_data = await response.json()
    return current_weather_data
