//prompt("word 1")
//prompt("word 2")
//prompt("word 3")
//prompt("word 4")
//prompt("word 5")

let arr1 = [prompt("word 1"), prompt("word 2"), prompt("word 3"), prompt("word 4"), prompt("word 5") ]
console.log(arr1);

let arr1_strLength = arr1.map(arr1 => {
    return arr1.length
}) //turns arr1 in array of numbers according to string length

largest = Math.max(...arr1_strLength); //length of largest string

var stars = "*";
console.log(stars.repeat(largest + 4));



let i = 0;
let length = arr1.length
let space = " ";

for (i = 0; i < length; i++){

    console.log("* " + arr1[i] + space.repeat(largest - arr1_strLength[i] + 1) + stars);
    
}
console.log(stars.repeat(largest +4));
