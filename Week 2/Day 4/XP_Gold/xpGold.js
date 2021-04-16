// Exercise 1 ===========



/*
let arrWord = [prompt("enter word")];
console.log(arrWord);

let wordScore = arrWord.map(arrWord =>{
    return arrWord.length
})

is_Blank();

function is_Blank(){
    if (wordScore[0] === 0){
        return true
    }
    else {
        return false
    }
}
console.log(is_Blank());
*/


// Exercise 2 =============


/*
var identity = prompt("enter full name");

var arrID = identity.split(" ");

abbrev_name()

function abbrev_name(identity){
    return arrID[0] + " " + arrID[1][0] + "."
}

console.log(abbrev_name(identity));

*/


// Exercise 3 =============


/*
var input = prompt("type a sentence");

var arrSent = input.split(" "); //splits to array with each word as element

var arrSize = arrSent.map(arrSent =>{
    return arrSent.length
})  //array of word lengths




output();
var s = " ";
function output(){
    let length = arrSent.length;
    for (i = 0; i < length; i++){
    s += ((arrSent[i][0].toLowerCase() + arrSent[i].slice(1, arrSize[i]).toUpperCase())) + " ";
    }
    
console.log(s);
    
}

//undefined element at the beginning??
*/



/*
var s = "";
for( i = 1; i < 11; i ++) {
  s += i + " ";
}
console.log(s); //structure for string input
*/

    

//Exercise 4 =============

/*

let arr = [[2, 4], [8, 1, 2], [5, 2, 4], [2, 3]];

let length = arr.length;

function isOmnipresent(arr, val) {
    for (let i = 0; i < arr.length; i++) {
        if (!arr[i].includes(val)) {
            return false
        }
        return true;
        
    
    }
    
}
console.log(isOmnipresent(arr, 2));
*/


