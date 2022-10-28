from django.shortcuts import render, redirect
from multiprocessing import context
from articulos.forms import ArticulosForm, CategoriasForm, MarcasForm, ProveedoresForm
from django.contrib import messages

from articulos.models import Articulos, Categoria, Marcas, Proveedores


# Create your views here

def articulos(request):
     titulo = "Artículos"
     articulos = Articulos.objects.filter(ArtEstado = '1')
     context = {
        'titulo':titulo,
        'articulos':articulos
     }
     return render(request, 'articulos/interfaz_articulos.html', context)

def registrar_articulo(request):
    titulo = "Registrar nuevo artículo"
    if request.method == "POST":
        form = ArticulosForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,f"Se agregó el articulo {request.POST['ArtNombre']} exitosamente"
            )
            return redirect('articulos')
        else:
            print('Error')
    else:
        form = ArticulosForm()

    context = {
        'titulo': titulo,
        'form': form
    }
    return render(request, 'articulos/frm_registrar_articulos.html', context)

def editar_articulo(request, pk):
    titulo = "Editar artículo"
    articulo = Articulos.objects.get(id=pk)
    if request.method == "POST":
        form = ArticulosForm(request.POST, instance=articulo)
        if form.is_valid():
            form.save()
            messages.success(
                request,f"Se editó el artículo {request.POST['ArtNombre']} exitosamente"
            )
            return redirect('articulos')
        else:
            print('Error al guardar')
    else:
        form = ArticulosForm(instance=articulo)

    context = {
        'titulo': titulo,
        'form': form
    }
    return render(request, 'articulos/frm_registrar_articulos.html', context)

def eliminar_articulo(request, pk):
    titulo = "Eliminar artículo"
    articulo = Articulos.objects.all()

    Articulos.objects.filter(id=pk).update(
        ArtEstado='0'
    )
    messages.success(
        request,f"Se eliminó el artículo exitosamente"
    )
    return redirect('articulos')

    context = {
        'titulo': titulo,
        'articulo': articulo
    }
    return render(request, 'articulos/frm_registrar_articulos.html', context)

def categorias(request):
    titulo = "Categorías en artículos"
    categorias = Categoria.objects.filter(CatEstado = '1')
    if request.method == "POST":
        form = CategoriasForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,f"Se agregó la categoría {request.POST['CatNombre']} exitosamente"
            )
            return redirect('categorias')
        else:
            print('Error')
    else:
        form = CategoriasForm()
    context = {
        'titulo': titulo,
        'categorias': categorias,
        'form': form
    }
    return render(request, 'articulos/interfaz_categorias.html', context)


def editar_categoria(request, pk):
    titulo = "Editar categoría"
    categoria = Categoria.objects.get(id=pk)
    if request.method == "POST":
        form = CategoriasForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            messages.success(
                request,f"Se editó la categoría {request.POST['CatNombre']} exitosamente"
            )
            return redirect('categorias')
        else:
            print('Error al guardar')
    else:
        form = CategoriasForm(instance=categoria)

    context = {
        'titulo': titulo,
        'form': form
    }
    return render(request, 'articulos/interfaz_categorias.html', context)

def eliminar_categoria(request, pk):
    titulo = "Eliminar categoria"
    ciudad = Categoria.objects.all()

    Categoria.objects.filter(id=pk).update(
        CatEstado='0'
    )
    # messages.WARNING(
    #     request,f"Se elimino la categoría {request.POST['']} exitosamente" #pregunta
    # )    
    return redirect('categorias')

    context = {
        'titulo': titulo,
        'ciudad': ciudad
    }
    return render(request, 'articulos/interfaz_categorias.html', context)

def marcas(request):
    titulo = "Marcas"
    marcas = Marcas.objects.filter(MarEstado = '1')
    if request.method == "POST":
        form = MarcasForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,f"Se agregó la marca {request.POST['MarNombre']} exitosamente"
            )
            return redirect('marcas')
        else:
            print('Error')
    else:
        form = MarcasForm()
    context = {
        'titulo': titulo,
        'marcas': marcas,
        'form': form
    }
    return render(request, 'articulos/interfaz_marcas.html', context)

def editar_marca(request, pk):
    titulo = "Editar marca"
    marca = Marcas.objects.get(id=pk)
    if request.method == "POST":
        form = MarcasForm(request.POST, instance=marca)
        if form.is_valid():
            form.save()
            messages.success(
                request,f"Se editó la marca {request.POST['MarNombre']} exitosamente"
            )
            return redirect('marcas')
        else:
            print('Error al guardar')
    else:
        form = MarcasForm(instance=marca)

    context = {
        'titulo': titulo,
        'form': form
    }
    return render(request, 'articulos/interfaz_marcas.html', context)

def eliminar_marca(request, pk):
    titulo = "Eliminar marca"
    marca = Marcas.objects.all()

    Marcas.objects.filter(id=pk).update(
        MarEstado='0'
    )
    messages.success(
        request,f"Se eliminó la marca exitosamente"
    )
    return redirect('marcas')

    context = {
        'titulo': titulo,
        'marca': marca
    }
    return render(request, 'articulos/interfaz_marcas.html', context)

def proveedores(request):
    titulo = "Proveedores"
    proveedores = Proveedores.objects.filter(ProEstado = '1')  # ver formulario
    context = {
        'titulo': titulo,
        'proveedores': proveedores
    }
    return render(request, 'articulos/interfaz_proveedores.html', context)

def registrar_proveedor(request):
    titulo = "Registrar nuevo proveedor"
    if request.method == "POST":
        form = ProveedoresForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,f"Se agregó el proveedor {request.POST['ProNombre']} exitosamente"
            )
            return redirect('proveedores')
        else:
            print('Error')
    else:
        form = ProveedoresForm()

    context = {
        'titulo': titulo,
        'form': form
    }
    return render(request, 'articulos/frm_registrar_proveedores.html', context)

def editar_proveedor(request, pk):
    titulo = "Editar proveedor"
    proveedor = Proveedores.objects.get(id=pk)
    if request.method == "POST":
        form = ProveedoresForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            messages.success(
                request,f"Se editó el proveedor {request.POST['ProNombre']} exitosamente"
            )
            return redirect('proveedores')
        else:
            print('Error al guardar')
    else:
        form = ProveedoresForm(instance=proveedor)

    context = {
        'titulo': titulo,
        'form': form
    }
    return render(request, 'articulos/frm_registrar_proveedores.html', context)

def eliminar_proveedor(request, pk):
    titulo = "Eliminar proveedor"
    proveedor = Proveedores.objects.all()

    Proveedores.objects.filter(id=pk).update(
        ProEstado='0'
    )
    messages.success(
        request,f"Se eliminó el proveedor exitosamente"
    )
    return redirect('proveedores')

    context = {
        'titulo': titulo,
        'proveedor': proveedor
    }
    return render(request, 'articulos/frm_registrar_proveedores.html', context)