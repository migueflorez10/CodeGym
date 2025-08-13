// objects 

const product_name = "Monitor";
const product_price = 100;
const product_availability = true;


const product = {
    product_name: "Monitor",
    product_price: 100,
    product_availability: true
}

console.log(product);
// console.log(product.product_price);
// console.log(product["product_name"]);


// add new properties
product.img = 'imagen.jpg';

// delete properties
delete product.product_availability;