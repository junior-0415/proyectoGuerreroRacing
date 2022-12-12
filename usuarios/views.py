from contextlib import redirect_stderr
from multiprocessing import context
from xml.dom.minidom import Document
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from articulos.models import Articulos
from usuarios.forms import CiudadesForm, ClienteForm, DepartamentosForm, EmpleadosForm, EmpresaForm, OrdenServicioForm, ServiciosForm, SucursalesForm, TblRelOrdenServicioArticulosForm, VehiculosForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Q

from django.views.generic import View
import os
from django.conf import settings
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.urls import reverse_lazy
from django.contrib.staticfiles import finders

from usuarios.models import Ciudades, Cliente, Departamentos, Empleados, Empresa, OrdenServicio, Servicios, Sucursales, TblRelOrdenServicioArticulos, Vehiculo

# Create your views here.

@login_required(login_url='login')
def empresa(request):
    titulo = "Tu empresa"
    empresa = Empresa.objects.filter(empr_estado = '1')
    context = {
        'titulo': titulo,
        'empresa': empresa,
    }
    return render(request, 'usuarios/interfaz_empresa.html', context)

def registrar_empresa(request):
    titulo = "Registrar empresa"
    if request.method == "POST":
        form = EmpresaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,f"Se registró tu empresa {request.POST['empr_nombre']} exitosamente"
            )
            return redirect('empresa')
        else:
            print('Error')
    else:
        form = EmpresaForm()
    context = {
        'titulo':titulo,
        'form':form
    }
    return render(request, 'usuarios/frm_empresa.html', context)

def editar_empresa(request, pk):
    titulo = 'Editar empresa'
    empresa = Empresa.objects.get(id=pk)
    if request.method == "POST":
        form = EmpresaForm(request.POST, instance=empresa)
        if form.is_valid():
            form.save()
            messages.success(
                request,f"Se editó la empresa {request.POST['empr_nombre']} exitosamente"
            )
            return redirect('empresa')
        else:
            print('Error al guardar')
    else:
        form = EmpresaForm(instance=empresa)

    context = {
        'titulo': titulo,
        'form': form
    }
    return render(request, 'usuarios/frm_empresa.html', context)

def sucursales(request):
    titulo = "Sucursales"
    sucursales = Sucursales.objects.filter(suc_estado = '1')
    if request.method == "POST":
        form = SucursalesForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,f"Se registró la sucursal {request.POST['suc_nombre']} exitosamente"
            )
            return redirect('sucursales')
        else:
            print('Error')
    else:
        form = SucursalesForm()
    context = {
        'titulo': titulo,
        'sucursales': sucursales,
        'form': form
    }
    return render(request, 'usuarios/interfaz_sucursales.html', context)

def editar_sucursal(request, pk):
    titulo = 'Editar sucursal'
    sucursal = Sucursales.objects.get(id=pk)
    if request.method == "POST":
        form = SucursalesForm(request.POST, instance=sucursal)
        if form.is_valid():
            form.save()
            messages.success(
                request,f"Se editó la sucursal {request.POST['suc_nombre']} exitosamente"
            )
            return redirect('sucursales')
        else:
            print('Error al guardar')
    else:
        form = SucursalesForm(instance=sucursal)

    context = {
        'titulo': titulo,
        'form': form
    }
    return render(request, 'usuarios/interfaz_sucursales.html', context)

def eliminar_sucursal(request, pk):
    Sucursales.objects.filter(id=pk).update(
        suc_estado='0'
    )
    messages.success(
        request,f"La sucursal se eliminó exitosamente"
    )
    return redirect('sucursales')

def servicios(request):
    titulo = "Servicios"
    servicios = Servicios.objects.filter(ser_estado = '1')
    busqueda = request.GET.get('serv_busqueda')
    if busqueda:
        servicios = Servicios.objects.filter(
            Q(ser_nombre__icontains = busqueda)
        ).distinct()
    if request.method == "POST":
        form = ServiciosForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,f"Se agregó el servicio {request.POST['ser_nombre']} exitosamente"
            )
            return redirect('servicios')
        else:
            print('Error')
    else:
        form = ServiciosForm()
    context = {
        'titulo': titulo,
        'servicios': servicios,
        'form': form
    }
    return render(request, 'usuarios/interfaz_servicios.html', context)

