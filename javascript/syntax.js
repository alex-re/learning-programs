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

for (var i = 0; i < names.length; i++) {
    var name = names[i];
    document.write(name + "<br/>")    
}

names.forEach(name => {
    document.write(name + "<br/>")
});

for (i in names) {
    console.log(names[i]);
}

for (var i = 0; i < names.length; i++) {
    text += names[i] + '<br/>'
}
document.write(text)
// =========================
