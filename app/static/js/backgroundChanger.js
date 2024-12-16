// Changing the header background to opaque while scrolling.

let itemOne = document.getElementById("body");
let itemTwo = document.getElementById("header");
let itemThree = document.getElementById("footer");
let itemFour = document.getElementById("search");

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

itemOne.onwheel = changeBackground;
// itemFour.onmouseover = changeCursor;
itemFour.onkeydown = submitSearch;


