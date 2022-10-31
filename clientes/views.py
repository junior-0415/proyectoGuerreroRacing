from contextlib import redirect_stderr
from multiprocessing import context
from xml.dom.minidom import Document
from django.shortcuts import redirect, render
from django.contrib import messages

from clientes.forms import CiudadesForm, ClienteForm, DepartamentosForm, VehiculosForm
from clientes.models import Ciudades, Cliente, Departamentos, Vehiculo

# Create your views here.


def clientes(request):
    titulo = "Clientes"
    clientes = Cliente.objects.filter(cli_estado = '1')  # guardar formulario
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
            messages.success(
                request,f"Se ha registrado el cliente {request.POST['cli_nombre']} exitosamente"
            )
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
            messages.success(
                request,f"Se editó el cliente {request.POST['cli_nombre']} exitosamente"
            )
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
        cli_estado='0'
    )
    messages.success(
        request,f"Se eliminó el cliente exitosamente"
    )
    return redirect('clientes')

    context = {
        'titulo': titulo,
        'clientes': clientes
    }
    return render(request, 'clientes/interfaz_clientes.html', context)


def ciudades(request):
    titulo = "Ciudades y municipios"
    ciudades = Ciudades.objects.filter(ciu_estado = '1')
    if request.method == "POST":
        form = CiudadesForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,f"Se agregó la ciudad o municipio {request.POST['ciu_nombre']} exitosamente"
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
            messages.success(
                request,f"Se editó la ciudad o municipio {request.POST['ciu_nombre']} exitosamente"
            )
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
        ciu_estado='0'
    )
    messages.success(
        request,f"Se editó la ciudad o municipio exitosamente"
    )
    return redirect('ciudades')

    context = {
        'titulo': titulo,
        'ciudad': ciudad
    }
    return render(request, 'clientes/interfaz_ciu_municipios.html', context)


def departamentos(request):
    titulo = "Departamentos"
    departamentos = Departamentos.objects.filter(dep_estado = '1')
    if request.method == 'POST':
        form = DepartamentosForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,f"Se agregó el departamento {request.POST['Dep_Nombre']} exitosamente"
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
            messages.success(
                request,f"Se editó {request.POST['dep_nombre']} exitosamente"
            )
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
        dep_estado='0'
    )
    messages.success(
        request,f"Se eliminó exitosamente el registro"
    )
    return redirect('departamentos')
    context = {
        'titulo': titulo,
        'departamento': departamento
    }
    return render(request, 'clientes/interfaz_departamentos.html', context)

def vehiculos(request):
    titulo = "Vehículos"
    vehiculos = Vehiculo.objects.filter(veh_estado = '1')
    context = {
        'titulo': titulo,
        'vehiculos': vehiculos
    }
    return render(request, 'clientes/vehiculos_registrados.html', context)

def registrar_vehiculo(request):
    titulo = "Registrar vehículo"
    if request.method == "POST":
        form = VehiculosForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,f"Se ha registrado el vehículo {request.POST['id_matricula']} exitosamente"
            )
            return redirect('vehiculos')
        else:
            print('Error')
    else:
        form = VehiculosForm()

    context = {
        'titulo': titulo,
        'form': form
    }
    return render(request, 'clientes/frm_registrar_nuevo_vehiculo.html', context)

def editar_vehiculo(request, pk):
    titulo = "Editar vehículo"
    vehiculo = Vehiculo.objects.get(id=pk)
    if request.method == "POST":
        form = VehiculosForm(request.POST, instance=vehiculo)
        if form.is_valid():
            form.save()
            messages.success(
                request,f"Se editó el vehículo {request.POST['id_matricula']} exitosamente"
            )
            return redirect('vehiculos')
        else:
            print('Error al guardar')
    else:
        form = VehiculosForm(instance=vehiculo)

    context = {
        'titulo': titulo,
        'form': form
    }
    return render(request, 'clientes/frm_registrar_nuevo_vehiculo.html', context)


def eliminar_vehiculo(request, pk):
    titulo = "Eliminar vehículo"
    vehiculo = Vehiculo.objects.all()

    Vehiculo.objects.filter(id=pk).update(
        veh_estado='0'
    )
    messages.success(
        request,f"Se eliminó el vehículo exitosamente"
    )
    return redirect('vehiculos')

    context = {
        'titulo': titulo,
        'vehiculo': vehiculo
    }
    return render(request, 'clientes/vehiculos_registrados.html', context)

def vehiculos_taller(request):
    titulo = "Vehículos en taller"
    vehiculos = Vehiculo.objects.filter(veh_taller = 'Si', veh_estado = '1')
    context = {
        'titulo': titulo,
        'vehiculos': vehiculos
    }
    return render(request, 'clientes/interfaz_vehiculos_en_taller.html', context)

def editar_vehiculo_taller(request, pk):
    titulo = "Editar vehículo"
    vehiculo = Vehiculo.objects.get(id=pk)
    if request.method == "POST":
        form = VehiculosForm(request.POST, instance=vehiculo)
        if form.is_valid():
            form.save()
            messages.success(
                request,f"Se editó el vehículo {request.POST['id_matricula']} exitosamente"
            )
            return redirect('vehiculos_taller')
        else:
            print('Error al guardar')
    else:
        form = VehiculosForm(instance=vehiculo)

    context = {
        'titulo': titulo,
        'form': form,
    }
    return render(request, 'clientes/frm_registrar_nuevo_vehiculo.html', context)

def sacar_vehiculo_taller(request, pk):
    titulo = "Sacar vehículo del taller"
    vehiculo = Vehiculo.objects.all()
    Vehiculo.objects.filter(id=pk).update(
        veh_taller='No'
    )
    messages.success(
        request,f"El vehiculo ha salido del taller"
    )
    return redirect('vehiculos_taller')

    context = {
        'titulo': titulo,
        'vehiculo': vehiculo
    }
    return render(request, 'clientes/interfaz_vehiculos_en_taller.html', context)

def ingresar_vehiculo_taller(request, pk):
    titulo = "ingresar vehículo del taller"
    vehiculo = Vehiculo.objects.all()
    Vehiculo.objects.filter(id=pk).update(
        veh_taller='Si'
    )
    messages.success(
        request,f"El vehiculo se ha ingresado al taller"
    )
    return redirect('vehiculos_taller')

    context = {
        'titulo': titulo,
        'vehiculo': vehiculo
    }
    return render(request, 'clientes/interfaz_vehiculos_en_taller.html', context)