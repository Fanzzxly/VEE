from flask import Flask, render_template, jsonify
from config import CURRENT_DISPLAY
from wheater_main_logic import run_periodically
from wheater_logic.current_ui_parser import get_current_weather
from wheater_logic.forecast_parser import get_hourly_forecast

app = Flask(__name__)


run_periodically()

@app.context_processor
def inject_config():
    return dict(cfg=CURRENT_DISPLAY)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather')
def weather():
    data = get_current_weather()
    status = 500 if "error" in data else 200
    return jsonify(data), status

@app.route("/weather/hourly")
def hourly_weather():
    data = get_hourly_forecast()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
