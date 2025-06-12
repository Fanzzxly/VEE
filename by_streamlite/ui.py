import streamlit as st
from core.wallpaper import get_base64_wallpaper, apply_background
from core.clock import show_clock
from utils.wheater_utils import get_current_weather
from core.weather import show_forecast_12_hour

# Setup halaman Streamlit
st.set_page_config(
    page_title="VEE Mirror",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Terapkan wallpaper background
bg_img = get_base64_wallpaper("assets/wallpaper/wallpaper.jpg")
apply_background(bg_img)

# Tampilkan jam digital
show_clock()

# Tampilkan cuaca saat ini
current = get_current_weather()
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    st.markdown(f"<div class='weather'>⛅ {current['info']}<br>{current['city']}</div>", unsafe_allow_html=True)

# Tampilkan forecast 12 jam ke depan
show_forecast_12_hour()