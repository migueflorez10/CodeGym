const cart = [
    { name: "Monitor 24 pg", Price: 500},
    { name: "Tv 50 pg", Price: 700},
    { name: "Tablet", Price: 300},
    { name: "AirPods", Price: 200},
    { name: "Keyboard", Price: 50},
    { name: "Cellphone", Price: 500},
    { name: "Speakers", Price: 300},
    { name: "Laptop", Price: 800},
]

// forEach
cart.forEach(product =>console.log(product.name));


// map
const array1 = cart.map(product => `${product.name} -- ${product.Price}`);
console.log(array1);