from flask import Flask, render_template, jsonify
import json
from config import CURRENT_DISPLAY, CURRENT_WEATHER_FILE

app = Flask(__name__)

@app.context_processor
def inject_config():
    return dict(cfg=CURRENT_DISPLAY)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather')
def weather():
    try:
        with open(CURRENT_WEATHER_FILE, 'r', encoding='utf-8') as f:
            raw = json.load(f)
            info_parts = raw.get("info", "").split("-")
            temp_str = info_parts[0].split("°")[0].strip()
            desc = info_parts[1].strip() if len(info_parts) > 1 else "Tidak diketahui"
            city = raw.get('city', 'Tidak diketahui')
            icon = raw.get('icon', '')
            
            return jsonify({
                "temp": int(temp_str),
                "desc": desc,
                "city": city,
                "icon": icon
            })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
