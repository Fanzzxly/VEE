# config.py | VEE Configuration

DISPLAY_MODE = "potrait"

DISPLAY_PRESET = {
    "small": {
        "scale": 0.6,
        "width": 800,
        "height": 480,
        "icon_size": 48
    },
    "large": {
        "scale": 1.0,
        "width": 1920,
        "height": 1080,
        "icon_size": 96
    },
    "potrait": {
        "scale": 0.72,
        "width": 612,
        "height": 880,
        "icon_size": 64
    }
}

CURRENT_DISPLAY = DISPLAY_PRESET[DISPLAY_MODE]

# Paths
CURRENT_WEATHER_FILE = 'data/current_weather.json'
FORECAST_CACHE_FILE = 'data/forecast_cache.json'
ICON_FOLDER = '/static/assets/weather_icon'
WALLPAPER_FOLDER = '/static/assets/wallpaper'

# User info
USERNAME = "Fanzzxly"

# Greeting (default/fallback)
GREETING_TEXT = {
    "morning": f"Oh look, it’s morning. What a surprise.<br>Totally didn’t see that coming for the thousandth time<br>Morning {USERNAME}..",
    "afternoon": f"Selamat siang, {USERNAME}.",
    "evening": f"Selamat malam, {USERNAME}."
}
