document.addEventListener("DOMContentLoaded", () => {
    let listElements = document.querySelectorAll('.list__button--click');

    listElements.forEach(listElement => {
        listElement.addEventListener('click', () => {
    
            listElement.classList.toggle('arrow');
    
            let height = 0;
            let menu = listElement.nextElementSibling;
            if (menu.clientHeight == "0") {
                height = menu.scrollHeight;
            }
    
            menu.style.height = `${height}px`;
    
        })
    
    });  });

const openModalMenu = document.querySelector('#open_modal_menu_img');
const modalMenu = document.querySelector('.modalMenu');
const closeModalMenu = document.querySelector('.img_modal_close');
const ocultarBtnModal = document.querySelector('.open_modal_btn');

openModalMenu.addEventListener('click', (e)=>{
    e.preventDefault();
    modalMenu.classList.add('modal--show-menu');
    ocultarBtnModal.classList.add('ocultar_btn_menu');
});

closeModalMenu.addEventListener('click', (e)=>{
    e.preventDefault();
    modalMenu.classList.remove('modal--show-menu');
});