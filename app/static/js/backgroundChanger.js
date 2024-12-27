// Changing the header background to opaque while scrolling.

let itemOne = document.getElementById("body");
let itemTwo = document.getElementById("header");
let itemThree = document.getElementById("footer");
let itemFour = document.getElementById("search");
let itemFive = document.getElementById("upload");
let itemSix = document.querySelector('.store-footer');

function changeBackground() {
    itemTwo.style.backgroundColor = "rgba(241, 233, 164)";
    itemThree.style.backgroundColor = "rgba(241, 233, 164)";
}

function changeCursor() {
    itemFour.style.cursor = 'pointer';
}

function submitSearch(event) {
    if (event.key === 'Enter') {
        this.submit();
    }
}

function printSuccessful(event) {
    event.preventDefault();
    console.log('Upload Successful!');
    setTimeout(() => {
        itemFive.submit(); // Submit the form after a delay
    }, 1000);
}



itemOne.onwheel = changeBackground;
itemFour.onkeydown = submitSearch;
itemFive.onsubmit = printSuccessful;


