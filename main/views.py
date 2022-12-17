from multiprocessing import context
from django.shortcuts import render, redirect
from django.views.defaults import page_not_found
from django.contrib import messages
from django.views.generic import View, TemplateView, ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from articulos.models import Articulos, Categoria, Marcas, Proveedores
from inventario.models import Pedidos
from usuarios.models import Ciudades, Cliente, Departamentos, Empleados, OrdenServicio, Servicios, Sucursales, Vehiculo

#from clientes.models import Cliente, Ciudades, Departamentos, Vehiculo

def inicio(request):
    context = {

    }
    return render(request, 'index.html', context)

def nosotros(request):
    titulo = "Nosotros"
    context = {
        'titulo': titulo
    }
    return render(request, 'nosotros.html', context)

def soporte_ayuda(request):
    titulo = "Soporte y ayuda"
    context = {
        'titulo': titulo
    }
    return render(request, 'interfaz_soporte_ayuda.html', context)

def logout_user(request):
    logout(request)
    return redirect('inicio')


@login_required(login_url='login')
def inicioAdmin(request):
    titulo = "Panel Principal"
    context = {
        'titulo': titulo
    }
    return render(request, 'frm_inicio_app.html', context)

# def error_404(request, exception):
#     return page_not_found(request, 'error_404.html')

# class Error_404(TemplateView):
#     template_name = "error_404.html"

class Error404(TemplateView):
    template_name = "error_404.html"

class Error500(TemplateView):
    template_name = "error_500.html"

    @classmethod
    def as_error_view(cls):
        v = cls.as_view()
        def view(request):
            r = v(request)
            r.render()
            return r
        return view