'use strict';

console.log('Hello, my favorite restaurants!');

const options = {
	method: 'GET',
	headers: {
		'X-RapidAPI-Host': 'restaurants-near-me-usa.p.rapidapi.com',
		'X-RapidAPI-Key': 'ad06cc1ec2mshf405726e1df988dp12ad4bjsn96ac2fc85cba'
	}
};




const zip = document.querySelector('#zip').innerText;

fetch(`https://restaurants-near-me-usa.p.rapidapi.com/restaurants/location/zipcode/${zip}/0`, options)
	.then((response) => response.json())
	.then((result) => result.restaurants)
    .then(show(data));
    
    function show(data) {
        let tab =
            `<tr>
            <th>Name</th>
            <th>Address</th>
            </tr>`;

        for (let r of result.restaurants){
            tab += `<tr>
            <td>${r.restaurantName}</td>
            <td>${r.address}</td>
            </tr>`;
        }
        document.querySelector('#restaurants').innerHTML= tab
    }

    
    // .then((restaurant) => document.querySelector('#restaurants')= restaurant)




