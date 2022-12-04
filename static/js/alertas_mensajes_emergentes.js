function eliminar_registros(id){
    Swal.fire({
        title: 'Confirmar acción',
        text: "El registro será envido a la papelera",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#d33',
        cancelButtonColor: '#00B9CA',
        confirmButtonText: 'Mover a papelera',
        cancelButtonText: 'Cancelar',
        allowOutsideClick: false,
        allowEscapeKey: false
    })
    .then(function(result){
        if (result.isConfirmed) {
            window.location.href = "eliminar/"+id+"/" 
        }
    });

};

function eliminar_servicio_def_alert(id){
    Swal.fire({
        title: 'Confirmar acción',
        text: "¡No podrás revertir esto! ¿Deseas eliminar definitivamente?",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#d33',
        cancelButtonColor: '#00B9CA',
        confirmButtonText: 'Eliminar',
        cancelButtonText: 'Cancelar',
        allowOutsideClick: false,
        allowEscapeKey: false
    })
    .then(function(result){
        if (result.isConfirmed) {
            window.location.href = "servicios/eliminar/"+id+"/" 
        }
    });

};

function eliminar_cliente_def_alert(id){
    Swal.fire({
        title: 'Confirmar acción',
        text: "¡No podrás revertir esto! ¿Deseas eliminar definitivamente?",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#d33',
        cancelButtonColor: '#00B9CA',
        confirmButtonText: 'Eliminar',
        cancelButtonText: 'Cancelar',
        allowOutsideClick: false,
        allowEscapeKey: false
    })
    .then(function(result){
        if (result.isConfirmed) {
            window.location.href = "clientes/eliminar/"+id+"/" 
        }
    });

};

function eliminar_ciudad_def_alert(id){
    Swal.fire({
        title: 'Confirmar acción',
        text: "¡No podrás revertir esto! ¿Deseas eliminar definitivamente?",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#d33',
        cancelButtonColor: '#00B9CA',
        confirmButtonText: 'Eliminar',
        cancelButtonText: 'Cancelar',
        allowOutsideClick: false,
        allowEscapeKey: false
    })
    .then(function(result){
        if (result.isConfirmed) {
            window.location.href = "ciudades/eliminar/"+id+"/" 
        }
    });

};

function eliminar_depart_def_alert(id){
    Swal.fire({
        title: 'Confirmar acción',
        text: "¡No podrás revertir esto! ¿Deseas eliminar definitivamente?",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#d33',
        cancelButtonColor: '#00B9CA',
        confirmButtonText: 'Eliminar',
        cancelButtonText: 'Cancelar',
        allowOutsideClick: false,
        allowEscapeKey: false
    })
    .then(function(result){
        if (result.isConfirmed) {
            window.location.href = "departamentos/eliminar/"+id+"/" 
        }
    });

};

function eliminar_marca_def_alert(id){
    Swal.fire({
        title: 'Confirmar acción',
        text: "¡No podrás revertir esto! ¿Deseas eliminar definitivamente?",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#d33',
        cancelButtonColor: '#00B9CA',
        confirmButtonText: 'Eliminar',
        cancelButtonText: 'Cancelar',
        allowOutsideClick: false,
        allowEscapeKey: false
    })
    .then(function(result){
        if (result.isConfirmed) {
            window.location.href = "marcas/eliminar/"+id+"/" 
        }
    });

};

function eliminar_articulo_def_alert(id){
    Swal.fire({
        title: 'Confirmar acción',
        text: "¡No podrás revertir esto! ¿Deseas eliminar definitivamente?",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#d33',
        cancelButtonColor: '#00B9CA',
        confirmButtonText: 'Eliminar',
        cancelButtonText: 'Cancelar',
        allowOutsideClick: false,
        allowEscapeKey: false
    })
    .then(function(result){
        if (result.isConfirmed) {
            window.location.href = "articulos/eliminar/"+id+"/" 
        }
    });

};

