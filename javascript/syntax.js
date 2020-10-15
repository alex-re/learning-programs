// Data Types
// Boolean Array Number null String
var myBool = new Boolean();
var person = ['gholi', 'gholizade', 25]
// =========================

// function if statment Date
function myFunc() {
    var name = document.getElementById('inp').value;
    if (name === "gholi") {
        alert(name + " 3 equals checks both type and value");
    } else if (name == "ali") {
        this.innerHTML = name + "2 equals Just checks value";
    } else {
        console.log("Hi " + name + " " + new Date().getDay());
    }
}
// =========================

// Swich statment 
var age = 17;
switch (age) {
    case 15:
        console.log('You are 17 now!');
        break;
    case 10:
    case 11:
        console.log('You are 10 OR 11');
        break;
    default:
        console.log('You are ' + age) + 'now!';
        break;
}
// =========================

// Loop statment
var names = ['ali', 'reza', 'gholi', 'ghasem']
// var text = new String();
var text = "";

// for (var i = 0; i < names.length; i++) {
for (let i = 0; i < names.length; i++) {
    // var name = names[i];
    let name = names[i];
    document.write(name + "<br/>")    
}

names.forEach(name => {
    document.write(name + "<br/>")
});

for (i in names) {
    console.log(names[i]);
}

// for (var i = 0; i < names.length; i++) {
for (let i = 0; i < names.length; i++) {
    text += names[i] + '<br/>'
}
document.write(text)
// =========================

// Try Catch
var x = document.getElementById('inp').value;

try {
    if (x == '') throw 'emty';
    if (isNaN(x)) throw 'not a number';    
    x = Number(x);
    if (x < 5) throw 'too low';
    if (x > 10) throw 'too hight';

} catch (error) {
    document.write('Your input is ' + error)
}

finally {
    document.getElementById('inp').value = '';
}
// =========================

// this, var, let, const
// THIS: this always refers to the object that cause the event (in functions) and out of blocks it refers to current document.
// VAR: old version to use variables because its accessible from uncommon block too!
// LET: newer version to use variables because its NOT accessible from uncommon block.
// CONST: newer version to use variables that we don't need to change them ever never BUT we can push (append) to theme (like server name and ...)
// NOTES: this is our reason for using let in for loop and ussually everywhere
// =========================

// debug 
// we have also `debugger;` command like `breakpoint()` in python
// =========================

// Function With Forms
function inpTestFunc() {
    var x, text;
    x = document.getElementById('fname').value;
    // var x = document.forms["myForm"]["fname"].value;
    if(isNaN(x) && x < 1 || x > 10) {
        text = "Input Not Valid";
        document.getElementById('demo').innerHTML=text;
        document.getElementById('demo').style.color="red";
    } else {
        text="Input Ok ."
        document.getElementById('demo').innerHTML=text;
        document.getElementById('demo').style.color="green";
    }
}
// =========================

// contractors
function Person(name, family, age) {
    this.name = name;
    this.family = family;
    this.age = age;
    this.fullName = function () {
        return this.name + ' ' + this.family;
    }
    // this.fullName = () => {
        // return this.name + ' ' + this.family;
    //   }
}

var people = []
var ali = new Person('ali', 'alizade', 15)
people.push(ali);
// =========================

// functions tricks
var add1 = function (a, b) {
    return a + b;
};

var add2 = (a, b) => {
    return a + b
}

var c1 = x(4, 5);

var myCustomFunc = new Function('a', 'b', 'return a * b');
var c2 = myCustomFunc(4, 5);
//--------
function sum(x=0, y=0) { // default values
    return x + y;
}

function unlimitedArgs() {
    for (let i = 0; i < arguments.length; i++) {
        console.log(arguments[i]);
    }
}
unlimitedArgs(1 ,'gholi', true, 1.4);

function add() {
    var count = 0;
    function plus() {
        count += 1
    }
    plus();
    plus();
    return count;
}
// =========================
