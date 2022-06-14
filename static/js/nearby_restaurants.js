'use strict';

console.log('Hello, my favorite restaurants!');

// let showRes = document.querySelectorAll('#restaurants');

console.log("Here is the photo");

const options = {
    method: 'GET',
    headers: {
        'X-RapidAPI-Key': 'ad06cc1ec2mshf405726e1df988dp12ad4bjsn96ac2fc85cba',
        'X-RapidAPI-Host': 'travel-advisor.p.rapidapi.com'
    }
};
const latitude = Number(document.querySelector('#lat').innerText)
const longitude = Number(document.querySelector('#lon').innerText)

// const latitude = 37.58572
// const longitude = -122.020543

fetch(`https://travel-advisor.p.rapidapi.com/restaurants/list-by-latlng?latitude=${latitude}&longitude=${longitude}&limit=5&currency=USD&distance=2&open_now=false&lunit=km&lang=en_US`, options)
    .then(function(response){
        return response.json()
    })
    .then(function(data){
        return data.data 
    })

    // .then (function(data){
    //     console.log(data)
    // })
    .then(function(restaurants){
        let placeholder = document.querySelector('#restaurants');
        let out = "";
        for (let restaurant of restaurants){
            out +=`
                <tr>
                    <td>${restaurant.name}</td>
                    <td>${restaurant.address}</td>
                    <td>${restaurant.distance_string}</td>
                </tr>
            `;
        }
        placeholder.innerHTML = out;
    })





