// Switch 

const methodPayment = `Cash`;

switch(methodPayment){
    case `Cash`:
        console.log(`You are paying cash`);
    break;
    case `Check`:
        console.log(`The user is going to pay by check, we will check the funds`);
    break;
    case `Card`:
        console.log(`You are paying card`);
    break;
    default:
        console.log(`You have not paid yet`)
}