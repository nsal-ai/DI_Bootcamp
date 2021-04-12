var sentence = "The movie is not bad I like it";
var wordNot = "not";
var wordBad = "bad";

string_to_array = function (sentence) {
    return sentence.trim().split(" "); 
}

console.log(string_to_array("The movie is not bad I like it")); //splits sentence into array


//var a = console.log(string_to_array("The movie is not bad I like it")); //doesn't work

//console.log(string_to_array(sentence).indexOf(wordNot));



//if ((string_to_array(sentence).indexOf(wordNot)) < (string_to_array(sentence).indexOf(wordBad))
    //console.log(string_to_array(sentence).splice(string_to_array(sentence).indexOf(wordNot), console.log(string_to_array(sentence).indexOf(wordBad) - string_to_array(sentence).indexOf(wordNot) + 1), 'good'));
   
    console.log(string_to_array(sentence).splice(string_to_array(sentence).indexOf(wordNot), 2, 'good'));
    console.log(string_to_array(sentence));
   




/*var length = string_to_array(sentence).length;
var result = false;
for (var i = 0; i < length; i++){
  string_to_array(sentence)[i] = wordNot;
  break;
     
    }

*/
  
//console.log(string_to_array(sentence)[i]);

let array1 = string_to_array(sentence);

//array1.includes(wordNot)

/*var length = array1.length;
for (var i = 0; i < length; i++){
    if (array1[i]=="not"){
        console.log("great");
    }
}
*/ // loop iteration to confirm word in the array

/*
//returns index 3
var length = array1.length;
for (var a = 0; a < length; a++){
    if (array1[a]=="not"){
        alert(a);
    }
 
       
}




//returns index 4
var length = array1.length;
for (var i = 0; i < length; i++){
    if (array1[i]=="bad"){
        alert(i);
    }
    
    
}

if (parseInt(alert(a)) < parseInt(alert(i)){
    array1.splice(alert(a), (alert()))
}
*/



   




var length = array1.length;
for (var a = 0; a < length; a++){
    if (array1[a]=="not"){
        alert(a);
    }
 
       
}




//returns index 4
var length = array1.length;
for (var i = 0; i < length; i++){
    if (array1[i]=="bad"){
        alert(i);
    }
    
    
}


if (array1.findIndex("not") < array1.findIndex("bad")){
    array1.splice(array1.findIndex("not"), array1.findIndex("bad") - array1.findIndex("not") + 1 ,'good');
    console.log(array1.toString());
}
else{
console.log(sentence);
}


