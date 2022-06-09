'use strict';

console.log('Hello, this is yelp!');

const URL = 'https://cors-anywhere.herokuapp.com/https://api.yelp.com/v3/businesses/search?term=food&location=92697';
const API_KEY = '6qRADsa6AXsVqtRhgedgNWqJGZUrK_KeebIKODou-F0Srx7ZdV4tjE9O4YDFpRzYZHtwiIi8OsUMqXB28kRmZZnHJv5nGBcKJakmUdNwV8_3c7oNOt4MdeAq30ctYnYx';

    const req = {URL, 
        method: 'GET',
        headers: {
        'Authorization': 'Bearer 6qRADsa6AXsVqtRhgedgNWqJGZUrK_KeebIKODou-F0Srx7ZdV4tjE9O4YDFpRzYZHtwiIi8OsUMqXB28kRmZZnHJv5nGBcKJakmUdNwV8_3c7oNOt4MdeAq30ctYnYx',
        'Content-Type': 'application/json'
        }
    };

        fetch (req)
            .then(response => response.json())
            .then(result =>console.log(result))