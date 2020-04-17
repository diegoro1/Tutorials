//-----------------------------------------------DOM--------------------------------------------------//
// Doctument Object Model

// selectors (single element, multiple elemnt)

// the window obj is the top level obj of the browser
console.log(window);


//single element
console.log(document.getElementById('my-form'));

const form = document.getElementById('my-form');
console.log(form);

// query selector
console.log(document.querySelector('.container'));


// multiple element
console.log(document.querySelectorAll('.item')); // use this
//older
console.log(document.getElementsByClassName('item')); // cant use array methods
document.getElementsByTagName('item') // same as above

var items = document.querySelectorAll('.item');
items.forEach((item) => console.log(item));

// removes h1
let h1s = document.querySelector('h1');
h1.remove();