function eliminar_categoria_def_alert(id){
    Swal.fire({
        title: 'Confirmar acción',
        text: "¡No podrás revertir esto! ¿Deseas eliminar definitivamente?",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#d33',
        cancelButtonColor: '#00B9CA',
        confirmButtonText: 'Eliminar',
        cancelButtonText: 'Cancelar',
        allowOutsideClick: false,
        allowEscapeKey: false
    })
    .then(function(result){
        if (result.isConfirmed) {
            window.location.href = "categorias/eliminar/"+id+"/" 
        }
    });

};

function eliminar_proveedor_def_alert(id){
    Swal.fire({
        title: 'Confirmar acción',
        text: "¡No podrás revertir esto! ¿Deseas eliminar definitivamente?",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#d33',
        cancelButtonColor: '#00B9CA',
        confirmButtonText: 'Eliminar',
        cancelButtonText: 'Cancelar',
        allowOutsideClick: false,
        allowEscapeKey: false
    })
    .then(function(result){
        if (result.isConfirmed) {
            window.location.href = "proveedores/eliminar/"+id+"/" 
        }
    });

};

function eliminar_vehiculo_def_alert(id){
    Swal.fire({
        title: 'Confirmar acción',
        text: "¡No podrás revertir esto! ¿Deseas eliminar definitivamente?",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#d33',
        cancelButtonColor: '#00B9CA',
        confirmButtonText: 'Eliminar',
        cancelButtonText: 'Cancelar',
        allowOutsideClick: false,
        allowEscapeKey: false
    })
    .then(function(result){
        if (result.isConfirmed) {
            window.location.href = "vehiculos/eliminar/"+id+"/" 
        }
    });

};

function eliminar_empleado_def_alert(id){
    Swal.fire({
        title: 'Confirmar acción',
        text: "¡No podrás revertir esto! ¿Deseas eliminar definitivamente?",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#d33',
        cancelButtonColor: '#00B9CA',
        confirmButtonText: 'Eliminar',
        cancelButtonText: 'Cancelar',
        allowOutsideClick: false,
        allowEscapeKey: false
    })
    .then(function(result){
        if (result.isConfirmed) {
            window.location.href = "empleados/eliminar/"+id+"/" 
        }
    });

};

function eliminar_sucursal_def_alert(id){
    Swal.fire({
        title: 'Confirmar acción',
        text: "¡No podrás revertir esto! ¿Deseas eliminar definitivamente?",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#d33',
        cancelButtonColor: '#00B9CA',
        confirmButtonText: 'Eliminar',
        cancelButtonText: 'Cancelar',
        allowOutsideClick: false,
        allowEscapeKey: false
    })
    .then(function(result){
        if (result.isConfirmed) {
            window.location.href = "sucursales/eliminar/"+id+"/" 
        }
    });

};

function eliminar_art_detalle_fac(id){
    Swal.fire({
        title: 'Confirmar acción',
        text: "¿Deseas quitar este artículo de la factura?",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#d33',
        cancelButtonColor: '#00B9CA',
        confirmButtonText: 'Quitar',
        cancelButtonText: 'Cancelar',
        allowOutsideClick: false,
        allowEscapeKey: false
    })
    .then(function(result){
        if (result.isConfirmed) {
            window.location.href = "/quitar-articulo/"+id+"/" 
        }
    });

};

function quitar_art_rel_ord_art(id){
    Swal.fire({
        title: 'Confirmar acción',
        text: "¿Deseas quitar este artículo de la factura?",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#d33',
        cancelButtonColor: '#00B9CA',
        confirmButtonText: 'Quitar',
        cancelButtonText: 'Cancelar',
        allowOutsideClick: false,
        allowEscapeKey: false
    })
    .then(function(result){
        if (result.isConfirmed) {
            window.location.href = "/quitar-articulo-orden-compra/"+id+"/" 
        }
    });

};


function eliminar_orden_ser_def_alert(id){
    Swal.fire({
        title: 'Confirmar acción',
        text: "¡No podrás revertir esto! ¿Deseas eliminar definitivamente?",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#d33',
        cancelButtonColor: '#00B9CA',
        confirmButtonText: 'Eliminar',
        cancelButtonText: 'Cancelar',
        allowOutsideClick: false,
        allowEscapeKey: false
    })
    .then(function(result){
        if (result.isConfirmed) {
            window.location.href = "ordenes-servicio/eliminar/"+id+"/" 
        }
    });

};