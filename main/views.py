from multiprocessing import context
from django.shortcuts import render, redirect
from django.views.defaults import page_not_found
from django.contrib import messages
from django.views.generic import View, TemplateView, ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from articulos.models import Articulos, Categoria, Marcas, Proveedores
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

# def loggedIn(request):
#     if request.user.is_authenticated:
#         respuesta:"Ingresado como: "  + request.user.username
#     else:
#         respuesta:"No estas autenticado."
#     return HttpResponse(respuesta)

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

def papelera_reciclaje(request):
    titulo = "Papelera de reciclaje"
    clientes = Cliente.objects.filter(cli_estado = '0')
    ciudades = Ciudades.objects.filter(ciu_estado = '0')
    departamentos = Departamentos.objects.filter(dep_estado = '0')
    marcas = Marcas.objects.filter(mar_estado = '0')
    articulos = Articulos.objects.filter(art_estado = '0')
    categorias = Categoria.objects.filter(cat_estado = '0')
    proveedores = Proveedores.objects.filter(pro_estado = '0')
    vehiculos = Vehiculo.objects.filter(veh_estado = '0')
    empleado = Empleados.objects.filter(emp_estado = '0')
    servicios = Servicios.objects.filter(ser_estado = '0')
    sucursales = Sucursales.objects.filter(suc_estado = '0')
    ordenes = OrdenServicio.objects.filter(ser_estado = '0')
    context = {
        'titulo':titulo,
        'clientes':clientes,
        'ciudades':ciudades,
        'departamentos':departamentos,
        'marcas':marcas,
        'articulos':articulos,
        'categorias':categorias,
        'proveedores':proveedores,
        'vehiculos':vehiculos,
        'empleado':empleado,
        'servicios':servicios,
        'sucursales':sucursales,
        'ordenes':ordenes,
    }
    return render(request, 'interfaz_papelera.html', context)

def restablecer_cliente(request, pk):
    titulo = "Eliminar cliente"
    clientes = Cliente.objects.all()

    Cliente.objects.filter(id=pk).update(
        cli_estado='1'
    )
    messages.success(
        request,f"Se ha restablecido el registro exitosamente"
    )
    return redirect('clientes')

    context = {
        'titulo': titulo,
        'clientes': clientes
    }
    return render(request, 'usuarios/interfaz_clientes.html', context)


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
        ciu_estado='1'
    )
    messages.success(
        request,f"Se restableció el registro exitosamente"
    )
    return redirect('ciudades')

    context = {
        'titulo': titulo,
        'ciudades': ciudades
    }
    return render(request, 'usuarios/interfaz_ciu_municipios.html', context)

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
        dep_estado='1'
    )
    messages.success(
        request,f"Se restableció el registro exitosamente"
    )
    return redirect('departamentos')

    context = {
        'titulo': titulo,
        'departamento': departamento
    }
    return render(request, 'usuarios/interfaz_departamentos.html', context)

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
        mar_estado='1'
    )
    messages.success(
        request,f"Se restableció el registro exitosamente"
    )
    return redirect('marcas')

    context = {
        'titulo': titulo,
        'marca': marca
    }
    return render(request, 'usuarios/interfaz_marcas.html', context)

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
        cat_estado='1'
    )
    messages.success(
        request,f"Se restableció el registro exitosamente"
    )
    return redirect('categorias')

    context = {
        'titulo': titulo,
        'categoria': categoria
    }
    return render(request, 'usuarios/interfaz_categorias.html', context)

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
        pro_estado='1'
    )
    messages.success(
        request,f"Se restableció el registro exitosamente"
    )
    return redirect('proveedores')

    context = {
        'titulo': titulo,
        'proveedor': proveedor
    }
    return render(request, 'usuarios/interfaz_proveedores.html', context)

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

def restablecer_articulo(request, pk):
    titulo = "Restablecer artículo"
    articulo = Articulos.objects.all()

    Articulos.objects.filter(id=pk).update(
        art_estado='1'
    )
    messages.success(
        request,f"Se restableció el registro exitosamente"
    )
    return redirect('articulos')

    context = {
        'titulo': titulo,
        'articulo': articulo
    }
    return render(request, 'usuarios/interfaz_proveedores.html', context)

