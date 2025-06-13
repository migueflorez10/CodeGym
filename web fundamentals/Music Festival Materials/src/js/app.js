document.addEventListener('DOMContentLoaded', ()=>{
    crearGaleria();
})

function crearGaleria(){
    const cantidad_imagenes = 16;
    const galeria = document.querySelector('.galeria-imagenes');
    for(let i=1; i <= cantidad_imagenes; i++ ){
        const imagen = document.createElement('IMG');
        imagen.src = `src/img/gallery/full/${i}.jpg`;
        imagen.alt = 'Imagen Galeria';

        // event handLer
        imagen.onclick = ()=>{
            mostrarImagen(i);
        } 


        galeria.appendChild(imagen);
    }
}

function mostrarImagen(i){
    // generar Modal

    const modal = document.createElement('DIV');
    modal.classList.add('modal');

    console.log(modal);
}