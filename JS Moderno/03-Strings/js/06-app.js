const producto = "Moniotr 20 pulgadas";

// .repetear te va a permitir una cadena de texto...
const texto = "En promocion ".repeat(3);

console.log(texto);

console.log(`${producto} ${texto} !!!`);

// Split, dividir un string

const actividad = "Estoy aprendiendo JavaScript Moderno";
console.log(actividad.split(" "));

const hobbies = "Leer, Caminar, escuchar musica, aprender a progamar";
console.log(hobbies.split(","));

const tweet = "Aprendiendo JavaScript #JSModernoConJuan";
console.log(tweet.split("#"))