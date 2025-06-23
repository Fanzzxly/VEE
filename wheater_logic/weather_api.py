# weather_api.py
import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
LAT = os.getenv("LAT")
LON = os.getenv("LON")
UNITS = os.getenv("UNITS", "metric")

def fetch_and_save_raw(path="data/raw/current_raw.json"):
    url = (
        f"https://api.openweathermap.org/data/2.5/weather?"
        f"lat={LAT}&lon={LON}&units={UNITS}&appid={API_KEY}"
    )
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        print("[✅] Data mentah berhasil disimpan.")
    else:
        print("[❌] Gagal fetch data dari OpenWeather:", response.status_code)
        

def fetch_and_save_forecast(path="data/raw/forecast_raw.json"):
    url = (
        f"https://api.openweathermap.org/data/3.0/onecall?"
        f"lat={LAT}&lon={LON}&exclude=minutely,daily,alerts&units={UNITS}&appid={API_KEY}"
    )
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        print("[✅] Data forecast hourly berhasil disimpan.")
    else:
        print("[❌] Gagal fetch data forecast:", response.status_code)
