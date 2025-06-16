# 📦 VEE Changelog

## [v0.2] – 2025-06-16
### ✨ Refactor + Display Adaptif + Configurable Layout

#### 🔧 Core Improvements
- Refactored project structure, added `config.py` to centralize key parameters
- Injected `cfg` via Flask `context_processor` for dynamic UI control
- Organized display presets: `small`, `portrait`, `large` with scale & icon size

#### 📐 Scalable UI System
- Implemented CSS variables `--scale` and `--icon-size` for responsive design
- All major text elements now scale dynamically based on mode
- Layout previewed and tested for 612 × 880 px (target display)

#### 🌦️ Weather Integration
- Replaced external `icon_url` with local icon mapping (`icon`)
- Displayed weather icon dynamically from `/static/assets/weather_icon/`
- Weather icon now responsive using CSS scaling

#### 🎨 Visual & Style Enhancements
- Applied `calc()` to all key font sizes (`clock`, `date`, `greeting`, `weather`)
- Removed hardcoded width/height from HTML for cleaner DOM structure

#### 📂 File & Structure Clean-up
- Updated `app.py` to use `CURRENT_WEATHER_FILE` from config
- Clean separation of logic, data, and style
- HTML and CSS now agnostic to specific screen size

---

## ✅ Status: Stable  
> Refactor complete, scalable engine implemented.  
> Ready for forecast modules and animated UI in v0.3.