from django.shortcuts import render, redirect
from multiprocessing import context
from articulos.forms import ArticulosForm, CategoriasForm, MarcasForm, ProveedoresForm
from django.contrib import messages
from django.db.models import Q

from articulos.models import Articulos, Categoria, Marcas, Proveedores


# Create your views here

def articulos(request):
    titulo = "Artículos"
    articulos = Articulos.objects.filter(art_estado = '1')
    busqueda = request.GET.get('art_busqueda')
    if busqueda:
        articulos = Articulos.objects.filter(
            Q(id__icontains = busqueda) |
            Q(art_nombre__icontains = busqueda)
        ).distinct()
    context = {
        'titulo':titulo,
        'articulos':articulos,
    }
    return render(request, 'articulos/interfaz_articulos.html', context)

def registrar_articulo(request):
    titulo = "Registrar nuevo artículo"
    if request.method == "POST":
        form = ArticulosForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,f"Se agregó el articulo {request.POST['art_nombre']} exitosamente"
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
                request,f"Se editó el artículo {request.POST['art_nombre']} exitosamente"
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
    Articulos.objects.filter(id=pk).update(
        art_estado='0'
    )
    messages.success(
        request,f"El artículo se envió a papelera exitosamente"
    )
    return redirect('articulos')

def categorias(request):
    titulo = "Categorías en artículos"
    categorias = Categoria.objects.filter(cat_estado = '1')
    busqueda = request.GET.get('cat_busqueda')
    if busqueda:
        categorias = Categoria.objects.filter(
            Q(id__icontains = busqueda) |
            Q(cat_nombre__icontains = busqueda)
        ).distinct()
    if request.method == "POST":
        form = CategoriasForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,f"Se agregó la categoría {request.POST['cat_nombre']} exitosamente"
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
                request,f"Se editó la categoría {request.POST['cat_nombre']} exitosamente"
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
    Categoria.objects.filter(id=pk).update(
        cat_estado='0'
    )
    messages.success(
        request,f"La categoría se envió a papelera exitosamente"
    )    
    return redirect('categorias')

def marcas(request):
    titulo = "Marcas"
    marcas = Marcas.objects.filter(mar_estado = '1')
    busqueda = request.GET.get('mar_busqueda')
    if busqueda:
        marcas = Marcas.objects.filter(
            Q(id__icontains = busqueda) |
            Q(mar_nombre__icontains = busqueda)
        ).distinct()
    if request.method == "POST":
        form = MarcasForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,f"Se agregó la marca {request.POST['mar_nombre']} exitosamente"
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
                request,f"Se editó la marca {request.POST['mar_nombre']} exitosamente"
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
    Marcas.objects.filter(id=pk).update(
        mar_estado='0'
    )
    messages.success(
        request,f"La marca se envió a papelera exitosamente"
    )
    return redirect('marcas')

def proveedores(request):
    titulo = "Proveedores"
    proveedores = Proveedores.objects.filter(pro_estado = '1')  # ver formulario
    busqueda = request.GET.get('pro_busqueda')
    if busqueda:
        proveedores = Proveedores.objects.filter(
            Q(id__icontains = busqueda) |
            Q(pro_nit__icontains = busqueda) |
            Q(pro_nombre__icontains = busqueda)
        ).distinct()
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
                request,f"Se agregó el proveedor {request.POST['pro_nombre']} exitosamente"
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
                request,f"Se editó el proveedor {request.POST['pro_nombre']} exitosamente"
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
    Proveedores.objects.filter(id=pk).update(
        pro_estado='0'
    )
    messages.success(
        request,f"El proveedor se envió a papelera exitosamente"
    )
    return redirect('proveedores')