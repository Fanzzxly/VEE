# weather_utils.py

import requests
import time
import json
import os

API_KEY = "8896804d86d596a9a99bf3b1f1044fb0"
LAT = 33.33444
LON = 129.86533
UNITS = "metric"

CACHE_FILE = "forecast_cache.json"
CACHE_EXPIRY_HOURLY = 3600  # 1 jam
CACHE_EXPIRY_DAILY = 10800  # 3 jam

def fetch_forecast():
    url = f"https://api.openweathermap.org/data/3.0/onecall?lat={LAT}&lon={LON}&exclude=minutely,alerts&units={UNITS}&appid={API_KEY}"
    print(f"[DEBUG] Fetching data from: {url}")
    try:
        response = requests.get(url)
        print(f"[DEBUG] Status code: {response.status_code}")
        if response.status_code == 200:
            print("[DEBUG] Berhasil ambil data forecast")
            return response.json()
        else:
            print(f"[ERROR] Response bukan 200: {response.text}")
    except Exception as e:
        print(f"[ERROR] Gagal fetch forecast: {e}")
    return None


def load_cached_forecast():
    if not os.path.exists(CACHE_FILE):
        return None

    with open(CACHE_FILE, "r") as f:
        data = json.load(f)

    now = time.time()
    if now - data.get("hourly_cached_at", 0) > CACHE_EXPIRY_HOURLY:
        return None  # expired

    return data

def save_forecast_to_cache(data):
    now = time.time()
    data["hourly_cached_at"] = now                 # Waktu disimpan ke file
    data["hourly_fetched_at"] = data.get("current", {}).get("dt", now)  # Waktu data dari API (UTC)
    with open(CACHE_FILE, "w") as f:
        json.dump(data, f)


def get_forecast():
    cache = load_cached_forecast()
    if cache:
        return cache
    data = fetch_forecast()
    if data:
        save_forecast_to_cache(data)
        return data
    return None
