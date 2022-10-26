from multiprocessing import context
from django.shortcuts import render, redirect
from django.views.defaults import page_not_found

from clientes.models import Cliente, Ciudades, Departamentos

def inicio(request):
    context = {}
    return render(request, 'index.html', context)


def login(request):
    titulo = "Iniciar sesión"
    context = {
        'titulo': titulo
    }
    return render(request, 'login.html', context)


def inicioAdmin(request):
    titulo = "Panel Principal"
    context = {
        'titulo': titulo
    }
    return render(request, 'frm_inicio_app.html', context)

def error_404(request, exception):
    return page_not_found(request, 'error_404.html')

def papelera_reciclaje(request):
    titulo = "Papelera de reciclaje"
    clientes = Cliente.objects.filter(CliEstado = '0')
    ciudades = Ciudades.objects.filter(CiuEstado = '0')
    departamentos = Departamentos.objects.filter(DepEstado = '0')
    context = {
        'titulo':titulo,
        'clientes':clientes,
        'ciudades':ciudades,
        'departamentos':departamentos
    }
    return render(request, 'interfaz_papelera.html', context)

def eliminar_def_cliente(request, pk):
    titulo = "Eliminar cliente"
    cliente = Cliente.objects.filter(id=pk).delete()

    return redirect('papelera')

    context = {
        'titulo': titulo,
        'cliente': cliente
    }
    return render(request, 'interfaz_papelera.html', context)
