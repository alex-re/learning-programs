// 35
for (let i = 0; i < 100; i++) {
    var request = new XMLHttpRequest();
    request.open('GET', 'data.txt', false); // asycrounus -> false (default is true)
    request.send()
    if (request.status === 200) {
        console.log(request);
        document.write(request.responseText);
    } else {
        console.log('error');
    }
}
// =========================
// 36
var request = new XMLHttpRequest();
request.open('GET', 'data.txt'); // === request.open('GET', 'data.txt', true);
request.onreadystatechange = function () {
    if ((request.readyState === 4) && (request.status === 200)) { // readyState is good for progress bar
        // request.readyState === 4 -> client side check. | request.status === 200 server side check.
        console.log(request);
        document.writeln(request.responseText);
    }
}

request.send();