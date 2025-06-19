import { CLOCK_REFRESH_INTERVAL } from "./config.js";

function updateClock() {
  const now = new Date();
  const hours = String(now.getHours()).padStart(2, '0');
  const minutes = String(now.getMinutes()).padStart(2, '0');
  document.getElementById('clock').textContent = `${hours}:${minutes}`;
}

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

updateClock();
updateDate();
setInterval(updateClock, CLOCK_REFRESH_INTERVAL);
