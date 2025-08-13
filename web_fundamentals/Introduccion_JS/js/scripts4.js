// Types of data

const product = "Monitor 24 pg";
const product2 = String("Monitor 27 pg");
const product3 = new String("Monitor 32 pg");

console.log(typeof product)
console.log(typeof product2)
console.log(typeof product3)

console.log(miVar); 
var miVar = 5;
console.log(miVar); 

function ejemplo() {
    var x = 1;
    if (true) {
        var x = 2; 
        console.log(x); 
    }
    console.log(x); 
}
ejemplo();


const PI = 3.1416;

const usuario = { nombre: "Ana" };
usuario.nombre = "Luis"; 
console.log(usuario.nombre); // "Luis"
