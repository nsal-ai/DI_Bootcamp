let fruits = ["Banana", "Apples", "Oranges", "Blueberries"]
fruits.splice(0, 1);
fruits.sort();
fruits.splice(3, 0, "Kiwi");

fruits.shift();
fruits.reverse();


let moreFruits = ["Banana", ["Apples",["Oranges"], "Blueberries"]];
moreFruits[1][1][0]; //selects Oranges

