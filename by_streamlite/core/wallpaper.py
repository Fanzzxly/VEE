import base64
import streamlit as st

def get_base64_wallpaper(file_path="assets/wallpaper/wallpaper.jpg"):
    """Mengambil gambar wallpaper dan mengubah ke base64."""
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

def apply_background(base64_img):
    """Mengaplikasikan background dan gaya CSS default UI."""
    st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{base64_img}");
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