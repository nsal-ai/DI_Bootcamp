playTheGame();
var x = confirm("Would you like to play the Game?");


function playTheGame() {
    

    if (x == true) {
        var y = +prompt("Enter a number between 0 and 10");                
        if (isNaN(y) || y > 10) {
            
            alert("Sorry not a number, Goodbye!");
        } else if (0 < y < 11 && Number.isInteger(y) == true) {
            var computerNumber = Math.floor(Math.random() * 11);            
            console.log(computerNumber);
        }

    } else {
        alert("No problem Goodbye!");
    }

}

//need to link local variable to second function
//need to set global variable? how...

test_func();

function test_func(y, computerNumber) {
    
    if (y === computerNumber) {
    
        alert("Winner");
        
    } else if (y > computerNumber) {
        
       var guess1 = +prompt("Your number is bigger than the computer's, guess again");
        
    } else if (y < computerNumber) {
        
       var guess1 =  +prompt("Your number is smaller than the computer's, guess again");
        
    }
}