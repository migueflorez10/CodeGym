// objects

const product = {
    product_name: "Monitor",
    product_price: 100,
    product_availability: true
}

// previous form
const price = product.product_price;
const product_name = product.product_name;
console.log(product_name);

// distructuring
const {product_price, product_availability} = product;
console.log(product_price);