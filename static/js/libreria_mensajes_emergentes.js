function clickCancelar() {
    swal({
        title: "Confirmar acción",
        text: "Hay cambios sin guardar, ¿Realmente deseas salir?",
        icon: "warning",
        buttons: ["Aceptar", "Cancelar"],
        closeOnClickOutside: false,
    });
};

const cancelar = document.getElementById("btn_cancelar");
cancelar.addEventListener("click", clickCancelar);

function clickEnviar() {
    swal({
        title: "Operación exitosa!",
        icon: "success",
        button: "Aceptar",
        closeOnClickOutside: false,
    });
};
const enviar = document.getElementById("btn_enviar");
enviar.addEventListener("click", clickEnviar);

function clickGuardar() {
    swal({
        title: "Operación exitosa!",
        icon: "success",
        button: "Aceptar",
        closeOnClickOutside: false,
    });
};
const guardar = document.getElementById("btn_guardar");
guardar.addEventListener("click", clickGuardar);