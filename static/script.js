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
  const hari = ['Minggu','Senin','Selasa','Rabu','Kamis','Jumat','Sabtu'];
  const bulan = ['Januari','Februari','Maret','April','Mei','Juni','Juli','Agustus','September','Oktober','November','Desember'];
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
  if (hour < 12) greet = "Selamat pagi, Fanza.";
  else if (hour < 18) greet = "Selamat siang, Fanza.";
  else greet = "Selamat malam, Fanza.";
  document.getElementById('greeting').textContent = greet;
}
updateGreeting();

// Fetch weather data
async function updateWeather() {
  try {
    const res = await fetch('/weather');
    const data = await res.json();
    document.getElementById('weather').textContent = `${data.temp}°C - ${data.desc} - ${data.city}`;
  } catch (err) {
    document.getElementById('weather').textContent = "(Gagal memuat cuaca)";
  }
}
updateWeather();
setInterval(updateWeather, 5 * 60 * 1000); // refresh tiap 5 menit