import requests
import time
import json
import os

# Konfigurasi
API_KEY = "8896804d86d596a9a99bf3b1f1044fb0"
LAT = 33.33444
LON = 129.86533
UNITS = "metric"

CACHE_FILE = "forecast_cache.json"
CURRENT_FILE = "current_weather.json"
CACHE_EXPIRY_HOURLY = 3600  # 1 jam

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

def save_forecast_to_cache(data):
    now = time.time()
    data["hourly_cached_at"] = now
    with open(CACHE_FILE, "w") as f:
        json.dump(data, f)

    # Simpan bagian current saja
    current = data.get("current", {})
    if current:
        current_data = {
            "info": f"{round(current['temp'])}°C - {current['weather'][0]['description'].capitalize()}",
            "icon_url": f"http://openweathermap.org/img/wn/{current['weather'][0]['icon']}@2x.png",
            "city": "Imari",  # Static karena OneCall tidak sediakan nama kota
            "fetched_at": now
        }
        with open(CURRENT_FILE, "w") as f:
            json.dump(current_data, f)

def load_cached_forecast():
    if not os.path.exists(CACHE_FILE):
        return None
    with open(CACHE_FILE, "r") as f:
        data = json.load(f)
    now = time.time()
    if now - data.get("hourly_cached_at", 0) > CACHE_EXPIRY_HOURLY:
        return None
    return data

def get_forecast():
    cache = load_cached_forecast()
    if cache:
        return cache

    data = fetch_forecast()
    if data:
        save_forecast_to_cache(data)
        return data

    # Fallback: kalau fetch gagal, pakai cache lama meski expired
    if os.path.exists(CACHE_FILE):
        print("[WARN] Fetch gagal, fallback ke cache lama")
        with open(CACHE_FILE, "r") as f:
            return json.load(f)

    return None

def get_current_weather():
    if os.path.exists(CURRENT_FILE):
        with open(CURRENT_FILE, "r") as f:
            return json.load(f)
    return {
        "info": "Cuaca tidak tersedia",
        "icon_url": "",
        "city": "",
        "fetched_at": 0
    }
