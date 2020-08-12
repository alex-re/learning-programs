function change_text(){
    document.getElementById("DIV").innerHTML="Hello from javascript!";
}    

// ________________________________________________________________________

$var1 = "Hi";
$footer = document.getElementsByClassName("div-class")[0].innerHTML = "Hello from javascript!";

for (i=0; i<10; i++)
    $footer.innerHTML += $var1+"\n";
console.log("done!")

for (i=0; i<10; i = i+1){
    console.log(a);
}

for (i=0; i<10; i += 1){
    console.log(a);
}
// ________________________________________________________________________

var about_stat = "it_is_visible";

function hide_about(){
    if (about_stat == "it_is_visible"){
        document.getElementById("about").style.visibility = "hidden";
        about_stat = "it_is_hidden";
    }
    else{
        document.getElementById("about").style.visibility = "visible";
        about_stat = "it_is_hidden";
    }
}

// ________________________________________________________________________

for (i=0; i < document.getElementsByClassName("div-class").length; i++){
    document.getElementsByClassName("div-class")[i].style.backgroundColor = "red"
    document.getElementsByTagName("p")[i].style.visibility = "hidden"
}

// ________________________________________________________________________

for (i=0; i < document.getElementsByTagName("li").length; i++){
    document.getElementsByTagName("li")[i].innerHTML = "<p>sss<br>sss</p>";
}

// ________________________________________________________________________

if (a == 1){
    console.log("a is equal to 1");
}
else{
    console.log("a is not equal to 1");
}

// ________________________________________________________________________

var a = 3;
console.log(a);
console.log("salam");

var a = "Hello"
console.log(a);

// ________________________________________________________________________

var a = 1, b = 2, c = 10;
var d = a + b;
var c = 10 * d;
var a = 5;
var list = [2, 3, 4, 5, 6];
console.log(list[0])

for (i=0; i<list.length; i++){
    console.log(i+ " : " +a[i]);
}


console.log(a);
console.log(b);
console.log(c);
console.log(d);

// ________________________________________________________________________
var cookie

cookie = document.cookie.split(";")[0]

cookie = "another value"

// ________________________________________________________________________

