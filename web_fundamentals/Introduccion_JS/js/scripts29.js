// Classes

class Product{
    constructor(name, price){
        this.name = name; 
        this.price = price; 
    }
    formatProduct(){
        return `the ${this.name} product is priced at ${this.price} `
    }
    formatPrice(){
        return `The price is ${this.price}` 
    }
}

const product1 = new Product(`MacBook Air M4`, 7200);
const product2 = new Product(`MacBook pro M4 pro`, 9200);

// Legacy
class Book extends Product{
    constructor(name, price, isbn){
        super(name, price);
        this.isbn = isbn; 
    }
    formatProduct(){
        return `${super.formatProduct()} and its isbn is ${this.isbn} `
    }
}

const book = new Book(`JavaScript Revolution`, 36000, `73892282700`);

console.log(book.formatProduct());
console.log(product1.formatPrice());
console.log(product2.formatProduct());
