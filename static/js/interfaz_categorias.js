const openModal = document.querySelector('#btn_anadir');
const modal = document.querySelector('.modal-form-cat');
const closeModal = document.querySelector('.modal_close-form-cat')
var direccion = "http://127.0.0.1:8000/articulos/categorias/";
var LocationActual = window.location;

openModal.addEventListener('click', (e)=>{
    e.preventDefault();
    modal.classList.add('modal--show-form-cat');
});

closeModal.addEventListener('click', (e)=>{
   e.preventDefault();
   modal.classList.remove('modal--show-form-cat');
});

if (direccion != LocationActual){
    modal.classList.add('modal--show-form-cat');
};