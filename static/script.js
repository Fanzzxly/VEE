// script.js | Magic Mirror v0.1

// Update clock every second
function updateClock() {
  const now = new Date();
  const hours = String(now.getHours()).padStart(2, '0');
  const minutes = String(now.getMinutes()).padStart(2, '0');
  document.getElementById('clock').textContent = `${hours}:${minutes}`;
}
setInterval(updateClock, 1000);
updateClock();

// Update date (once)
function updateDate() {
  const now = new Date();
  const hari = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'];
  const bulan = ['January','February','March','April','May','June','July','August','September','October','November','December'];
  const day = hari[now.getDay()];
  const date = now.getDate();
  const month = bulan[now.getMonth()];
  const year = now.getFullYear();
  document.getElementById('date').textContent = `${day}, ${date} ${month} ${year}`;
}
updateDate();

// Greeting by time
function updateGreeting() {
  const hour = new Date().getHours();
  let greet = "Halo";
  if (hour < 12) greet = "Oh look, it’s morning. What a surprise.<br>Totally didn’t see that coming for the thousandth time<br>Morning Fanzzxly..";
  else if (hour < 18) greet = "Selamat siang, Fanzzxly.";
  else greet = "Selamat malam, Fanza.";
  document.getElementById('greeting').innerHTML = greet;
}
updateGreeting();

// Fetch weather data
async function updateWeather() {
  try {
    const res = await fetch('/weather');
    const data = await res.json();

    // Update teks cuaca
    document.getElementById('weather').textContent = `${data.temp}°C, ${data.desc} - ${data.city}`;

    // Update icon lokal
    document.getElementById('weather-icon').src = `/static/assets/weather_icon/${data.icon}.png`;
    document.getElementById('weather-icon').alt = data.icon;

   

  } catch (err) {
    document.getElementById('weather').textContent = "(Gagal memuat cuaca)";
    console.log("icon from JSON:", data.icon);
  }
}
updateWeather();
setInterval(updateWeather, 5 * 60 * 1000); // refresh tiap 5 menit

function setWallpaperByTime() {
  const hour = new Date().getHours();
  let timeOfDay;

  if (hour >= 5 && hour < 12) timeOfDay = 'pagi';
  else if (hour >= 12 && hour < 18) timeOfDay = 'siang';
  else if (hour >= 18 && hour < 22) timeOfDay = 'sore';
  else timeOfDay = 'malam';

  document.body.style.transition = 'background-image 1s ease-in-out';
  document.body.style.backgroundImage = `url('/static/assets/wallpaper/${timeOfDay}.jpg')`;
}

setWallpaperByTime();
