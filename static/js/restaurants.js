'use strict';

console.log('Hello, my favorite restaurants!');

// let showRes = document.querySelectorAll('#restaurants');

console.log("Here is the photo");





async function start() {
    const options = {
        method: 'GET',
        headers: {
            'X-RapidAPI-Key': 'ad06cc1ec2mshf405726e1df988dp12ad4bjsn96ac2fc85cba',
            'X-RapidAPI-Host': 'travel-advisor.p.rapidapi.com'
        }
    };
    const latitude = 37.733795
    const longitude = -122.446747
    
    const response = await fetch(`https://travel-advisor.p.rapidapi.com/restaurants/list-by-latlng?latitude=${latitude}&longitude=${longitude}&limit=5&currency=USD&distance=2&open_now=false&lunit=km&lang=en_US`, options);
    const data = await response.json()
    // createRestaurantList(data.data)
    const restaurants = await data.data
    console.log(restaurants)



    for (const restaurant of restaurants){
        const restrName = restaurant['name'];
        createRestaurantList(restrName)
        };

    function createRestaurantList(restrName) {
        document.querySelector('#restaurants').append(restrName)
        }
}

start()



// function createRestaurantList(restaurants) {
//     document.querySelector('#restaurants').innerHTML= restaurants
// }