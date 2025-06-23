# 📦 VEE Changelog

## ✨ Version `v0.3` – *“Modular Weather Intelligence”*

**Release Date:** 2025-06-23  
**Status:** ✅ Stable & Modular  
**Tagline:**  
> *"VEE v0.3 — Now aware of the weather.  
But still judging you silently."*

---

### 🚀 Major Features

- ✅ **Real-time Weather Integration**
  - Fetch data dari OpenWeather API (`OneCall v3.0`)
  - Data `current` dan `hourly` dipisah dan disimpan ke `current.json` & `forecast.json`

- 🔁 **Automatic Periodic Fetching**
  - Implementasi `threading` untuk fetch otomatis setiap 30 menit via `run_periodically()`

- 🧠 **Data Parsing Logic**
  - `current_parser.py` untuk current weather
  - `forecast_parser.py` untuk hourly forecast
  - Struktur JSON dibersihkan untuk frontend consumption

- 📁 **Modular File Structure**
  - Folder `wheater_logic/` sebagai pusat logic backend
  - Folder `data/` untuk menyimpan cache JSON

- 🌐 **Flask API Endpoint**
  - `/weather`: menyajikan current weather JSON
  - `/weather/hourly`: menyajikan hourly forecast JSON
  - `config.py` untuk lokasi, units, dan metadata tampilan

---

### 💡 UI Frontend Enhancement

- 🪟 **HTML Modular (Jinja2)**
  - `clock.html`, `greeting.html`, `current_weather.html`, `hourly_weather.html` terpisah
  - `index.html` sebagai komposer utama UI

- 💡 **Modular JavaScript**
  - `clock.js`, `greeting.js`, `current_weather.js`, `forecast_weather.js`, `wallpaper.js`
  - Auto-refresh cuaca via `fetch()` per 1 menit tanpa reload halaman

---

### 🔧 Developer Improvements

- `.env` digunakan untuk API key & koordinat lokasi
- `python-dotenv` digunakan untuk keamanan konfigurasi
- Struktur sudah siap integrasi ke komponen lanjut: STT, TTS, intent AI, gesture, dan VAD

---

### 🧠 Next Planned (v0.4 Preview)

- 🔊 Text-to-Speech voice feedback
- 🗣️ Basic intent recognition
- 📦 AudioManager centralization
- 🎯 Proactive UI behavior (sensor-aware)
- 🤝 Integrasi awal dengan gesture/camera atau PIR sensor

---

### ✅ Conclusion

> `v0.3` bukan hanya modularisasi—ini adalah pondasi VEE sebagai **entitas berbasis cuaca yang hidup dan adaptif.**  
> Sistem siap menerima modul lanjutan tanpa beban, dan semua struktur sudah scalable.
