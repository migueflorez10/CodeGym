// arrays

const numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100];
console.table(numbers);

const months = ["january", "february", "march", "april", "may", "june"];
console.table(months);

// const array = ["hello", 10, true, "yes", null, {name: "Miguel", work: "Frontend"}, [1,2,3]];
// console.log(array);

// access the values of an array
// console.log(numbers[4]);

// // connect the extensions of an array
// console.log(months.length);

// numbers.forEach( function(number){
//     console.log(number)
// });

// numbers[10] = 110;
// console.table(numbers);

numbers.push(110, 120, 130); // arranged at the end of the arrangement
numbers.unshift(-10, -20, -30, -40); // arranged at the beginning of the arrangement
console.log(numbers);

months.pop(); // removes the last value from the array
console.log(months);

months.shift(); // removes the first value from the array
console.log(months);

months.splice(2, 1); // removes a specific value from the array, can be one or more as specified
console.log(months);


// Rest operator o Spread Operator

const newArray = [...months, "july, august"];
console.log(newArray);