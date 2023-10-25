// render map
var mymap = L.map("mapid").setView([-6.1124964, -38.2062628], 13);

L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
  maxZoom: 19,
  attribution:
    '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
}).addTo(mymap);

var url = "/animaisApi/";

fetch(url)
  .then((response) => response.json())
  .then((data) => {
    var animais_resolvidos = data.filter(animal => animal.state === "Resgatado" || animal.state === "Não Localizado");
    mostrarAnimais(animais_resolvidos);
  });

function mostrarAnimais(animais) {
  animais.forEach((animal) => {
    pop = L.popup({
      closeOnClick: true,
    }).setContent("<img src=" + animal.foto + ' style="width: 150px">');

    coords = [animal.coordX, animal.coordY];
    marker = L.marker(coords).addTo(mymap).bindPopup(pop);

    tooltip = L.tooltip({
      permanent: true,
    }).setContent(animal.descriçao);
  });
}

animalinfo = document.querySelectorAll(".animalinfo");

function centralizarAnimal() {
  animais.forEach((animal, index) => {
    animalinfo[index].addEventListener("click", (event) => {
      mymap.flyTo([animal.coordX, animal.coordY], 17);
    });
  });
}

