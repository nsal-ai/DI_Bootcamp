//====== Exercise 1 ======

/*var age = prompt("what is your age?");

function checkDriverAge(age) {
    if (age < 18){
        alert("Sorry, you are too young to drive this car. Powering off");
    }
    else{
        alert("You are old enough to drive, Powering on. Enjoy the ride");
    }
}

checkDriverAge(age);
*/




//====== Exercise 2 =========

/*
let values = [0.25, 0.10, 0.05, 0.01];

function changeEnough (inPocket, changeDue){
    var sum = 0;
    for (let i = 0; i < inPocket.length; i++ ){
        sum += inPocket[i] * values[i];
    }
    if (sum >= changeDue){
        console.log("true");
    }
    else{
        console.log("false");
    }
}


changeEnough([10, 0, 0, 0], 5);
*/



//========= Exercise 3 ==========

/*
let i = 0
let sum = 0

function mult23 (entry){
    var length = Math.floor(entry/23);
    for (i = 0; i < length + 1; i++){
        console.log(i * 23);
        sum += (i * 23);
       }
       
  console.log(sum);
}

mult23(500);
*/


//========= Exercise 4 =============


/*
let amazonBasket = {
glasses: 1,
books: 2,
floss: 100,
}



function checkBasket (item) {
    let newItem = prompt(`which item`);
    if (newItem in amazonBasket){
        console.log(`already in basket`);
    }
else{
    console.log(`add to basket`);
}
}

checkBasket("books")
*/




//====== Exercise 5 ==========
/*
let stock = {
    "banana": 6,
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry": 1,
}

let prices = {
    "banana": 4,
    "apple": 2,
    "pear": 1,
    "orange": 1.5,
    "blueberry": 10,
}




var shoppingList = ["banana", "orange", "apple"];
let sum = 0;


function myBill() {
    for(i = 0; i < shoppingList.length; i++) {
        if (shoppingList[i] in stock){
           console.log(prices.shoppingList[i]);
        }
    }




    



}
myBill(shoppingList);

//trouble linking array to object in order to extract key values...

*/











//========== Exercise 6 =============

/*
var amount = prompt(`how much is it?`);

function Bill(amount) {

    if (amount < 50) {
        console.log(0.2 * amount);
        console.log(1.2 * amount);

    } else if (50 < amount < 200) {
        console.log(0.15 * amount);
        console.log(1.15 * amount);
    } else if (amount > 200) {
        console.log(0.1 * amount);
        console.log(1.1 * amount);
    }

}

Bill(amount);
*/





//=========== Exercise 7 ===========

/*
function hotel_cost(nights, price) {
 var nights = +prompt("Hi there!, How many nights?");
 if (isNaN(nights)){
    nights = +prompt("Hi there!, How many nights?");
 }
 return "$" + nights*price;
};
console.log(hotel_cost(0,140));
hotel_cost();

*/


//start from the following below:


hotel_cost();

let nights = +prompt("how many nights of stay?");

function hotel_cost(nights, price) {
    return nights * price;
 
}
const x = nights * 140;
console.log(hotel_cost(nights, 140));


let package = {
    "London": 183,
    "Paris": 220,

}



let dest = prompt("where do you want to go?")
plane_ride_cost();

function plane_ride_cost() {

    if (dest != "London" && dest != "Paris") {
        console.log("$300");
        
    } else if (dest === "London") {
        console.log(package.London);
    } else if (dest === "Paris") {
        console.log(package.Paris);
    }
}


let rentTime = +prompt("number of days for car rental?");
rental_car_cost();

function rental_car_cost(rentTime) {
    if (rentTime == NaN) {
        prompt("number of days for car rental?");
    } else {
        return rentTime * 40;
    }


}
const z = rentTime * 40;
console.log(rental_car_cost(rentTime));


total_vacation_cost();

function total_vacation_cost(x,z){
    if(dest == package.London){
        return x + package.London + z;
    
    }
    else if(dest == package.Paris){
        return x + package.Paris + z;
    }
    else if (dest != "Paris" || dest != "London"){
    return x + 300 + z;
    }
}



