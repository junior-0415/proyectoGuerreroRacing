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
    })

}

function eliminar_registros_def(id){
    Swal.fire({
        title: 'Confirmar acción',
        text: "¡No podrás revertir esto! ¿Deseas eliminar?",
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
    })

}

// ¡No podrás revertir esto!

// btns_eliminacion.forEach(btn => {
//     btn.addEventListener('click', function (e) {
//         e.preventDefault();
//         Swal.fire({
//             title: 'Are you sure?',
//             text: "You won't be able to revert this!",
//             icon: 'warning',
//             showCancelButton: true,
//             confirmButtonColor: '#3085d6',
//             cancelButtonColor: '#d33',
//             confirmButtonText: 'Yes, delete it!'
//         }).then((result) => {
//             if (result.isConfirmed) {
//                 window.location.replace();
//                 Swal.fire(
//                     'Deleted!',
//                     'Your file has been deleted.',
//                     'success'
//                 )
//             }
//         })
//     })
// });
