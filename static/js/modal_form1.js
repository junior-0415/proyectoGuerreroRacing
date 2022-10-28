const openModal = document.querySelector('#btn_anadir');
const modal = document.querySelector('.modal-form1');
const closeModal = document.querySelector('.modal_close-form1')
var direccion = "http://127.0.0.1:8000/vehiculos/marcas/";
var LocationActual = window.location;

openModal.addEventListener('click', (e)=>{
    e.preventDefault();
    modal.classList.add('modal--show-form1');
});

closeModal.addEventListener('click', (e)=>{
   e.preventDefault();
   modal.classList.remove('modal--show-form1');
});

if (direccion != LocationActual){
    modal.classList.add('modal--show-form1');
};