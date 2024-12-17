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

// function hideFooter() {
//     footer.style.display = 'none';
// }

itemOne.onwheel = changeBackground;
itemFour.onkeydown = submitSearch;
itemFive.onsubmit = printSuccessful;

let footer = document.querySelector('.store-footer');
let isScrolling;

// Function to hide the footer
function hideFooter() {
    footer.style.display = 'none';
}

// Function to show the footer
function showFooter() {
    footer.style.display = 'block';
}

// Listen for scroll events
window.addEventListener('scroll', function () {
    hideFooter();

    // Clear the timeout if it's already set
    clearTimeout(isScrolling);

    // Set a timeout to run after scrolling ends
    isScrolling = setTimeout(function () {
        showFooter();
    }, 100); // Adjust the delay as needed
});



