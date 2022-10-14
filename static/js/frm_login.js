const openModal1 = document.querySelector('.btn_olvidar_contrasena');
const modal1 = document.querySelector('.modal1');
const closeModal1 = document.querySelector('.modal_close1');

openModal1.addEventListener('click', (e)=>{
    e.preventDefault();
    modal1.classList.add('modal--show1');
});

closeModal1.addEventListener('click', (e)=>{
    e.preventDefault();
    modal1.classList.remove('modal--show1');
});


const openModal2 = document.querySelector('#btn_siguiente1');
const modal2 = document.querySelector('.modal2');
const closeModal2 = document.querySelector('.modal_close2');

openModal2.addEventListener('click', (e)=>{
    e.preventDefault();
    modal2.classList.add('modal--show2');
    modal1.classList.remove('modal--show1');
});

closeModal2.addEventListener('click', (e)=>{
    e.preventDefault();
    modal2.classList.remove('modal--show2');
    modal1.classList.add('modal--show1');
});


const openModal3 = document.querySelector('#btn_siguiente2');
const modal3 = document.querySelector('.modal3');
const closeModal3 = document.querySelector('.modal_close3');

openModal3.addEventListener('click', (e)=>{
    e.preventDefault();
    modal3.classList.add('modal--show3');
    modal2.classList.remove('modal--show2');
});

closeModal3.addEventListener('click', (e)=>{
    e.preventDefault();
    modal3.classList.remove('modal--show3');
    modal2.classList.add('modal--show2');
});

const openModal4 = document.querySelector('#btn_siguiente3');
const modal4 = document.querySelector('.modal4');
const closeModal4 = document.querySelector('.modal_close4');

openModal4.addEventListener('click', (e)=>{
    e.preventDefault();
    modal4.classList.add('modal--show4');
    modal3.classList.remove('modal--show3');
});

closeModal4.addEventListener('click', (e)=>{
    e.preventDefault();
    modal4.classList.remove('modal--show4');
});