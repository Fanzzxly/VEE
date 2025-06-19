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