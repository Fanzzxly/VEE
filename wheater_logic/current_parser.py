# weather_parser.py

import json
from config import CURRENT_RAW_FILE, CURRENT_CLEAN_FILE

def parse_current_weather(raw):
    temp = round(raw["main"]["temp"])
    desc = raw["weather"][0]["description"].capitalize()
    icon = raw["weather"][0]["icon"]
    city = raw.get("name", "Unknown")

    return {
        "info": f"{temp}°C - {desc}",
        "icon": icon,
        "city": city
    }

def parse_and_save_clean():
    try:
        with open(CURRENT_RAW_FILE, "r", encoding="utf-8") as f:
            raw = json.load(f)

        parsed = parse_current_weather(raw)

        with open(CURRENT_CLEAN_FILE, "w", encoding="utf-8") as f:
            json.dump(parsed, f, indent=2)

        print("[✅] Data berhasil diparse dan disimpan ke format bersih.")
       
    except Exception as e:
        print("[❌] Gagal parsing:", str(e))
