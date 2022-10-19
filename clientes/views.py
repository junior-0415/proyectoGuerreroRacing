from contextlib import redirect_stderr
from multiprocessing import context
from django.shortcuts import render

from clientes.forms import ClienteForm
from clientes.models import Cliente

# Create your views here.
def clientes(request):
    titulo="Clientes"
    clientes= Cliente.objects.all() #guardar formulario
    context={
        'titulo':titulo,
        'clientes':clientes
    }
    return render(request,'clientes/interfaz_clientes.html',context)

def registrar_cliente(request):
    titulo="Registrar nuevo cliente"
    if request.method == "POST":
        form= ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect_stderr('clientes')
        else:
            print('Error')
    else:
        form= ClienteForm()

    context={
        'titulo':titulo,
        'form':form
    }
    return render(request, 'clientes/frm_registrar_cliente.html',context)