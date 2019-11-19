//thank god for single line comments
//this is just a random variblre setting
// btw randomly foundout how to write to console.


console.log("hi!");

var x = 50, y = 30;
console.log(x + y); // same as java!

var str = "strings kind of work the same as well!";
console.log(str);

//will this work without "var"?
x = 40;
console.log(x);

//-----------------------------------------------------------------------------
// Strings
//-----------------------------------------------------------------------------


//why doesnt str work then?
//lets go deeper in str:

var str = "new string!";
console.log(str.length + " this is the length of the strong!"); // same as java! :)

console.log(str.toUpperCase());

//-----------------------------------------------------------------------------
// Math.
//-----------------------------------------------------------------------------

var number = 44.55;
console.log(Math.round(number)); // rounds to int

// random numbers
console.log(Math.random()); // generates  number from 0-1

// this should get a rand double from 0-100.0 round is to make it an int
// kind of an ungly way to rand if you ask me
// C will always be king
for(var i = 0; i < 100; i++) // thank God for C for loops!
  console.log(Math.round(Math.random() * 100));

//-----------------------------------------------------------------------------
// Booleans
//-----------------------------------------------------------------------------

var Bool = true; // vary bad :( but Bool is true! use lowercase
if(Bool)
  console.log("yup it's true!");

//this is supper bizzar but neat
var number = 40, other = 50;

console.log(number === other); // === the comparison LOL!
