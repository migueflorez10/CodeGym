// Control structures

const score = 1000; 

if (score === 1000){
    console.log(`Your score is ${score}`);
} else{
    console.log(`You lost`);
}

const cash = 1000; 
const cart = 800; 

if(cash > cart){
    console.log(`the user can pay`);
}else{
    console.log(`insufficient funds`)
}


const rol = `admin`;

if (rol === `admin`){
    console.log(`Acces to the entire system`)
}else if(rol === `publisher`){
    console.log(`you have access only to the photos`)
}else{
    console.log(`you do not have access`)
}