// static/js/vee_fetch.js
function fetchWeather() {
    fetch('/weather')
        .then(res => res.json())
        .then(data => {
            document.getElementById("city").textContent = data.city;
            document.getElementById("desc").textContent = data.desc;
            document.getElementById("temp").textContent = data.temp + "°C";
            document.getElementById("icon").src = data.icon_url;
        });
}

function fetchForecast() {
    fetch('/weather/hourly')
        .then(res => res.json())
        .then(data => {
            const container = document.getElementById("forecast");
            container.innerHTML = "";
            data.forEach(item => {
                const el = document.createElement("div");
                el.innerHTML = `<b>${item.time}</b> - ${item.pop}% <img src="https://openweathermap.org/img/wn/${item.icon}.png">`;
                container.appendChild(el);
            });
        });
}

setInterval(() => {
    fetchWeather();
    fetchForecast();
}, 60000);

window.onload = () => {
    fetchWeather();
    fetchForecast();
};
