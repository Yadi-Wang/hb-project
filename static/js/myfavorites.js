'use strict';

console.log('Hello, my favorite world!');


let showPhotos = document.querySelectorAll('[id^=propertyid-filed]');

showPhotos.forEach(function (showPhotos) {
    showPhotos.addEventListener('click', (evt) => {    
console.log(showPhotos.innerHTML)
console.log("Here is the photo");
const options = {
    method: 'GET',
    headers: {
        'X-RapidAPI-Host': 'realty-in-us.p.rapidapi.com',
        'X-RapidAPI-Key': 'ad06cc1ec2mshf405726e1df988dp12ad4bjsn96ac2fc85cba'
        }};
const queryString = showPhotos.innerHTML;
console.log(queryString)

const url = `https://realty-in-us.p.rapidapi.com/properties/v2/detail?property_id=${queryString}`;
fetch(url, options)
    .then((response) => response.json())
    .then((result) => result.properties[0].photos[0]["href"])
    .then((photosrc) => document.querySelector(`#photo-filed-${queryString}`).src= photosrc)
    .catch(err => console.error(err));
});
});


