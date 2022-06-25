'use strict';

console.log('Hello, my favorite world!');


let likeButton = document.querySelectorAll('[id^=like-button]');



likeButton.forEach(function (likeButton){
    console.log(likeButton.value);
    // likeButton.addEventListener('click', () => {location.href = `/add_to_favorites/${likeButton.innerHTML}`;});
    likeButton.addEventListener('click', (evt) => {
        evt.preventDefault();
  
        const inputs = {
            thepropertyid: likeButton.value,
        };
        
        fetch('/add-to-favorites', {
            method: 'POST',
            body: JSON.stringify(inputs),
            headers: {
            'Content-Type': 'application/json',
            },
        })
        .then((response) => response.json())
        .then((responseJson) => {
        console.log(responseJson);
        
        if (responseJson.action == "add"){
            console.log("Add");
            likeButton.className = "btn btn-primary bi bi-heart-fill";
        } else {
            console.log("Delete");
            likeButton.className = "btn btn-primary bi bi-heart";
        };
        alert(responseJson.property);
        location.reload();
        });
    });
});
