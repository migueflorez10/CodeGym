// functions

// function sum (n1, n2){
//     return n1 + n2;
// }

// const result = sum(8, 8);

// console.log(result);

let total = 0;

function addCart (price){
    return total += price;
}

total = addCart (400);
total = addCart (400);
total = addCart (200);


function calculateTax(total){
    return 1.15 * total;
}

const totalPayable = calculateTax(total);

console.log(total); 
console.log(`The total amount payable with taxes is: $${totalPayable}`); 