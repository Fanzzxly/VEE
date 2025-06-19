
import { WEATHER_REFRESH_INTERVAL } from './config.js';

async function updateWeather() {
  try {
    const res = await fetch('/weather');
    const data = await res.json();

    // Update teks cuaca
    document.getElementById('weather').textContent = `${data.temp}°C, ${data.desc} - ${data.city}`;
   

  } catch (err) {
    document.getElementById('weather').textContent = "(Gagal memuat cuaca)";
    console.log("icon from JSON:", data.icon);
  }
}
updateWeather();
setInterval(updateWeather, WEATHER_REFRESH_INTERVAL)

