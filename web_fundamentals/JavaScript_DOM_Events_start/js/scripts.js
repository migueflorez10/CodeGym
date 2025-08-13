// querySelector

const heading = document.querySelector('.header__texto h2'); // 0 or 1 elements
heading.textContent = 'Form'

// querySelectorAll 

const link = document.querySelectorAll('.navegacion a');
console.log(link);
link[0].textContent = 'Receta';
link[0].classList.add('new-nav');
// link[0].classList.remove('navegacion__enlace');

// GetElementById

const heading2 = document.getElementById('heading');
console.log(heading2);

// generate new link
const nuevoEnlace = document.createElement('A');

// add href 
nuevoEnlace.href = 'nuevo-enlace.html';

// add text 
nuevoEnlace.textContent = "Modo dark";

// add class 
nuevoEnlace.classList.add('navegacion__enlace');

// add to document
const navegacion = document.querySelector('.navegacion');
navegacion.appendChild(nuevoEnlace);

console.log(nuevoEnlace);


// events

// console.log(1);

// window.addEventListener('load', ()=>{   // load waits until the js and html dependent files are ready.
//     console.log(2);
// })

// window.onload = () => {
//     console.log(10);
// }

// document.addEventListener('DOMContentLoaded', () => { // only waits for HTML, but doesn't wait for CSS or Images
//     console.log(3);
// })

// console.log(5);

// window.onscroll = (event) => {
//     console.log(event)
// }

// select elemnets and asing an event to them

// const btnEnviar = document.querySelector('.boton--primario');
// btnEnviar.addEventListener('click', (event) => {
//     console.log(event);
//     event.preventDefault();
//     // validate form
//     console.log('send....')
// })


// inputs events and textarea

const datos = {
    nombre: '',
    email: '',
    mensaje: ''
}

const nombreInput = document.querySelector('#nombre');
const emailInput = document.querySelector('#email');
const mensajeInput = document.querySelector('#mensaje');
const formulario = document.querySelector('.formulario');

nombreInput.addEventListener('input', leerTexto);

emailInput.addEventListener('input', leerTexto);

mensajeInput.addEventListener('input', leerTexto);

formulario.addEventListener('submit', (evento)=>{
    evento.preventDefault();
    // valid form

    const {nombre, email, mensaje} = datos;

    if(nombre === '' || email === '' || mensaje === ''){
        mostrarError('Todos los campos son obligatorios')
        return; // cust de code execution
    }

    mensajeExito('Formulario enviado con exito')

    // send form

    console.log('Send Form')
})

function leerTexto(e){
    // console.log(e.target.value);
    datos[e.target.id] = e.target.value; 
    // console.log(datos);
}

// display error on screen
function mostrarError(mensaje){
    const error = document.createElement('p');
    error.textContent = mensaje; 
    error.classList.add('error');
    formulario.appendChild(error);


    // message appears after three seconds
    setTimeout(() => {
        error.remove()
    }, 5000);
};

// message - correct form
function mensajeExito(mensaje){
    const correcto = document.createElement('p');
    correcto.textContent = mensaje; 
    correcto.classList.add('correcto');
    formulario.appendChild(correcto);


    // message appears after three seconds
    setTimeout(() => {
        correcto.remove()
    }, 5000);
};

