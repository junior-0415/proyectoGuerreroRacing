const openModal = document.querySelector('#btn_anadir');
const modal = document.querySelector('.modal-form');
const closeModal = document.querySelector('.modal_close-form')

openModal.addEventListener('click', (e)=>{
    e.preventDefault();
    modal.classList.add('modal--show-form');
});

closeModal.addEventListener('click', (e)=>{
   e.preventDefault();
   modal.classList.remove('modal--show-form');
});