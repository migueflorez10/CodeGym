// Promises in Js

const authenticatedUser = new Promise ((resolve, reject) => {
    const auth = false; 

    if(auth){
        resolve(`authenticated user`); // the promise was fulfilled
    }else{
        reject(`I cant log in`); // the promise was not fulfilled
    }
})

authenticatedUser
    .then( result => console.log(result))
    .catch( error => console.log(error))

console.log(authenticatedUser);


// There are three values in the promises 
// pending: has not been complied with, but neither has it been rejected.
// fulfilled: already fulfilled
// Rejected; has been rejected or could not be fulfilled

