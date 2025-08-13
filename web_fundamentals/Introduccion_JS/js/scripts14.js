// objets 
const product = {
    product_name: "Monitor",
    product_price: 100,
    product_availability: true
}

const measures = {
    weigth: "1kg",
    size: "1mm"
}

const newProduct = {...product, ...measures};

console.log(product);
console.log(newProduct	);