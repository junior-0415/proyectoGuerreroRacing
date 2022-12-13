function eliminar_registros(id){
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
            window.location.href = "eliminar/"+id+"/" 
        }
    });

};

function cerrar_orden_servicio(id){
    Swal.fire({
        title: 'Confirmar acción',
        text: "Esta órden será marcada como pagada. ¡Ya no la podrás editar!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#d33',
        cancelButtonColor: '#00B9CA',
        confirmButtonText: 'Cerrar órden',
        cancelButtonText: 'Cancelar',
        allowOutsideClick: false,
        allowEscapeKey: false
    })
    .then(function(result){
        if (result.isConfirmed) {
            window.location.href = "cerrar/"+id+"/" 
        }
    });

};

function cerrar_factura(id){
    Swal.fire({
        title: 'Confirmar acción',
        text: "Esta factura sera actualizada al estado cerrada. ¡Ya no la podrás editar!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#d33',
        cancelButtonColor: '#00B9CA',
        confirmButtonText: 'Cerrar factura',
        cancelButtonText: 'Cancelar',
        allowOutsideClick: false,
        allowEscapeKey: false
    })
    .then(function(result){
        if (result.isConfirmed) {
            window.location.href = "cerrar/"+id+"/" 
        }
    });

};

function cerrar_pedido(id){
    Swal.fire({
        title: 'Confirmar acción',
        text: "Este pedido sera actualizado al estado cerrado. ¡Ya no la podrás editar!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#d33',
        cancelButtonColor: '#00B9CA',
        confirmButtonText: 'Cerrar pedido',
        cancelButtonText: 'Cancelar',
        allowOutsideClick: false,
        allowEscapeKey: false
    })
    .then(function(result){
        if (result.isConfirmed) {
            window.location.href = "cerrar/"+id+"/" 
        }
    });

};

function cerrar_orden_compra(id){
    Swal.fire({
        title: 'Confirmar acción',
        text: "Esta órden sera actualizada al estado cerrada. ¡Ya no la podrás editar!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#d33',
        cancelButtonColor: '#00B9CA',
        confirmButtonText: 'Cerrar órden',
        cancelButtonText: 'Cancelar',
        allowOutsideClick: false,
        allowEscapeKey: false
    })
    .then(function(result){
        if (result.isConfirmed) {
            window.location.href = "cerrar/"+id+"/" 
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

function eliminar_art_detalle_fac(id, tbl_facturas_idfactura){
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
            window.location.href = "/quitar-articulo-factura/"+id+"/"+tbl_facturas_idfactura+"/"
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

function eliminar_compra_pedido_def_alert(id){
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
            window.location.href = "compras-pedidos/eliminar/"+id+"/" 
        }
    });

};

function quitar_art_rel_pedido_art(id){
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
            window.location.href = "/compras/registrar-compra-pedido/articulos/quitar/"+id+"/" 
        }
    });

};

function quitar_art_rel_ord_comp_art(id){
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
            window.location.href = "/compras/crear-orden-de-compra/articulos/eliminar/"+id+"/" 
        }
    });

};