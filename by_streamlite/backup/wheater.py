import streamlit as st
from datetime import datetime
from wheater_utils import get_forecast

# Ambil data dari cache/fetch
forecast_data = get_forecast()
if not forecast_data:
    st.error("Gagal memuat data cuaca.")
    st.stop()

hourly_data = forecast_data["hourly"][:12]

# UI Layout
st.set_page_config(page_title="Forecast 12 Jam", layout="wide")
st.markdown("<h2 style='text-align: center;'>⏰ Forecast 12 Jam ke Depan (Live + Cache)</h2>", unsafe_allow_html=True)

# Tampilkan 12 jam ke depan
cols = st.columns(len(hourly_data))
for i, col in enumerate(cols):
    dt = datetime.fromtimestamp(hourly_data[i]["dt"]).strftime("%I %p").lstrip("0")  # Gunakan %I bukan %-I (kompatibel Windows)
    temp = f"{round(hourly_data[i]['temp'])}°C"
    icon_code = hourly_data[i]["weather"][0]["icon"]
    icon_url = f"http://openweathermap.org/img/wn/{icon_code}.png"

    with col:
        st.image(icon_url, width=60)
        st.markdown(f"<h4 style='text-align: center;'>{dt}</h4>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center;'>{temp}</p>", unsafe_allow_html=True)

# Info waktu cache terakhir (opsional)
cached_time = forecast_data.get("hourly_cached_at")
if cached_time:
    readable_time = datetime.fromtimestamp(cached_time).strftime("%d %b %Y %H:%M")
    st.markdown(f"<p style='text-align: center; font-size:14px;'>📦 Cache terakhir diupdate: {readable_time}</p>", unsafe_allow_html=True)

