function updateGreeting() {
  const hour = new Date().getHours();
  let greet = "Halo";
  if (hour < 12) greet = "Oh look, it’s morning. What a surprise.<br>Totally didn’t see that coming for the thousandth time<br>Morning Fanzzxly..";
  else if (hour < 18) greet = "Midday check-in: brain’s lagging, stomach’s growling, spirit’s ghosting.<br> Hi, Fanzzxly.";
  else greet = "Oh great, it’s night.<br> Another day wasted like a pro.<br> Sweet dreams, Fanzzxly.";
  document.getElementById('greeting').innerHTML = greet;
}

updateGreeting();


