import json
from datetime import datetime, timezone, timedelta
from config import FORECAST_CACHE_FILE

def format_hour(ts, tz_offset):
    dt = datetime.fromtimestamp(ts + tz_offset, tz=timezone.utc)
    return dt.strftime("%H:%M")

def format_day(ts, tz_offset):
    dt = datetime.fromtimestamp(ts + tz_offset, tz=timezone.utc)
    return dt.strftime("%a")

def get_hourly_forecast(limit=5):
    try:
        with open(FORECAST_CACHE_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            tz_offset = data.get("timezone_offset", 0)
            hourly = data.get("hourly", [])[:limit]

            return [{
                "hour": format_hour(item["dt"], tz_offset),
                "pop": int(item.get("pop", 0) * 100),
                "icon": item["weather"][0]["icon"],
                "desc": item["weather"][0]["description"]
            } for item in hourly]
    except Exception as e:
        return {"error": str(e)}


def get_daily_forecast(limit=7):
    try:
        with open(FORECAST_CACHE_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            tz_offset = data.get("timezone_offset", 0)
            daily = data.get("daily", [])[:limit]

            return [{
                "day": format_day(item["dt"], tz_offset),
                "min": round(item["temp"]["min"]),
                "max": round(item["temp"]["max"]),
                "icon": item["weather"][0]["icon"],
                "pop": int(item.get("pop", 0) * 100)  # convert to percent
            } for item in daily]
    except Exception as e:
        return {"error": str(e)}