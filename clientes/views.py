from contextlib import redirect_stderr
from multiprocessing import context
from django.shortcuts import redirect, render
from django.contrib import messages

from clientes.forms import CiudadesForm, ClienteForm, DepartamentosForm
from clientes.models import Ciudades, Cliente, Departamentos

# Create your views here.


def clientes(request):
    titulo = "Clientes"
    clientes = Cliente.objects.filter(CliEstado = '1')  # guardar formulario
    context = {
        'titulo': titulo,
        'clientes': clientes
    }
    return render(request, 'clientes/interfaz_clientes.html', context)


def registrar_cliente(request):
    titulo = "Registrar nuevo cliente"
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clientes')
        else:
            print('Error')
    else:
        form = ClienteForm()

    context = {
        'titulo': titulo,
        'form': form
    }
    return render(request, 'clientes/frm_registrar_cliente.html', context)


def editar_cliente(request, pk):
    titulo = "Editar cliente"
    cliente = Cliente.objects.get(id=pk)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('clientes')
        else:
            print('Error al guardar')
    else:
        form = ClienteForm(instance=cliente)

    context = {
        'titulo': titulo,
        'form': form
    }
    return render(request, 'clientes/frm_registrar_cliente.html', context)


def eliminar_cliente(request, pk):
    titulo = "Eliminar cliente"
    clientes = Cliente.objects.all()

    Cliente.objects.filter(id=pk).update(
        CliEstado='0'
    )

    return redirect('clientes')

    context = {
        'titulo': titulo,
        'clientes': clientes
    }
    return render(request, 'clientes/interfaz_clientes.html', context)

def ciudades(request):
    titulo = "Ciudades y municipios"
    ciudades = Ciudades.objects.filter(CiuEstado = '1')
    if request.method == "POST":
        form = CiudadesForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,f"Se agregó la ciudad o municipio {request.POST['CiuNombre']} exitosamente"
            )
            return redirect('ciudades')
        else:
            print('Error')
    else:
        form = CiudadesForm()
    context = {
        'titulo': titulo,
        'ciudades': ciudades,
        'form': form
    }
    return render(request, 'clientes/interfaz_ciu_municipios.html', context)


def editar_ciudad(request, pk):
    titulo = "Editar ciudad"
    ciudad = Ciudades.objects.get(id=pk)
    if request.method == "POST":
        form = CiudadesForm(request.POST, instance=ciudad)
        if form.is_valid():
            form.save()
            return redirect('ciudades')
        else:
            print('Error al guardar')
    else:
        form = CiudadesForm(instance=ciudad)

    context = {
        'titulo': titulo,
        'form': form
    }
    return render(request, 'clientes/interfaz_ciu_municipios.html', context)


def eliminar_ciudad(request, pk):
    titulo = "Eliminar ciudad"
    ciudad = Ciudades.objects.all()

    Ciudades.objects.filter(id=pk).update(
        CiuEstado='0'
    )

    return redirect('ciudades')

    context = {
        'titulo': titulo,
        'ciudad': ciudad
    }
    return render(request, 'clientes/interfaz_ciu_municipios.html', context)


def departamentos(request):
    titulo = "Departamentos"
    departamentos = Departamentos.objects.filter(DepEstado = '1')
    if request.method == 'POST':
        form = DepartamentosForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,f"Se agregó el departamento {request.POST['DepNombre']} exitosamente"
            )
            return redirect('departamentos')
        else:
            print('Error')
    else:
        form = DepartamentosForm()
    context = {
        'titulo': titulo,
        'departamentos': departamentos,
        'form': form
    }
    return render(request, 'clientes/interfaz_departamentos.html', context)


def editar_departamento(request, pk):
    titulo = "Editar departamento"
    departamento = Departamentos.objects.get(id=pk)
    if request.method == "POST":
        form = DepartamentosForm(request.POST, instance=departamento)
        if form.is_valid():
            form.save()
            return redirect('departamentos')
        else:
            print('Error al guardar')
    else:
        form = DepartamentosForm(instance=departamento)

    context = {
        'titulo': titulo,
        'form': form
    }
    return render(request, 'clientes/interfaz_departamentos.html', context)


def eliminar_departamento(request, pk):
    titulo = "Eliminar departamento"
    departamento = Departamentos.objects.all()
    Departamentos.objects.filter(id=pk).update(
        DepEstado='0'
    )
    return redirect('departamentos')
    context = {
        'titulo': titulo,
        'departamento': departamento
    }
    return render(request, 'clientes/interfaz_departamentos.html', context)
