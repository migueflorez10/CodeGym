// "use strict" // run javascript in strict way
// Objets

const product = {
    product_name: "Monitor",
    product_price: 100,
    product_availability: true
}

Object.freeze(product); // freeze .seal

product.product_img = "image";

console.log(Object.isFrozen(product));

console.log(product);