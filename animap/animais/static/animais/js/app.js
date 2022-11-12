var endereçoLocal = document.querySelector('#localização');

var endereços = document.querySelector('#endereços');

var endereço = document.querySelector('#id_endereço');
var coordX = document.querySelector('#id_coordX');
var coordY = document.querySelector('#id_coordY');

function mostrarEndereços(){
    endereços.innerHTML = ""
    if (addressData.length > 0) {
        addressData.forEach(endereço => {
            nomeEndereço = endereço.display_name.replace('"' , " ")
            endereços.innerHTML += "<div class='results' onclick='selectEndereço(" + endereço.lat + "," +  endereço.lon + "," + '"' + nomeEndereço + '"' + ")'>" + endereço.display_name + "</div>"
        });
    };
};

function selectEndereço(x, y, endr){
    endereço.value = endr
    coordX.value = x
    coordY.value = y
    mymap.flyTo([x,y], 16)
    marker.closePopup()
    marker.setLatLng ([x,y])
    marker.closePopup()
};

function acheEndereço(){
    url = "https://nominatim.openstreetmap.org/search?format=json&limit3&q=" + endereçoLocal.value 
    fetch(url)
            .then(response => response.json())
            .then(data => addressData = data)
            .then(mostrarEndereço => mostrarEndereços())
};


// map

var mymap = L.map('mapid').setView([-6.1124964, -38.2062628], 13);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(mymap);
