from usuarios.models import Empleados

def sesion(request):
    usuario_actual = request.user
    image_user = None
    # if request.user.is_authenticated:
    #     image_user = Empleados.objects.get(user_id=usuario_actual.id).emp_foto.url
    context = {
        'usuario_actual':usuario_actual,
        'image_user':image_user
    }
    return context