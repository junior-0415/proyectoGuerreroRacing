from django.shortcuts import render, redirect
from multiprocessing import context
from articulos.forms import ArticulosForm, CategoriasForm, MarcasForm, ProveedoresForm
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required, permission_required

from articulos.models import Articulos, Categoria, Marcas, Proveedores


# Create your views here

@login_required(login_url='login')
@permission_required('articulos.view_articulos')
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

@login_required(login_url='login')
@permission_required('articulos.add_articulos')
def registrar_articulo(request):
    titulo = "Registrar nuevo artículo"
    if request.method == "POST":
        form = ArticulosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(
                request,f"Se agregó el articulo {request.POST['art_nombre']} exitosamente"
            )
            return redirect('articulos')
        else:
            messages.error(
                request,f"Se ha producido un error al guardar el artículo"
            )
    else:
        form = ArticulosForm()

    context = {
        'titulo': titulo,
        'form': form
    }
    return render(request, 'articulos/frm_registrar_articulos.html', context)

@login_required(login_url='login')
@permission_required('articulos.change_articulos')
def editar_articulo(request, pk):
    titulo = "Editar artículo"
    articulo = Articulos.objects.get(id=pk)
    if request.method == "POST":
        form = ArticulosForm(request.POST, request.FILES, instance=articulo)
        if form.is_valid():
            form.save()
            messages.success(
                request,f"Se editó el artículo {request.POST['art_nombre']} exitosamente"
            )
            return redirect('articulos')
        else:
            messages.error(
                request,f"Se ha producido un error al editar el artículo"
            )
    else:
        form = ArticulosForm(instance=articulo)

    context = {
        'titulo': titulo,
        'form': form
    }
    return render(request, 'articulos/frm_registrar_articulos.html', context)

@login_required(login_url='login')
@permission_required('articulos.delete_articulos')
def eliminar_articulo(request, pk):
    Articulos.objects.filter(id=pk).update(
        art_estado='0'
    )
    messages.success(
        request,f"El artículo se eliminó exitosamente"
    )
    return redirect('articulos')

@login_required(login_url='login')
@permission_required('articulos.view_categoria')
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
            messages.error(
                request,f"Se ha producido un error al guardar la categoría"
            )
    else:
        form = CategoriasForm()
    context = {
        'titulo': titulo,
        'categorias': categorias,
        'form': form
    }
    return render(request, 'articulos/interfaz_categorias.html', context)

@login_required(login_url='login')
@permission_required('articulos.change_categoria')
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
            messages.error(
                request,f"Se ha producido un error al editar la categoría"
            )
    else:
        form = CategoriasForm(instance=categoria)

    context = {
        'titulo': titulo,
        'form': form
    }
    return render(request, 'articulos/interfaz_categorias.html', context)

@login_required(login_url='login')
@permission_required('articulos.delete_categoria')
def eliminar_categoria(request, pk):
    Categoria.objects.filter(id=pk).update(
        cat_estado='0'
    )
    messages.success(
        request,f"La categoría se eliminó exitosamente"
    )    
    return redirect('categorias')

@login_required(login_url='login')
@permission_required('articulos.view_marcas')
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
            messages.error(
                request,f"Se ha producido un error al guardar la marca"
            )
    else:
        form = MarcasForm()
    context = {
        'titulo': titulo,
        'marcas': marcas,
        'form': form
    }
    return render(request, 'articulos/interfaz_marcas.html', context)


@login_required(login_url='login')
@permission_required('articulos.change_marcas')
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
            messages.error(
                request,f"Se ha producido un error al editar la marca"
            )
    else:
        form = MarcasForm(instance=marca)

    context = {
        'titulo': titulo,
        'form': form
    }
    return render(request, 'articulos/interfaz_marcas.html', context)

@login_required(login_url='login')
@permission_required('articulos.delete_marcas')
def eliminar_marca(request, pk):
    Marcas.objects.filter(id=pk).update(
        mar_estado='0'
    )
    messages.success(
        request,f"La marca se eliminó exitosamente"
    )
    return redirect('marcas')

@login_required(login_url='login')
@permission_required('articulos.view_proveedores')
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

@login_required(login_url='login')
@permission_required('articulos.add_proveedores')
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
            messages.error(
                request,f"Se ha producido un error al guardar el proveedor"
            )
    else:
        form = ProveedoresForm()

    context = {
        'titulo': titulo,
        'form': form
    }
    return render(request, 'articulos/frm_registrar_proveedores.html', context)

@login_required(login_url='login')
@permission_required('articulos.change_proveedores')
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
            messages.error(
                request,f"Se ha producido un error al editar el proveedor"
            )
    else:
        form = ProveedoresForm(instance=proveedor)

    context = {
        'titulo': titulo,
        'form': form
    }
    return render(request, 'articulos/frm_registrar_proveedores.html', context)

@login_required(login_url='login')
@permission_required('articulos.delete_proveedores')
def eliminar_proveedor(request, pk):
    Proveedores.objects.filter(id=pk).update(
        pro_estado='0'
    )
    messages.success(
        request,f"El proveedor se eliminó exitosamente"
    )
    return redirect('proveedores')