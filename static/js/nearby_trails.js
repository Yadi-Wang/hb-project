'use strict';

console.log('Hello, my favorite restaurants!');

// let showRes = document.querySelectorAll('#restaurants');

console.log("Here is the photo");

const optionsTrial = {
    method: 'GET',
    headers: {
        'X-RapidAPI-Key': 'ad06cc1ec2mshf405726e1df988dp12ad4bjsn96ac2fc85cba',
        'X-RapidAPI-Host': 'trailapi-trailapi.p.rapidapi.com'
    }
};

const latitudeTrail = Number(document.querySelector('#lat').innerText)
const longitudeTrail = Number(document.querySelector('#lon').innerText)

// const latitudeTrail = 37.58572
// const longitudeTrail = -122.020543

fetch(`https://trailapi-trailapi.p.rapidapi.com/activity/?lat=${latitudeTrail}&limit=5&lon=${longitudeTrail}&radius=25&q-activities_activity_type_name_eq=hiking`, optionsTrial)
    .then(function(response){
        return response.json()
    })
    // .then(function(data){
    //     console.log(data)
    // })
    .then(function(outdoors){
        let placeholderTrail = document.querySelector('#outdoors');
        let out = "";
        for (const outdoor of Object.values(outdoors)){
            out +=`
                <tr>
                    <td>${outdoor.name}</td>
                    <td>${outdoor.city} ${outdoor.state}</td>
                    <td>${outdoor.description}</td>
                </tr>
            `;
        }
        placeholderTrail.innerHTML = out;
    })

