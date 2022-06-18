'use strict';

console.log('Hello, my favorite world!');

let likeButton = document.querySelectorAll('[id^=propertyid-filed]');


likeButton.forEach(function (likeButton){
    likeButton.addEventListener('click', () => {location.href = `/add_to_favorites/${likeButton.innerHTML}`;});
});

