//Evercise 1

/*colors = ["red", "green", "blue", "purple"]

var length = colors.length;
for (i = 0; i < length; i++){
    console.log('My #',(i + 1), 'choice is', colors[i]);
}
*/

//Bonus Suffix

/*colors = ["red", "green", "blue", "purple"]
choice = ["My 1st choice", "My 2nd choice", "My 3rd choice", "My 4th choice"]

var length = colors.length;
for (i = 0; i < length; i++){
    console.log(choice[i], 'is', colors[i]);
}
*/
// console.log(`My #{i} color is ${color[i]}) short hand syntax to consider



//Exercise 2--------

//let people = ["Greg", "Mary", "Devon", "James"]

//people.splice(0, 1);
//people.splice(2, 1, 'Jason');
//people.splice(3, 1, 'Yigal');

//length = people.length;

//for (i = 0; i < length; i++){
// console.log(people[i]);
//}

//for (i = 0; i < length; i++) {
//    console.log(people[i]);
//    if (people[i] == "Jason"){
//        break;
//    }
//}


//newPeeps = people.slice(1, -1); 
//console.log(newPeeps);

//for (people of people)


   // console.log(people.slice(1, -1));

   //console.log(people.indexOf("Mary"));

   //console.log(people.indexOf("Foo"));
   //returns -1 as it does not exist in array

  //let last = people.pop();

  //last element in the array always has index number of (length - 1)


  //Exercise 3------

  
 //let i = 0
 // while (+prompt(prompt("number")) < 10){
 //     prompt("number");
 //     i++;
 // }
  

 //Exercise 4------


 //let guestList = {
 //   randy: "Germany",
 //   karla: "France",
 //   wendy: "Japan",
  //  norman: "England",
  //  sam: "Argentina"
  //}

  





  //let entry = prompt('enter name');
  //if (entry in guestList){
   // console.log(`Hi! I'm ${entry}, and i'm from ${guestList.entry}`); //undefined last $
  //}
  //else{
  //    console.log("Hi I'm a guest.");
  //}





//Exercise 5 ---------


/*let family = {
    origin: "Iraq",
    residence: "London",
    siblings: "1",

}

let i = 0;
for (keys in family){
   console.log(keys);
    
}

for  (values in family){
    console.log(Object.values(family));
    break;
}

*/


//Exercise 6 --------------

//let details = {
//    my: 'name',
//    is: 'Rudolf',
//    the: 'raindeer',

//};

//console.log(`${Object.entries(details)}`);



//Exercise 7 ---------------

//let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
//firstLetters = names.map(x => x[0]);
//console.log(`${firstLetters}`);