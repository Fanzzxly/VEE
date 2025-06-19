# weather_parser.py

import json
from config import CURRENT_WEATHER_FILE

def get_current_weather():
    try:
        with open(CURRENT_WEATHER_FILE, 'r', encoding='utf-8') as f:
            raw = json.load(f)

            # Pecah info jadi "22°C - Overcast clouds"
            info_parts = raw.get("info", "").split("-")
            temp_str = info_parts[0].split("°")[0].strip()
            desc = info_parts[1].strip() if len(info_parts) > 1 else "Tidak diketahui"

            city = raw.get('city', 'Tidak diketahui')
            icon = raw.get('icon', '')

            return {
                "temp": int(temp_str),
                "desc": desc,
                "city": city,
                "icon": icon
            }

    except Exception as e:
        return {"error": str(e)}
