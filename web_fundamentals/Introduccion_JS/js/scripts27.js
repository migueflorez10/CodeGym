// reserved word "This"

const reservation = {
    name: `Miguel`,
    lastName: `Martinez`,
    total: 6500,
    paid: true,
    information: function(){
        console.log(`The customer ${this.name} reserved and the amount payable is ${this.total}`);
    }
}

const reservation2 = {
    name: `Juan`,
    lastName: `Martinez`,
    total: 6500,
    paid: true,
    information: function(){
        console.log(`The customer ${this.name} reserved and the amount payable is ${this.total}`);
    }
}

reservation.information();