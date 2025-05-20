// arrays methods

const months = ["january", "february", "march", "april", "may", "june"];

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

months.forEach(function(month){
    if(month == "march"){
        console.log("March if this")
    }
});

// includes
let result = months.includes("march");


// some - is better to arrays of objects

result = cart.some(function(product){
    return product.name == "Cellphone"
})

// .reduce 

result = cart.reduce(function(total, product){
    return total + product.Price
}, 0);

// filter

result = cart.filter(function(product){
    return product.Price > 400
});

result = cart.filter(function(product){
    return product.name !== "Cellphone"
});

console.log(result);