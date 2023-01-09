var mymap = L.map("mapid").setView([-6.1124964, -38.2062628], 13);

L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
  maxZoom: 19,
  attribution:
    '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
}).addTo(mymap);

const coordXElement = document.querySelector('.coordX');
const coordYElement = document.querySelector('.coordY');

const coordX = Number(coordXElement.textContent);
const coordY = Number(coordYElement.textContent);

marker = L.marker([coordX, coordY]).addTo(mymap);