def eliminar_def_articulo(request, pk):
    titulo = "Eliminar artículo"
    articulo = Articulos.objects.filter(id=pk).delete()
    messages.warning(
        request,f"Se eliminó definitivamente el registro"
    )
    return redirect('papelera')

    context = {
        'titulo': titulo,
        'articulo': articulo
    }
    return render(request, 'interfaz_papelera.html', context)

def restablecer_vehiculo(request, pk):
    titulo = "Restablecer vehículo"
    vehiculo = Vehiculo.objects.all()

    Vehiculo.objects.filter(id=pk).update(
        veh_estado='1'
    )
    messages.success(
        request,f"Se restableció el registro exitosamente"
    )
    return redirect('vehiculos')

    context = {
        'titulo': titulo,
        'vehiculo': vehiculo
    }
    return render(request, 'usuarios/vehiculos_registrados.html', context)

def eliminar_def_vehiculo(request, pk):
    titulo = "Eliminar vehículo"
    vehiculo = Vehiculo.objects.filter(id=pk).delete()
    messages.warning(
        request,f"Se eliminó definitivamente el registro"
    )
    return redirect('papelera')

    context = {
        'titulo': titulo,
        'vehiculo': vehiculo
    }
    return render(request, 'interfaz_papelera.html', context)

def restablecer_empleado(request, pk):
    titulo = "Restablecer empleado"
    empleado = Empleados.objects.all()

    Empleados.objects.filter(id=pk).update(
        emp_estado='1'
    )
    messages.success(
        request,f"Se restableció el registro exitosamente"
    )
    return redirect('empleados')

    context = {
        'titulo': titulo,
        'empleado': empleado
    }
    return render(request, 'usuarios/interfaz_empleado_usuarios.html', context)

def eliminar_def_empleado(request, pk):
    titulo = "Eliminar vehículo"
    empleado = Empleados.objects.filter(id=pk).delete()
    messages.warning(
        request,f"Se eliminó definitivamente el registro"
    )
    return redirect('papelera')

    context = {
        'titulo': titulo,
        'empleado': empleado
    }
    return render(request, 'interfaz_papelera.html', context)

def restablecer_servicio(request, pk):
    titulo = "Restablecer servicio"
    servicio = Servicios.objects.all()

    Servicios.objects.filter(id=pk).update(
        ser_estado='1'
    )
    messages.success(
        request,f"Se restableció el registro exitosamente"
    )
    return redirect('servicios')

    context = {
        'titulo': titulo,
        'servicio': servicio
    }
    return render(request, 'usuarios/interfaz_servicios.html', context)

def eliminar_def_servicio(request, pk):
    titulo = "Eliminar servicio"
    servicio = Servicios.objects.filter(id=pk).delete()
    messages.warning(
        request,f"Se eliminó definitivamente el registro"
    )
    return redirect('papelera')

    context = {
        'titulo': titulo,
        'servicio': servicio
    }
    return render(request, 'interfaz_papelera.html', context)

def restablecer_sucursal(request, pk):
    Sucursales.objects.filter(id=pk).update(
        suc_estado='1'
    )
    messages.success(
        request,f"Se restableció el registro exitosamente"
    )
    return redirect('sucursales')

def eliminar_def_sucursal(request, pk):
    Sucursales.objects.filter(id=pk).delete()
    messages.warning(
        request,f"Se eliminó definitivamente el registro"
    )
    return redirect('papelera')

def restablecer_orden_ser(request, pk):
    OrdenServicio.objects.filter(id=pk).update(
        ser_estado='1'
    )
    messages.success(
        request,f"Se restableció el registro exitosamente"
    )
    return redirect('ordenes_servicio')

def eliminar_def_orden_ser(request, pk):
    OrdenServicio.objects.filter(id=pk).delete()
    messages.warning(
        request,f"Se eliminó definitivamente el registro"
    )
    return redirect('papelera')