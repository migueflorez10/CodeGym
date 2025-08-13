// Fetch API 

async function getStaff(){
    const file = 'staff.json';
    // fetch(file)
    //     .then( result =>  result.json())
    //     .then(datos =>{
    //         // console.log(datos.staff);

    //         const {staff} = datos;
    //         // console.log(staff);

    //         staff.forEach(staff =>{
    //             console.log (staff);
    //             console.log (staff.id);
    //             console.log (staff.name);
    //             console.log (staff.job);
    //         })
    //     })
    const result = await fetch(file);
    const datos = await result.json();
    console.log(datos);
}

getStaff();