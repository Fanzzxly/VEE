from datetime import datetime
import streamlit as st

def show_clock():
    now = datetime.now().strftime("%H:%M")
    st.markdown(f"<div class='clock'>{now}</div>", unsafe_allow_html=True)
