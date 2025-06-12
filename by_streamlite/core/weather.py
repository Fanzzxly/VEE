import streamlit as st
from datetime import datetime
from utils.wheater_utils import get_forecast

def show_forecast_12_hour():
    forecast_data = get_forecast()
    if not forecast_data:
        st.error("Gagal memuat data cuaca.")
        return

    hourly_data = forecast_data["hourly"][:12]

    st.markdown("<h2 style='text-align: center;'>⏰ Forecast 12 Jam ke Depan</h2>", unsafe_allow_html=True)

    cols = st.columns(len(hourly_data))
    for i, col in enumerate(cols):
        dt = datetime.fromtimestamp(hourly_data[i]["dt"]).strftime("%I %p").lstrip("0")
        temp = f"{round(hourly_data[i]['temp'])}°C"
        icon_code = hourly_data[i]["weather"][0]["icon"]
        icon_url = f"http://openweathermap.org/img/wn/{icon_code}.png"

        with col:
            st.image(icon_url, width=60)
            st.markdown(f"<h4 style='text-align: center;'>{dt}</h4>", unsafe_allow_html=True)
            st.markdown(f"<p style='text-align: center;'>{temp}</p>", unsafe_allow_html=True)

    # Waktu terakhir cache
    cached_time = forecast_data.get("hourly_cached_at")
    if cached_time:
        readable_time = datetime.fromtimestamp(cached_time).strftime("%d %b %Y %H:%M")
        st.markdown(f"<p style='text-align: center; font-size:14px;'>📦 Cache terakhir diupdate: {readable_time}</p>", unsafe_allow_html=True)
