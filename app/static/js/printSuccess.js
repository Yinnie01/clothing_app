// Changing the header background to opaque while scrolling.

let itemOne = document.getElementById("body");
let itemTwo = document.getElementById("header");
let itemThree = document.getElementById("footer");
let itemFive = document.getElementById("upload");

function changeBackground() {
    itemTwo.style.backgroundColor = "rgba(241, 233, 164)";
    itemThree.style.backgroundColor = "rgba(241, 233, 164)";
}

function printSuccessful(event) {
    // event.preventDefault();
    console.log('Upload Successful!');
    // setTimeout(() => {
    //     itemFive.submit(); // Submit the form after a delay
    // }, 1000);
}

itemOne.onwheel = changeBackground;
itemFive.onsubmit = printSuccessful;


