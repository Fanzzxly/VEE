import json
from datetime import datetime
from config import FORECAST_RAW_FILE, FORECAST_CLEAN_FILE

def parse_hourly_forecast(raw):
    result = []
    for hour_data in raw.get("hourly", [])[:5]:  
        timestamp = hour_data["dt"]
        time_str = datetime.fromtimestamp(timestamp).strftime("%H:%M")

        pop = round(hour_data.get("pop", 0) * 100)
        icon = hour_data["weather"][0]["icon"]

        result.append({
            "time": time_str,
            "pop": pop,
            "icon": icon
        })
    return result

def parse_and_save_hourly(path=FORECAST_CLEAN_FILE):
    try:
        with open(FORECAST_RAW_FILE, "r", encoding="utf-8") as f:
            raw = json.load(f)

        parsed = parse_hourly_forecast(raw)

        with open(path, "w", encoding="utf-8") as f:
            json.dump(parsed, f, indent=2)

        print("[✅] Forecast hourly berhasil disimpan (clean).")
    except Exception as e:
        print("[❌] Gagal parsing forecast:", str(e))


#entry point frontend
def get_hourly_forecast():
    try:
        with open(FORECAST_CLEAN_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        return {"error": str(e)}
