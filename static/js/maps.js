'use strict';

console.log('Hello, my favorite world!');



console.log('Hello, my favorite map!');



function initMap() {
  const lat = Number(document.querySelector('#lat').innerText)
  const lng = Number(document.querySelector('#lon').innerText)

  const propCoords = {
    lat: lat,
    lng: lng,
  };

  const basicMap = new google.maps.Map(document.querySelector('#map'), {
    center: propCoords,
    zoom: 11,
  });

  const homeMarker = new google.maps.Marker({
    position: propCoords,
    title: 'Home',
    map: basicMap,
  });

  homeMarker.addListener('click', () => {
    alert('Hi!');
  });
};
