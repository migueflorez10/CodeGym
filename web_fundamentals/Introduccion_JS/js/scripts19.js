// functions

// Declaration of a function

function sum (number1=0, number2=0){ // number1 and number2 are parameters
    console.log(number1 + number2);
}

sum(2, 2); // Arguments
sum();

// expression of function

const sum2 = function(n1, n2){
    console.log(n1 + n2);
}

sum2(4, 4);