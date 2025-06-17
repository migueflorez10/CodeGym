document.addEventListener('DOMContentLoaded', ()=>{
    navegacionFija();
    crearGaleria();
    resaltarEnlace();
    scrollNav();
})

function navegacionFija(){
    const header = document.querySelector('.header');
    const sobreFestival = document.querySelector('.sobre-festival');

    window.addEventListener('scroll', ()=>{
        if(sobreFestival.getBoundingClientRect().bottom < 1){
            header.classList.add('fixed');
        } else {
            header.classList.remove('fixed');
        }
    })
}

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
    const imagen = document.createElement('IMG');
    imagen.src = `src/img/gallery/full/${i}.jpg`;
    imagen.alt = 'Imagen Galeria';
    
    // generar Modal
    const modal = document.createElement('DIV');
    modal.classList.add('modal');
    modal.onclick = cerrarModal;

    // boton de cerrar modal
    const cerrarModalBtn = document.createElement('BUTTON');
    cerrarModalBtn.textContent = 'X';
    cerrarModalBtn.classList.add('btn-cerrar');
    cerrarModalBtn.onclick = cerrarModal;

    modal.appendChild(imagen);
    modal.appendChild(cerrarModalBtn);

    // agregar al html
    const body = document.querySelector('body');
    body.classList.add('overflow-hidden');
    body.appendChild(modal);
}

function cerrarModal(){
    const modal = document.querySelector('.modal');
    modal.classList.add('fadeOut');
    setTimeout(() => {
        modal?.remove();
        const body = document.querySelector('body');
        body.classList.remove('overflow-hidden')
    }, 500);
}

function resaltarEnlace() {
    window.addEventListener('scroll', () => {
    const sections = document.querySelectorAll('section');
    const navLinks = document.querySelectorAll('.navegacion-principal a');
    let actual = '';

    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.clientHeight;

    if (window.scrollY >= (sectionTop - sectionHeight / 3)) {
        actual = section.id;
        }
    });

    navLinks.forEach(link => {
            link.classList.remove('active'); 
    if (link.getAttribute('href') === '#' + actual) {
            link.classList.add('active');  
            }
        });
    });
}

function scrollNav(){
    const navLinks = document.querySelectorAll('.navegacion-principal a');
    navLinks.forEach(link =>{
        link.addEventListener('click', (e) => {
            e.preventDefault()
            const sectionScroll = e.target.getAttribute('href');
            const section = document.querySelector(sectionScroll);
            section.scrollIntoView({behavior: 'smooth'})
        })
    })
}