// Declaration of a function
function sum() {
    console.log(10 + 10);
}
sum();

// Expression of function
const sum2 = function() {
    console.log(20 + 20);
};
sum2();

// Immediately Invoked Function Expression (IIFE)
(function() {
    console.log("Hello Michael");
})();

// Additional examples:

// 1. Function with parameters and return value
function multiply(a, b) {
  return a * b;
}
console.log("multiply(3,4):", multiply(3, 4)); // 12

// 2. Arrow function
const divide = (a, b) => {
    if (b === 0) {
    console.warn("Division by zero!");
    return null;
}
    return a / b;
};
console.log("divide(10,2):", divide(10, 2)); // 5

// 3. Function with default parameters
function greet(name = "Guest") {
    console.log(`Hello, ${name}!`);
}
greet();           // Hello, Guest!
greet("Sandra");   // Hello, Sandra!

// 4. Rest parameters
function sumAll(...numbers) {
    return numbers.reduce((acc, n) => acc + n, 0);
}
console.log("sumAll(1,2,3,4):", sumAll(1, 2, 3, 4)); // 10

// 5. Closure example
function counter() {
    let count = 0;
    return function() {
        count++;
        return count;
    };
}
const inc = counter();
console.log("inc():", inc()); // 1
console.log("inc():", inc()); // 2
