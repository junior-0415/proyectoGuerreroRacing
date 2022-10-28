from multiprocessing import context
from django.shortcuts import render, redirect
from django.views.defaults import page_not_found
from django.contrib import messages
from articulos.models import Articulos, Categoria, Marcas, Proveedores

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
    marcas = Marcas.objects.filter(MarEstado = '0')
    articulos = Articulos.objects.filter(ArtEstado = '0')
    categorias = Categoria.objects.filter(CatEstado = '0')
    proveedores = Proveedores.objects.filter(ProEstado = '0')
    context = {
        'titulo':titulo,
        'clientes':clientes,
        'ciudades':ciudades,
        'departamentos':departamentos,
        'marcas':marcas,
        'articulos':articulos,
        'categorias':categorias,
        'proveedores':proveedores
    }
    return render(request, 'interfaz_papelera.html', context)

def restablecer_cliente(request, pk):
    titulo = "Eliminar cliente"
    clientes = Cliente.objects.all()

    Cliente.objects.filter(id=pk).update(
        CliEstado='1'
    )
    messages.success(
        request,f"Se ha restablecido el registro exitosamente"
    )
    return redirect('clientes')

    context = {
        'titulo': titulo,
        'clientes': clientes
    }
    return render(request, 'clientes/interfaz_clientes.html', context)


def eliminar_def_cliente(request, pk):
    titulo = "Eliminar cliente"
    cliente = Cliente.objects.filter(id=pk).delete()
    messages.warning(
        request,f"Se ha eliminado definitivamente el registro"
    )
    return redirect('papelera')

    context = {
        'titulo': titulo,
        'cliente': cliente
    }
    return render(request, 'interfaz_papelera.html', context)

def restablecer_ciudad(request, pk):
    titulo = "Restablecer ciudad"
    ciudades = Ciudades.objects.all()

    Ciudades.objects.filter(id=pk).update(
        CiuEstado='1'
    )
    messages.success(
        request,f"Se restableció el registro exitosamente"
    )
    return redirect('ciudades')

    context = {
        'titulo': titulo,
        'ciudades': ciudades
    }
    return render(request, 'clientes/interfaz_ciu_municipios.html', context)

def eliminar_def_ciudad(request, pk):
    titulo = "Eliminar ciudad"
    ciudad = Ciudades.objects.filter(id=pk).delete()
    messages.warning(
        request,f"Se eliminó definitivamente el registro"
    )
    return redirect('papelera')

    context = {
        'titulo': titulo,
        'ciudad': ciudad
    }
    return render(request, 'interfaz_papelera.html', context)

def restablecer_departamento(request, pk):
    titulo = "Restablecer ciudad"
    departamento = Departamentos.objects.all()

    Departamentos.objects.filter(id=pk).update(
        DepEstado='1'
    )
    messages.success(
        request,f"Se restableció el registro exitosamente"
    )
    return redirect('departamentos')

    context = {
        'titulo': titulo,
        'departamento': departamento
    }
    return render(request, 'clientes/interfaz_departamentos.html', context)

def eliminar_def_depart(request, pk):
    titulo = "Eliminar departamento"
    depart = Departamentos.objects.filter(id=pk).delete()
    messages.warning(
        request,f"Se eliminó definitivamente el registro"
    )
    return redirect('papelera')

    context = {
        'titulo': titulo,
        'depart': depart
    }
    return render(request, 'interfaz_papelera.html', context)

def restablecer_marca(request, pk):
    titulo = "Restablecer marca"
    marca = Marcas.objects.all()

    Marcas.objects.filter(id=pk).update(
        MarEstado='1'
    )
    messages.success(
        request,f"Se restableció el registro exitosamente"
    )
    return redirect('marcas')

    context = {
        'titulo': titulo,
        'marca': marca
    }
    return render(request, 'clientes/interfaz_marcas.html', context)

def eliminar_def_marca(request, pk):
    titulo = "Eliminar marca"
    marca = Marcas.objects.filter(id=pk).delete()
    messages.warning(
        request,f"Se eliminó definitivamente el registro"
    )
    return redirect('papelera')

    context = {
        'titulo': titulo,
        'marca': marca
    }
    return render(request, 'interfaz_papelera.html', context)

def restablecer_categoria(request, pk):
    titulo = "Restablecer categoría"
    categoria = Categoria.objects.all()

    Categoria.objects.filter(id=pk).update(
        CatEstado='1'
    )
    messages.success(
        request,f"Se restableció el registro exitosamente"
    )
    return redirect('categorias')

    context = {
        'titulo': titulo,
        'categoria': categoria
    }
    return render(request, 'articulos/interfaz_categorias.html', context)

def eliminar_def_categoria(request, pk):
    titulo = "Eliminar categoria"
    categoria = Categoria.objects.filter(id=pk).delete()
    messages.warning(
        request,f"Se eliminó definitivamente el registro"
    )
    return redirect('papelera')

    context = {
        'titulo': titulo,
        'categoria': categoria
    }
    return render(request, 'interfaz_papelera.html', context)

def restablecer_proveedor(request, pk):
    titulo = "Restablecer proveedor"
    proveedor = Proveedores.objects.all()

    Proveedores.objects.filter(id=pk).update(
        ProEstado='1'
    )
    messages.success(
        request,f"Se restableció el registro exitosamente"
    )
    return redirect('proveedores')

    context = {
        'titulo': titulo,
        'proveedor': proveedor
    }
    return render(request, 'articulos/interfaz_proveedores.html', context)

def eliminar_def_proveedor(request, pk):
    titulo = "Eliminar proveedor"
    proveedor = Proveedores.objects.filter(id=pk).delete()
    messages.warning(
        request,f"Se eliminó definitivamente el registro"
    )
    return redirect('papelera')

    context = {
        'titulo': titulo,
        'proveedor': proveedor
    }
    return render(request, 'interfaz_papelera.html', context)