// Async - Await 

function downloadNewsCustomers(){
    return new Promise(resolve =>{
        console.log(`Download customers....wait...`)

        setTimeout(() => {
            resolve(`customers were downloaded`);
        }, 5000)
    });
}

function downloadLastOrder(){
    return new Promise(resolve =>{
        console.log(`Download orders..wait...`)

        setTimeout(() => {
            resolve(`Orders were downloaded`);
        }, 3000)
    });
}

async function app(){
    try {
        // const customers = await downloadNewsCustomers();
        // const orders = await downloadLastOrder();
        // console.log(customers);
        // console.log(orders);

        const result = await Promise.all([downloadNewsCustomers(), downloadLastOrder()]);
        console.log(result[0]);
        console.log(result[1]);
    } catch (error) {
        console.log(error);
    }
}

app();

