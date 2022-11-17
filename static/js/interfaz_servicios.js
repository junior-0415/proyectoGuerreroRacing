const openModal = document.querySelector('#btn_anadir');
const modal = document.querySelector('.modal-form');
const closeModal = document.querySelector('.modal_close-form');
var direccion = "http://127.0.0.1:8000/servicios/";
var LocationActual = window.location;

openModal.addEventListener('click', (e)=>{
    e.preventDefault();
    modal.classList.add('modal--show-form');
});

closeModal.addEventListener('click', (e)=>{
    e.preventDefault();
    modal.classList.remove('modal--show-form');
});

if (direccion != LocationActual){
        modal.classList.add('modal--show-form');
};
