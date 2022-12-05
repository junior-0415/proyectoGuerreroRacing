from usuarios.models import Empleados

def sesion(request):
    usuario_actual = request.user
    image_user = r"../media/images/usuarios/default.png"
    if request.user.is_authenticated:
        if Empleados.objects.filter(user_id=usuario_actual.id):
            image_user = Empleados.objects.get(user_id=usuario_actual.id).emp_foto.url
    context = {
        'usuario_actual':usuario_actual,
        'image_user':image_user
    }
    return context