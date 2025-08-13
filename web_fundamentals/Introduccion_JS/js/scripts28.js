// Object Constructor and Object literal (POO)

// Object literal

const product = {
    name: `Tablet`,
    price: 1000
}


// object constructor

function Customer(name, lastName){
    this.name = name;
    this.lastName = lastName;
}

Customer.prototype.formatProduct = function(){
    return `Your name: ${this.name} Last name: ${this.lastName}`;
}

function Product(name, price, availability){
    this.name = name;
    this.price = price;
    this.availability = availability;
}

// create functions that are only used in a specialized obect

Product.prototype.formatProduct = function(){
    return `The product ${this.name} has a price of: $ ${this.price}`;
}

const product2 = new Product(`Ifhone 15 pro max`, 6900, false);
const product3 = new Product(`Ifhone 16 pro max`, 7200, true);
const product4 = new Product(`Macbook Air M4`, 8000, true);
const customer = new Customer(`Miguel`, `Florez`);

console.log(customer);
console.log(product2);
console.log(product2.formatProduct());
console.log(product3.formatProduct());
console.log(product4.formatProduct());





