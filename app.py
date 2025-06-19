from flask import Flask, render_template, jsonify
from config import CURRENT_DISPLAY
from current_parser import get_current_weather
from forecast_parser import get_hourly_forecast, get_daily_forecast

app = Flask(__name__)

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

@app.route('/forecast/hourly')
def forecast_hourly():
    data = get_hourly_forecast()
    status = 500 if "error" in data else 200
    return jsonify(data), status

@app.route('/forecast/daily')
def forecast_daily():
    data = get_daily_forecast()
    status = 500 if "error" in data else 200
    return jsonify(data), status


if __name__ == '__main__':
    app.run(debug=True)