def editar_servicio(request, pk):
    titulo = "Editar servicio"
    servicio = Servicios.objects.get(id=pk)
    if request.method == "POST":
        form = ServiciosForm(request.POST, instance=servicio)
        if form.is_valid():
            form.save()
            messages.success(
                request,f"Se editó el servicio {request.POST['ser_nombre']} exitosamente"
            )
            return redirect('servicios')
        else:
            print('Error al guardar')
    else:
        form = ServiciosForm(instance=servicio)

    context = {
        'titulo': titulo,
        'form': form
    }
    return render(request, 'usuarios/interfaz_servicios.html', context)


def eliminar_servicio(request, pk):
    Servicios.objects.filter(id=pk).update(
        ser_estado='0'
    )
    messages.success(
        request,f"El servicio se eliminó exitosamente"
    )
    return redirect('servicios')

def clientes(request):
    titulo = "Clientes"
    clientes = Cliente.objects.filter(cli_estado = '1')
    busqueda = request.GET.get('cli_busqueda')
    if busqueda:
        clientes = Cliente.objects.filter(
            Q(id_identificacion__icontains = busqueda) |
            Q(cli_nombres__icontains = busqueda) |
            Q(cli_apellidos__icontains = busqueda)
        ).distinct()
    context = {
        'titulo': titulo,
        'clientes': clientes
    }
    return render(request, 'usuarios/interfaz_clientes.html', context)


def registrar_cliente(request):
    titulo = "Registrar nuevo cliente"
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,f"Se ha registrado el cliente {request.POST['cli_nombres']} exitosamente"
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
    return render(request, 'usuarios/frm_registrar_cliente.html', context)


