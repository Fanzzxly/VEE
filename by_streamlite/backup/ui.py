import streamlit as st
from datetime import datetime
from streamlit_autorefresh import st_autorefresh
import requests
import base64

# ========== KONFIG ==========
API_KEY = "694d6a304f314457888bf9a48f724abe"
LAT = 33.33444
LON = 129.86533
UNITS = "metric"
# =============================

def get_base64_of_file(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

def get_weather():
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={API_KEY}&units={UNITS}"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        temp = round(data["main"]["temp"])
        desc = data["weather"][0]["description"].capitalize()
        icon = data["weather"][0]["icon"]
        city = data["name"]
        return f"{temp}°C - {desc}", f"http://openweathermap.org/img/wn/{icon}@2x.png", city
    else:
        return "Cuaca tidak tersedia", "", ""

# Setup UI
st.set_page_config(page_title="VEE Mirror", layout="wide", initial_sidebar_state="collapsed")
bg_img = get_base64_of_file("wallpaper.jpg")
st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{bg_img}");
        background-size: cover;
        background-position: center;
        color: white;
        font-family: 'Orbitron', sans-serif;
    }}
    .clock {{
        font-size: 80px;
        text-align: center;
        margin-top: 20px;
        text-shadow: 0 0 20px #00f0ff;
    }}
    .weather {{
        text-align: center;
        font-size: 24px;
        margin-top: 20px;
        text-shadow: 0 0 10px #00ffee;
    }}
    </style>
""", unsafe_allow_html=True)

# Auto-refresh tiap 1 menit
st_autorefresh(interval=60000, key="refresh")

# Jam
now = datetime.now().strftime("%H:%M")
st.markdown(f"<div class='clock'>{now}</div>", unsafe_allow_html=True)

# Cuaca
weather_info, icon_url, city = get_weather()
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    st.markdown(f"<div class='weather'>⛅ {weather_info}<br>{city}</div>", unsafe_allow_html=True)
    if icon_url:
        st.image(icon_url, width=80)
