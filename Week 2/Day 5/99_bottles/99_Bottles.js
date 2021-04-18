let x = +prompt("Enter number of bottles");


for (var i = 0; i < x; i++) {
    x -= i;
    console.log(x + " bottles of beer on the wall");
    console.log(x + " bottles of beer");
    console.log("take " + (i + 1) + " down, pass it around");
    if (x - i - 1 < 0) {
        console.log((0) + " bottles of beer on the wall")
    } else {
        console.log((x - i - 1) + " bottles of beer on the wall");


    }
}
// X bottles of beer on the wall
// X bottles of beer
// take (i = 1) down, pass it around
// (X-i) bottles of beer on the wall


// X, (X-i), (X-2i-1), (X-3i-3) etc....sequence of bottles total
// x - i - 3n (can iterate from n=0)