def editar_cliente(request, pk):
    titulo = "Editar cliente"
    cliente = Cliente.objects.get(id=pk)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            messages.success(
                request,f"Se editó el cliente {request.POST['cli_nombres']} exitosamente"
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
    return render(request, 'usuarios/frm_registrar_cliente.html', context)


def eliminar_cliente(request, pk):
    Cliente.objects.filter(id=pk).update(
        cli_estado='0'
    )
    messages.success(
        request,f"El cliente se eliminó exitosamente"
    )
    return redirect('clientes')

@login_required(login_url='login')
@permission_required('usuarios.view_ciudades')
def ciudades(request):
    titulo = "Ciudades y municipios"
    ciudades = Ciudades.objects.filter(ciu_estado = '1')
    busqueda = request.GET.get('ciu_busqueda')
    if busqueda:
        ciudades = Ciudades.objects.filter(
            Q(id_ciudad__icontains = busqueda) |
            Q(ciu_nombre__icontains = busqueda)
        ).distinct()
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
    return render(request, 'usuarios/interfaz_ciu_municipios.html', context)


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
    return render(request, 'usuarios/interfaz_ciu_municipios.html', context)


def eliminar_ciudad(request, pk):
    Ciudades.objects.filter(id=pk).update(
        ciu_estado='0'
    )
    messages.success(
        request,f"La ciudad o municipio se eliminó exitosamente"
    )
    return redirect('ciudades')


def departamentos(request):
    titulo = "Departamentos"
    departamentos = Departamentos.objects.filter(dep_estado = '1')
    busqueda = request.GET.get('dep_busqueda')
    if busqueda:
        departamentos = Departamentos.objects.filter(
            Q(id_depart__icontains = busqueda) |
            Q(dep_nombre__icontains = busqueda)
        ).distinct()
    if request.method == 'POST':
        form = DepartamentosForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,f"Se agregó el departamento {request.POST['dep_nombre']} exitosamente"
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
    return render(request, 'usuarios/interfaz_departamentos.html', context)


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
    return render(request, 'usuarios/interfaz_departamentos.html', context)


def eliminar_departamento(request, pk):
    Departamentos.objects.filter(id=pk).update(
        dep_estado='0'
    )
    messages.success(
        request,f"El departamento se eliminó exitosamente"
    )
    return redirect('departamentos')

def vehiculos(request):
    titulo = "Vehículos"
    vehiculos = Vehiculo.objects.filter(veh_estado = '1')
    busqueda = request.GET.get("buscar")
    if busqueda:
        vehiculos = Vehiculo.objects.filter(
            Q(id_matricula__icontains = busqueda)
        ).distinct()
    context = {
        'titulo': titulo,
        'vehiculos': vehiculos
    }
    return render(request, 'usuarios/vehiculos_registrados.html', context)

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
    return render(request, 'usuarios/frm_registrar_nuevo_vehiculo.html', context)

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
    return render(request, 'usuarios/frm_registrar_nuevo_vehiculo.html', context)


def eliminar_vehiculo(request, pk):
    Vehiculo.objects.filter(id=pk).update(
        veh_estado='0'
    )
    messages.success(
        request,f"El vehículo se eliminó exitosamente"
    )
    return redirect('vehiculos')

def vehiculos_taller(request):
    titulo = "Vehículos en taller"
    vehiculos = Vehiculo.objects.filter(veh_taller = 'Si', veh_estado = '1')
    busqueda = request.GET.get('veh_busqueda')
    if busqueda:
        vehiculos = Vehiculo.objects.filter(
            Q(id_matricula__icontains = busqueda)
        ).distinct()
    context = {
        'titulo': titulo,
        'vehiculos': vehiculos
    }
    return render(request, 'usuarios/interfaz_vehiculos_en_taller.html', context)

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
    return render(request, 'usuarios/frm_registrar_nuevo_vehiculo.html', context)

def sacar_vehiculo_taller(request, pk):
    Vehiculo.objects.filter(id=pk).update(
        veh_taller='No'
    )
    messages.success(
        request,f"El vehículo ha salido del taller"
    )
    return redirect('vehiculos_taller')

def ingresar_vehiculo_taller(request, pk):
    Vehiculo.objects.filter(id=pk).update(
        veh_taller='Si'
    )
    messages.success(
        request,f"El vehículo se ha ingresado al taller"
    )
    return redirect('vehiculos_taller')


def empleado(request):
    titulo = "Empleados"
    empleado = Empleados.objects.filter(emp_estado='1')
    busqueda = request.GET.get('emp_busqueda')
    if busqueda:
        empleado = Empleados.objects.filter(
            Q(id_emp_identificacion__icontains = busqueda) |
            Q(emp_nombre__icontains = busqueda) |
            Q(emp_apellidos__icontains = busqueda)
        ).distinct()
    context = {
        'titulo': titulo,
        'empleado': empleado
    }
    return render(request, 'usuarios/interfaz_empleado_usuarios.html', context)

@login_required(login_url='login')
def registrar_empleado(request):
    titulo = "Registrar nuevo empleado"
    if request.method == "POST":
        form = EmpleadosForm(request.POST, request.FILES)
        if form.is_valid():
            if not User.objects.filter(username=request.POST['id_emp_identificacion']): # si este filtro esta vacio significa que el usuario no se ha creado
                user = User.objects.create_user('nombre', 'email@email', 'pass')
                user.username = request.POST['id_emp_identificacion']
                user.first_name = request.POST['emp_nombre']
                user.last_name = request.POST['emp_apellidos']
                user.email = request.POST['emp_email']
                user.password = "@" + request.POST['id_emp_identificacion']
                user.save()
                user_group = User
                my_group = Group.objects.get(name='User_Normal')
                usuario.user.groups.clear() # para cuando se borre el grupo de usuarios, se borre el viejo y quede el nuevo grupo
                my_group.user_set.add(usuario.user)
            else:
                user = User.objects.get(username=request.POST['id_emp_identificacion'])
            
            usuario = Empleados.objects.create(
                tbl_sucursal_idsucursal = Sucursales.objects.get(id=int(request.POST['tbl_sucursal_idsucursal'])),
                id_emp_identificacion = request.POST['id_emp_identificacion'],
                emp_tipo_documento = request.POST['emp_tipo_documento'],
                tbl_ciudad_idciudad = Ciudades.objects.get(id=int(request.POST['tbl_ciudad_idciudad'])),
                emp_nombre = request.POST['emp_nombre'],
                emp_apellidos = request.POST['emp_apellidos'],
                emp_genero = request.POST['emp_genero'],
                emp_direccion = request.POST['emp_direccion'],
                emp_telefono = request.POST['emp_telefono'],
                emp_celular = request.POST['emp_celular'],
                emp_email = request.POST['emp_email'],
                emp_fecha_nacimiento = request.POST['emp_fecha_nacimiento'],
                emp_cargo = request.POST['emp_cargo'],
                emp_num_contrato = request.POST['emp_num_contrato'],
                emp_fecha_ingreso = request.POST['emp_fecha_ingreso'],
                emp_foto = form.cleaned_data.get('emp_foto'),
                user = user,
            )
            return redirect('empleados')

        else:
            form = EmpleadosForm(request.POST, request.FILES)
    else:
        form = EmpleadosForm()

    context = {
        'titulo': titulo,
        'form': form
    }
    return render(request, 'usuarios/frm_registrar_empleados.html', context)

def editar_empleado(request, pk):
    titulo = "Editar empleado"
    empleado = Empleados.objects.get(id=pk)
    if request.method == "POST":
        form = EmpleadosForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            messages.success(
                request,f"Se editó el empleado {request.POST['emp_nombre']} exitosamente"
            )
            return redirect('empleados')
        else:
            print('Error al guardar')
    else:
        form = EmpleadosForm(instance=empleado)

    context = {
        'titulo': titulo,
        'form': form
    }
    return render(request, 'usuarios/frm_registrar_empleados.html', context)

def eliminar_empleado(request, pk):
    Empleados.objects.filter(id=pk).update(
        emp_estado='0'
    )
    messages.success(
        request,f"El empleado se eliminó exitosamente"
    )
    return redirect('empleados')

def ordenes_servicio(request, modal_status='hid'):
    titulo = "Registrar órdenes de venta"
    ordenes = OrdenServicio.objects.filter(ser_estado='1', ord_s_estado_pago='Sin pagar')

    ### cuerpo del modal ###
    modal_title = ""
    modal_txt = ""
    modal_submit = ""
    #######################

    pk_orden = ""
    tipo = None
    form_update = None
    form = OrdenServicioForm()

    if request.method == "POST" and 'form-crear' in request.POST:
        form = OrdenServicioForm(request.POST)
        if form.is_valid():
            aux = form.save(commit=False)
            aux.tbl_empleados_idempleado = Empleados.objects.get(user_id=request.user.id)
            aux.save()
            messages.success(
                request, f"La Órden de servicio {aux.id} ha sido abierta"
            )
            return redirect('detalle_orden_servicio', aux.id)
        else:
            form = OrdenServicioForm(request.POST)
            messages.error(
                request, f"Error al abrir lar Órden de servicio"
            )
###################### configuracion modal de eliminacion ########################
    if  request.method == "POST" and 'form-eliminar' in request.POST:
        modal_status = 'show'
        pk_orden = request.POST['pk']
        orden = OrdenServicio.objects.get(id=pk_orden)

        ### Cuerpo del modal ###
        modal_title = f"Eliminar {orden}"
        modal_txt = f"Eliminar la orden{orden}"
        modal_submit = "Eliminar"
        ########################

        tipo = "eliminar"

#################### Configuracon modal de edicion ##############################
    if request.method == "POST" and 'form-editar' in request.POST:
        modal_status = 'show'
        pk_orden = request.POST['pk']
        orden = OrdenServicio.objects.get(id=pk_orden)

        ### Cuerpo del modal ###
        modal_title = f"Editar {orden}"
        modal_submit = "Editar"
        ########################

        tipo = "editar"
        form_update = OrdenServicioUpdateForm(instance=orden)

################### Configuración de eliminación ###############################
    if request.method == 'POST' and 'modal-confirmar' in request.POST:
        if request.POST['tipo'] == 'eliminar':
            orden = OrdenServicio.objects.filter(id = int(request.POST['modal-pk'])).update(
                ser_estado = '0'
            )
            messages.success(
                request,f"Se eliminó la órden {orden.id} exitosamente!"
            )
            return redirect('ordenes_servicio')

        if request.POST['tipo'] == 'editar':
            pk_orden = request.POST['modal-pk']
            orden = OrdenServicio.objects.get(id=pk_orden)
            form_update = OrdenServicioUpdateForm(request.POST, instance=orden)

            if form_update.is_valid():
                form_update.save()
                messages.success(
                    request,f"Se editó la órden {orden.id} exitosamente!"
                )
                return redirect('ordenes_servicio')
    context = {
        'titulo':titulo,
        'ordenes':ordenes,
        'form':form,
        'modal_status':modal_status,
        'modal_submit':modal_submit,
        'modal_title':modal_title,
        'modal_text':modal_txt,
        'pk':pk_orden,
        'tipo':tipo,
        'form_update':form_update,
    }
    return render(request, 'usuarios/frm_crear_orden_servicio.html', context)

def tbl_rel_orden_ser_articulos(request, pk):
    titulo = f"Detalle de la orden de venta {pk}"
    rel = TblRelOrdenServicioArticulos.objects.filter(tbl_orden_servicio_idorden_servicio_id=pk)
    print(rel)
    if request.method == "POST":
        form = TblRelOrdenServicioArticulosForm(request.POST)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.tbl_orden_servicio_idorden_servicio_id = pk
            temp.save()
            messages.success(
                request, f"Se agregó el artículo con codígo {request.POST['Ttbl_articulos_idarticulo']} existosamente"
            )
            return redirect('detalle_orden_servicio', pk)
        else:
            print('Error')
    else:
        form = TblRelOrdenServicioArticulosForm()
    context = {
        'titulo':titulo,
        'form':form,
        'rel':rel,
    }
    return render(request, 'usuarios/rel_orden_servicio_articulos.html', context)

def eliminar_orden_ser(request, pk):
    OrdenServicio.objects.filter(id=pk).update(
        ser_estado='0'
    )
    messages.success(
        request,f"La órden se eliminó exitosamente"
    )
    return redirect('ordenes_servicio')

def cerrar_orden_servicio(request, pk):
    OrdenServicio.objects.filter(id=pk).update(
        ord_s_estado_pago='Pagado'
    )
    messages.success(
        request,f"La órden se ha cerrado exitosamente"
    )
    return redirect('ordenes_servicio')

def quitar_art_rel_ord_art(request, pk):
    TblRelOrdenServicioArticulos.objects.filter(id=pk).delete()
    messages.success(
        request,f"Se ha quitado el artículo"
    )
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

class ImprimirOrdenServicio(View):
    def link_callback(self, uri, rel):
            """
            Convert HTML URIs to absolute system paths so xhtml2pdf can access those
            resources
            """
            result = finders.find(uri)
            if result:
                    if not isinstance(result, (list, tuple)):
                            result = [result]
                    result = list(os.path.realpath(path) for path in result)
                    path=result[0]
            else:
                    sUrl = settings.STATIC_URL        # Typically /static/
                    sRoot = settings.STATIC_ROOT      # Typically /home/userX/project_static/
                    mUrl = settings.MEDIA_URL         # Typically /media/
                    mRoot = settings.MEDIA_ROOT       # Typically /home/userX/project_static/media/

                    if uri.startswith(mUrl):
                            path = os.path.join(mRoot, uri.replace(mUrl, ""))
                    elif uri.startswith(sUrl):
                            path = os.path.join(sRoot, uri.replace(sUrl, ""))
                    else:
                            return uri

            # make sure that file exists
            if not os.path.isfile(path):
                    raise Exception(
                            'media URI must start with %s or %s' % (sUrl, mUrl)
                    )
            return path

    def get(self, request, *args, **kwargs):
        try:
            template = get_template('usuarios/imprimir_orden_servicio.html')
            context = {
                'orden_servicio': OrdenServicio.objects.get(pk=self.kwargs['pk']),
                'icon': 'static/img/logo_racing.png',
                'articulos_orden': TblRelOrdenServicioArticulos.objects.filter(tbl_orden_servicio_idorden_servicio=self.kwargs['pk']),
                'empresa': Empresa.objects.get(empr_estado=1),
                'sucursal': 'Bogotá, Colombia',
            }
            html = template.render(context)
            response = HttpResponse(content_type='application/pdf')
            #response['Content-Disposition'] = 'attachment; filename="factura.pdf"'
            pisa_status = pisa.CreatePDF(
            html, dest=response,
            link_callback=self.link_callback
            )
            return response
        except:
            pass
        return HttpResponseRedirect(reverse_lazy('ordenes_servicio'))

def historial_ord_servicio(request):
    titulo = "Historial ordenes de servicio"
    ordenes_servicio_h = OrdenServicio.objects.filter(ser_estado='1', ord_s_estado_pago='Pagado')
    busqueda = request.GET.get("ord_s_busqueda")
    if busqueda:
        ordenes_servicio_h = OrdenServicio.objects.filter(
            Q(ord_s_identificacion_cli = busqueda) |
            Q(ord_s_vehiculo = busqueda)
        ).distinct()
    context = {
        'titulo':titulo,
        'ordenes_servicio_h':ordenes_servicio_h,
    }
    return render(request, 'usuarios/interfaz_historial_ord_servicio.html', context)

def tbl_rel_orden_ser_art_hist(request, pk):
    titulo = f"Detalle de la orden de servicio {pk}"
    rel = TblRelOrdenServicioArticulos.objects.filter(tbl_orden_servicio_idorden_servicio_id=pk)
    print(rel)
    context = {
        'titulo':titulo,
        'rel':rel,
    }
    return render(request, 'usuarios/interfaz_detall_hist_ord_ser.html', context)