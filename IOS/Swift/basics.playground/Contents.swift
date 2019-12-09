import UIKit

//--------------------------------------------------------------------------------------------------------
//                                        Constants and Variables
//--------------------------------------------------------------------------------------------------------

//variable: (var)
var myNumber = 10
//constant: (let)
let constNumber = 20

// same as c/java/c#
// three doubles
var x = 0.0, y = 0.0, z = 0.0

// type anotation can also be used
//var welcomeMessage: String
var welcomeMessage = "Hello!"

// this sets 3 variables to type double eventhough only the last one gets the colon
//var w, u, k: Double

// something weird but not illegal
var 🦆 = "duck"

//--------------------------------------------------------------------------------------------------------
//                                              print
//--------------------------------------------------------------------------------------------------------
print(🦆)
print(x)
print("\(x), \(y), \(z)") // print formatter \()

/*
 did you know
 you can also comment like in C :)
*/

//something different than C 🤯
/* This is the start of the first multiline comment.
 /* This is the second, nested multiline comment. */
 This is the end of the first multiline comment. */

// semicolons are also valid
var cat = "cat"; print(cat)


//--------------------------------------------------------------------------------------------------------
//                                              Integers
//--------------------------------------------------------------------------------------------------------

// int bounds
let minValue = UInt8.min // sets the constant minValue to the min of a unsigned 8 bit int (0)
let maxValue = UInt8.max // sets the constant maxValue to the max of a unsigned 8 bit int (255)


//--------------------------------------------------------------------------------------------------------
//                                              Floats
//--------------------------------------------------------------------------------------------------------

// double = 64bit
//float = 32bit

var maxMoney = Double.greatestFiniteMagnitude // i wish
print("maxMoney: \(maxMoney)")


//--------------------------------------------------------------------------------------------------------
//                                     Type safety TypeInference
//--------------------------------------------------------------------------------------------------------

// an insanity check
var edgyNumber = 23
// this doesnt work
//edgyNumber = 2.3
// edgyNumber is assumed to be an int from declaration

//better approach
var superEdgyNumber = 23.0
superEdgyNumber = 2.3

//--------------------------------------------------------------------------------------------------------
//                                     Numerical Litertals
//--------------------------------------------------------------------------------------------------------

/*
Integer literals can be written as:

A decimal number, with no prefix
A binary number, with a 0b prefix
An octal number, with a 0o prefix
A hexadecimal number, with a 0x prefix
*/

let decimalInt = 17
let binaryint = 0b10001
let octalInt = 0o21
let hexInt = 0x11

print(decimalInt)
print(binaryint)
print(octalInt)
print(hexInt)

// All of these floating-point literals have a decimal value of 12.1875:
let coolerNumber = 12.1875
let expCoolerNumber = 1.21875e1
let hexCoolerNumber = 0xC.3p0

// this is different and legal
let oneMillion = 1_000_000


//--------------------------------------------------------------------------------------------------------
//                                     Numeric Type Conversions
//--------------------------------------------------------------------------------------------------------

let twoThou: UInt16 = 2000
let one: UInt8 = 1
let sumAbove = twoThou + UInt16(one)


// now for int and double
let three = 3
let ptsd = 0.14159
let pi = Double(three) + ptsd
print(pi)

let intPi = Int(pi)
print(intPi)

//--------------------------------------------------------------------------------------------------------
//                                              Boolens
//--------------------------------------------------------------------------------------------------------

let rosesAreRed = true
let violetsAreBlue = false

if rosesAreRed
{
    print("WHaT a BeAuLtiFul ARt")
}

if violetsAreBlue
{
    print("HoW PerF")
}
else
{
    print("What a shame.")
}

// unlike c, putting non bools in if stataments is a nono
/*
 var DonaldTrump = 1
 if DonaldTrump
 {
 print("ILLEGALS!!!!!!")
 }
*/

//--------------------------------------------------------------------------------------------------------
//                                              Optionals
//--------------------------------------------------------------------------------------------------------

let possibleNumber = "123"
let convertedNumber = Int(possibleNumber)

// using nil
var serverResponse: Int? = 404
serverResponse = nil // use ? for possible nil values

// var surveyAnswer: String? is auto set to nil

// short exp of how this may be uselful
if convertedNumber == nil
{
    print("String contains more than just ints")
}

// neat trick to check is conversion worked (optional binding)

if let actualNumber = Int(possibleNumber)
{
    print(actualNumber)
}

// if any of the values f the optional binding are nill or any of the booleans are false
// the statement will be false
var veryTrue = true
if let optional1 = Int("4"), let oprional2 = Int("5"), veryTrue
{
    print("first optional working!: \(optional1), \(oprional2)")
}

if let optional3 = Int("hey!"), let optional4 = Int("45"), veryTrue
{
    print("This wont print :)")
}

let veryFalse = false
if let opitonal5 = Int("1"), let optinal6 = Int("1"), veryFalse
{
    print("Nope!")
}

// implicetly unwrapping optionals
// this is kind of how pointers are dereferenced in C/C++
let niceString: String? = "You are amazing!"
print(niceString!)

/* this will lead to an error as I know from dereferencing null pointers
 let badString: String? (nil by default)
 print(badString!)
*/

// this works!
let badString: String? = nil
if badString == nil
{
    print("We got this!!")
}

let badInt = Int("ohh no, this is naughty")
if badInt == nil
{
    print("this could have been bad!")
}


//--------------------------------------------------------------------------------------------------------
//                                              Assetions/preconditions
//--------------------------------------------------------------------------------------------------------

var age = 55
assert(age >= 50, "Only boomers allowed")
print(age)

// age = 30
// assert(age > 50, "Only boomers allowed")
// Assertion failed: Only boomers allowed: file basics.playground, line 239
// ^ thats what happens when boomers are invited to parties ^

// this is also nice
/*
if(age < 50)
{
    print("age > 20")
}
else
{
    assertionFailure("Dude for real, only boomers allowed!")
}
*/
// Fatal error: Dude for real, only boomers allowed!: file basics.playground, line 250
// ^ thats what happens when boomers are invited to parties ^ SQUARED.

// precondition(age < 50, "ONLY BOOMERS PLEASE!")
// ^^ Precondition failed: ONLY BOOMERS PLEASE!: file basics.playground, line 257 ^^
