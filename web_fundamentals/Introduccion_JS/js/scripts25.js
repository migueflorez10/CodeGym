// for loop

// for(let i = 0; i <= 10; i++){
//     console.log(i);
// }

// for(let i = 1; i <= 10; i++){
//     if(i % 2 == 0){
//         console.log(`The number ${i} is even`);
//     } else{
//         console.log(`The number ${i} is odd`);
//     }
// }

const cart = [
    { name: "Monitor 24 pg", Price: 500},
    { name: "Tv 50 pg", Price: 700},
    { name: "Tablet", Price: 300},
    { name: "AirPods", Price: 200},
    { name: "Keyboard", Price: 50},
    { name: "Cellphone", Price: 500},
    { name: "Speakers", Price: 300},
    { name: "Laptop", Price: 800},
]

for(let i = 0; i < cart.length; i++){
    console.log(cart[i].name);
}


// while loop

// let i = 1; // index

// while(i<=10){ // condition
//     if(i % 2 == 0){
//         console.log(`The number ${i} is even`);
//     }else{
//         console.log(`The number ${i} is odd`);
//     }

//     i++; // increase 
// }


// Do while loop

let i = 0;

do {
    console.log(i);
    i++;
} while(i <= 10);