//prompt("enter value")
//prompt("enter x");
//prompt("enter y");

//Exercise 1

//let x = +prompt("enter x")
//let y = +prompt("enter y")

//if (x > y) {
//   alert("x is the biggest number");
// } else {
//    console.log("");
// }


//----------

//Exercise 2: Chihuahua

//newDog = "Chihuahua"
//newDog.length;

//console.log(newDog.length);
//console.log(newDog.toLowerCase());
//console.log(newDog.toUpperCase());



//let newDog = parseInt("which dog");

//prompt("which dog?");
//prompt("choose dog");

/*let newDog = prompt("choose dog");

if (newDog.toLowerCase().toUpperCase() == "chihuahua") {
    alert("I love Chihuahuas, it's my favorite dog");
}
else {
    console.log("I don't care I prefer cats");
}
*/ //playing around with this

/*
let newDog = prompt("choose dog");

if (newDog.toLowerCase() == "chihuahua") {
  alert("I love chihuahuas too");
}
else{
    console.log("I don't care I like cats");
}
*/
//above works. How do I allow prompt input to apply to upper case??

//-------

//Exercise 3

/*var x = parseInt(prompt("type a number"));
x %= 2;
if(x == 0){
    alert("x is an even number");
}
else{
    alert("x is an odd number");
}
*/

//-------

//Exercise 4

/*let whatHappens;
let direction;

switch (direction) {
    case "forward":
        break;
        whatHappens = "you encounter a monster";
    case "back":
        whatHappens = "you arrived home";
        break;
        break;
    case "right":
        whatHappens = "you found a river";
        break;
    case "left":
        break;
        whatHappens = "you run into a troll";
        break;
    default:
        whatHappens = "please enter a valid direction";
}
*/
// 1. you encounter a monster
// 2. you arrived home
// 3. you found a river
// 4. you run into a troll

//------
//Exercise 5

let users = ["Lea123","ahla123","Noam123","bingo"]
x = users.length - 2;
if (users.length == 0) {
    console.log("the users array is empty");
}
 else if (users.length == 1) {
    console.log(users[0] + " " + "is online");
} 
else if (users.length == 2) {
        console.log(users[0] + "," + " " + users[1] + " " + "are online");
    }
else if (users.length > 2){
        console.log(users[0] + "," + users[1] + " " + "and" + " " + x +  " more are online");
    }
    