//-----------------------------------------------OOP--------------------------------------------------//
// two ways of doing it

// constructor function
function Person(firstName, lastName, dateOfBirth)
{
    this.firstName = firstName;
    this.lastName = lastName;
    this.dateOfBirth = new Date(dateOfBirth);

    // returns year of birth
    this.getBirthYear = function()
    {
        return this.dateOfBirth.getFullYear();
    }

    // returns full name
    this.getFullName = function()
    {
        return this.firstName + " " + this.lastName;
    }
}
// prototyping 
Person.prototype.getFirstName = function()
{
    return this.firstName;
}

// instantiation
let person1 = new Person("Bob", "Dylan", "04-03-2006");
let person2 = new Person("Mary", "Lamb", "01-12-1939");

console.log(person1);
console.log(person2.dateOfBirth);
console.log(person1.getBirthYear());
console.log(person1.getFullName());
console.log(person2.getFirstName());

// after ES6 (ES2015) a prettier way and more familiar
// classes
class Dog
{
    // just like java
    constructor(breed, sex, dob)
    {
        this.breed = breed;
        this.sex = sex;
        this.dob = new Date(dob);
    }

    getBreed()
    {
        return this.breed;
    }

    getSex()
    {
        return this.sex;
    }

    getDob()
    {
        return this.dateOfBirth;
    }

    setBreed(breed)
    {
        this.breed = breed;
    }
}

let dog1 = new Dog("Pub", "Male", "10-10-2010");
console.log(dog1.getBreed());

dog1.setBreed("Beagle");
console.log(dog1.getBreed());
