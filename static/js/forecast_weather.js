import { FORECAST_REFRESH_INTERVAL } from "./config.js";

async function updateForecastHourly() {
  try {
    const res = await fetch('/weather/hourly');
    const data = await res.json();

    const container = document.getElementById('forecast-hourly-list');
    if (!container) return;
    container.innerHTML = '';

    data.forEach(item => {
      const el = document.createElement('div');
      el.className = 'forecast-item';
      el.innerHTML = `
        <div>${item.time}</div>
        <img src="/static/assets/weather_icon/${item.icon}.png" alt="${item.icon}">
        <div>${item.pop}%</div>
      `;
      container.appendChild(el);
    });

  } catch (err) {
    console.error("Gagal fetch forecast hourly:", err);
  }
}

updateForecastHourly();
setInterval(updateForecastHourly,FORECAST_REFRESH_INTERVAL);