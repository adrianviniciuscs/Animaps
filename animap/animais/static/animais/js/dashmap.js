var mymap = L.map("mapid").setView([-6.1124964, -38.2062628], 13);

L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
  maxZoom: 19,
  attribution:
    '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
}).addTo(mymap);

const coordYElement = document.querySelector('.coordY');
const coordYText = coordYElement.textContent;
const coordYValue = parseFloat(coordYText.split(': ')[1]);

const coordXElement = document.querySelector('.coordX');
const coordXText = coordXElement.textContent;
const coordXValue = parseFloat(coordXText.split(': ')[1]);

marker = L.marker([coordXValue, coordYValue]).addTo(mymap);
