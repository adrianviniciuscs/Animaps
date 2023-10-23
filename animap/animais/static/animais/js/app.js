// map

var mymap = L.map("mapid").setView([-6.1124964, -38.2062628], 13);

L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
  maxZoom: 19,
  attribution:
    '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
}).addTo(mymap);

var endereçoLocal = document.querySelector("#localização");

var endereços = document.querySelector("#endereços");

var endereço = document.querySelector("#id_endereço");
var coordX = document.querySelector("#id_coordX");
var coordY = document.querySelector("#id_coordY");

var marker = null;
var clickendr = "";

mymap.on("click", function (e) {
  if (marker) {
    mymap.removeLayer(marker);
  }
  var lat = e.latlng.lat;
  var lng = e.latlng.lng;
  url = `https://nominatim.openstreetmap.org/reverse?format=jsonv2&lat=${lat}&lon=${lng}`;

  fetch(url)
    .then((response) => response.json())
    .then((data) => {
      endereço.value = data.display_name;
    });

  console.log(clickendr);
  coordX.value = lat;
  coordY.value = lng;

  marker = L.marker([lat, lng]).addTo(mymap);
});

function mostrarEndereços() {
  endereços.innerHTML = "";
  if (addressData.length > 0) {
    addressData.forEach((endereço) => {
      nomeEndereço = endereço.display_name.replace('"', " ");
      endereços.innerHTML +=
        "<div class='hover:bg-blue-100 focus:bg-blue-100 focus-outline-none border focus:border-blue-500' onclick='selectEndereço(" +
        endereço.lat +
        "," +
        endereço.lon +
        "," +
        '"' +
        nomeEndereço +
        '"' +
        ")'>" +
        endereço.display_name +
        "</div>";
    });
  }
}

function selectEndereço(x, y, endr) {
  endereço.value = endr;
  coordX.value = x;
  coordY.value = y;
  mymap.flyTo([x, y], 16);
  marker.closePopup();
  marker.setLatLng([x, y]);
  marker.closePopup();
}

function acheEndereço() {
    const viewbox = "-38.265381,-6.166838,-38.147278,-6.060672";
    const url = `https://nominatim.openstreetmap.org/search?format=json&limit=5&viewbox=${viewbox}&bounded=1&q=${endereçoLocal.value}`;
    fetch(url)
    .then((response) => response.json())
    .then((data) => (addressData = data))
    .then((mostrarEndereço) => mostrarEndereços());
}
