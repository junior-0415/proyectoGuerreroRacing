const openModal = document.querySelector('#btn_admistrar');
const modal = document.querySelector('.modal_acciones');
const closeModal = document.querySelector('.modal_close_acciones')

openModal.addEventListener('click', (e)=>{
    e.preventDefault();
    modal.classList.add('modal--show-acciones');
});

closeModal.addEventListener('click', (e)=>{
   e.preventDefault();
   modal.classList.remove('modal--show-acciones');
});