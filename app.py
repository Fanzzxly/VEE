# app.py | Magic Mirror v0.1
from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather')
def weather():
    try:
        with open('current_weather.json', 'r', encoding='utf-8') as f:
            raw = json.load(f)
            temp_str = raw['info'].split('°')[0]
            desc = raw['info'].split('-')[1].strip()
            city = raw['city']
            return jsonify({
                "temp": int(temp_str),
                "desc": desc,
                "city": city
            })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
