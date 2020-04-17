//alert('Hello World.');
//console.log("Hi!");
//console.error("Error msg!");

//-----------------------------------------------Variables--------------------------------------------//
/*
    three ways of declaring variables: var const and let:
        var: globaly scoped (dont use as much anymore)
        const: constant variables (cannont change)
        var: can change
*/

//const gravity = 9.8;
//let age = 23;

//-----------------------------------------------Data Type--------------------------------------------//
/*
    String, numbers, bool, null, undefined
*/

const name = "Bob";
var age = 40;
var isHuman = true;
var null_val = null; 
var undefined_val = undefined;

console.log(typeof name);
console.log(typeof age);
console.log(typeof isHuman);
console.log(typeof null_val);
console.log(typeof undefined_val);


//-----------------------------------------------Strings----------------------------------------------//
// concatination
//  two ways
//      old:
console.log("My name is " + name + " and I am " + age);

//      new:
console.log(`My name is ${name} and I am ${age}`);

// legal
var hello = `My name is ${name} and I am ${age}`;
console.log(hello);

// len of string
var human = "Bill";
console.log(`${name} length == ${name.length}`);

// other funtions (or methods in this case)
console.log(name.toUpperCase());
console.log(name.toLowerCase());
console.log(name.substring(0, 2));
console.log(name.substring(0, 2).toUpperCase());

// splitting strings into an array
console.log(name.split(''));

// when would split come in handy? linked in skills being putting by user 
// to be made and stored as an array
var skills = "C++, Java, C, killing time";
console.log(skills.split(", ")); //, and (space)!

//-----------------------------------------------Arrays-----------------------------------------------//
// two ways of doing is
// with 'new' or with []

var numbers = new Array(1, 2, 3, 4);
console.log(numbers);

var fruits = ["Apples", "Pears", "Watermelons"];
console.log(fruits);

// data types can be mixed (crazy!)
var random = ["Bob", "Candy", 1020, 2e-10, true, null];
console.log(random);

// array accessing
console.log(fruits[0]);

// appending arrays
fruits[fruits.length] = "Banana";
console.log(fruits);

// const array can be added
const veggies = ["carrots", "lettuce", "beans"];
veggies.push("Broccolis");
console.log(veggies);

// adds to the 0th index
veggies.unshift("Onions");
console.log(veggies);

// pop! (like linked lists!)
veggies.pop();
console.log(veggies);

// checking arrays for sub array
console.log(Array.isArray(fruits));
console.log(Array.isArray("Banana"));

// getting index back
console.log(fruits.indexOf("Banana"));


//---------------------------------------Object Literals----------------------------------------------//
// check out the nested object literal! (is nested even the right word here)?
var person = {
    firstName: 'Joe',
    lastName: 'Roe',
    age: 22,
    hobbies: ['music', 'sports', 'turtles'],
    address: {
        street: "Main Street",
        city: "Boston",
        State:"MA"
    }
}

console.log(person);
console.log(person.firstName);
console.log(person.hobbies[1]);
console.log(person.address.city);

// how to pull data out and storing in varibale
var {firstName, lastName} = person;
console.log(firstName);

// for embedded objects
var {firstName, lastName, address:{city}} = person;
console.log(city);

// adding property
person.email = "joe@roe.com";
console.log(person.email);

//---------------------------------------Array of Objects---------------------------------------------//
var todos = [
    {
        id: 1,
        text: "Take Out Trash",
        completed: true,
    },
    {
        id: 2,
        text: "Meeting",
        completed: true,
    },
    {
        id: 3,
        text: "Appointment",
        completed: false,
    }
]

console.log(todos[1].text);

// converting into JSON
var todoJSON = JSON.stringify(todos);
console.log(todoJSON);

//-------------------------------------------Loops----------------------------------------------------//

for (let i = 0; i < 10; i++)
{
    console.log(i);
}

let i = 0;
while(i < 10)
{
    console.log(i)
    i += 2;
}

for (let todo of todos)
{
    console.log(todo.text);
}

//-------------------------------------------High Order Array Methods---------------------------------//
// forEach, map, filter

// forEach
todos.forEach(function(todo)
    {
        console.log(todo.text);
    }
);

// map
let todoText = todos.map(function(todo)
    {
        return todo.text;
    }
);
console.log(todoText[1]);

let todoCompleted = todos.filter(function(todo)
    {
        return todo.completed == true;
    }
);
console.log(todoCompleted);

// only getting the text back for completed
let todoCompletedText = todos.filter(function(todo)
    {
        return todo.completed == true;
    }
).map(function(todo)
    {
        return todo.text;
    }
)

console.log(todoCompletedText);

//-------------------------------------------Conditionals---------------------------------------------//

let x = 10;

if (x == 10)
{
    console.log("x == 10");
}

// ===
// checks for data AND data type
// therefore you should use === most of the times

x = "10"
if (x == 10)
{
    console.log("10 == 10");
}
if (x === 10)
{
    console.log("string (10) == 10");
}
if (x === "10")
{
    console.log("string 10 == string 10");
}

// || (or) && (and)

x = 100;
let y = 50;

if (x === y || x > y)
{
    console.log("Use less than of equal to next time :)");
}

if (x === y && x > y)
{
    console.log("this should not print");
}

// turnary! WOOOOO!

x = 10;
let thisIsAwesome = (x == 10)? 'YES IT IS!' : 'No... it is not.';
console.log("Is this awesome? " + thisIsAwesome);

let roses = "Blue";

// switch statements
switch(roses)
{
    case "Red":
        console.log("Nope.");
        break;
    
    case "Violet":
        console.log("Try again...");
        break;
    
    case "Blue":
        console.log("This is C code and so are you.");
        break;
    default:
        console.log("gravy is good for your skin.");
}

//-------------------------------------------Funtions-------------------------------------------------//

function addNums(a, b)
{
    return a + b;
}

console.log(addNums(100, 150));

function factorial(n)
{
    if (n < 2)
        return 1;

    return n * factorial(n - 1);
}

for (let i = 0; i <= 10; i++)
    console.log(`${i} factorial = ${factorial(i)}`);

function power(a, b)
{
    let i, total = 1;
    for (i = 0; i < b; i++)
        total = total * a;
    
    return total;
}

console.log(power(2, 3));
console.log(power(2,16));

// there can be default parameters in funtions
function square(a, b = 2)
{
    let i, total = 1;
    for (i = 0; i < b; i++)
        total = total * a;
    
    return total;
}

console.log(square(3));
console.log("Buggy square " + square(3,3));

// arrow funtions

const multiply = (a, b) =>
{
    return a * b;
}

console.log(multiply(4,9));

// similarly 

const multi = (a, b) => a * b;

console.log(multi(4,9));