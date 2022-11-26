from contextlib import redirect_stderr
from multiprocessing import context
from xml.dom.minidom import Document
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from articulos.models import Articulos
from usuarios.forms import CiudadesForm, ClienteForm, DepartamentosForm, EmpleadosForm, EmpresaForm, OrdenServicioForm, ServiciosForm, SucursalesForm, TblRelOrdenServicioArticulosForm, VehiculosForm
from django.contrib.auth.models import User

from usuarios.models import Ciudades, Cliente, Departamentos, Empleados, Empresa, OrdenServicio, Servicios, Sucursales, TblRelOrdenServicioArticulos, Vehiculo

# Create your views here.

@login_required(login_url='login')
def empresa(request):
    titulo = "Tu empresa"
    empresa = Empresa.objects.filter(empr_estado = '1')
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
        'titulo': titulo,
        'empresa': empresa,
        'form': form
    }
    return render(request, 'usuarios/empresa.html', context)

def sucursales(request):
    titulo = "Sucursales"
    sucursal = Sucursales.objects.filter(suc_estado = '1')
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
        'sucursal': sucursal,
        'form': form
    }
    return render(request, 'usuarios/sucursales.html', context)

def servicios(request):
    titulo = "Servicios"
    servicios = Servicios.objects.filter(ser_estado = '1')
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
        request,f"El servicio se envió a papelera exitosamente"
    )
    return redirect('servicios')

def clientes(request):
    titulo = "Clientes"
    clientes = Cliente.objects.filter(cli_estado = '1')
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
        request,f"El cliente se envió a papelera exitosamente"
    )
    return redirect('clientes')

@login_required(login_url='login')
@permission_required('usuarios.view_ciudades')
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
        request,f"La ciudad o municipio se envió a papelera exitosamente"
    )
    return redirect('ciudades')


def departamentos(request):
    titulo = "Departamentos"
    departamentos = Departamentos.objects.filter(dep_estado = '1')
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
        request,f"El departamento se envió a papelera exitosamente"
    )
    return redirect('departamentos')

def vehiculos(request):
    titulo = "Vehículos"
    vehiculos = Vehiculo.objects.filter(veh_estado = '1')
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
        request,f"El vehículo se envió a papelera exitosamente"
    )
    return redirect('vehiculos')

def vehiculos_taller(request):
    titulo = "Vehículos en taller"
    vehiculos = Vehiculo.objects.filter(veh_taller = 'Si', veh_estado = '1')
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
        request,f"El empleado se envió a papelera exitosamente"
    )
    return redirect('empleados')

def ordenes_servicio(request):
    titulo = "Órdenes de servicio"
    ordenes_servicio = OrdenServicio.objects.filter(ser_estado='1')
    rel_articulos = TblRelOrdenServicioArticulos.objects.filter(tbl_estado='1')

    context = {
        'titulo': titulo,
        'ordenes_servicio': ordenes_servicio,
        'rel_articulos':rel_articulos
    }
    return render(request, 'usuarios/interfaz_ordenes_servicio.html', context)

def crear_orden_servicio(request):
    titulo = "Crear órden servicio"
    if request.method == "POST":
        form = OrdenServicioForm(request.POST)
        if form.is_valid():
            form.save()
            llave_primaria_form = ""
            # messages.success(
            #     request,f"Se ha registrado la orden número {request.POST['pk']} exitosamente"
            # )
            #return redirect('ordenes_servicio')
        else:
            print('Error')
        
    else:
        form = OrdenServicioForm()

    context = {
        'titulo': titulo,
        'form': form,
    }
    return render(request, 'usuarios/frm_crear_orden_servicio.html', context)

def tbl_rel_orden_ser_articulos(request, llave_primaria_form):
    if request.method == "POST":
        form2 = TblRelOrdenServicioArticulosForm(request.POST)
        if form2.is_valid():
            tbl_rel = TblRelOrdenServicioArticulos.objects.create(
                tbl_orden_servicio_idorden_servicio = llave_primaria_form,
                Ttbl_articulos_idarticulo = Articulos.objects.get(id=int(request.POST['Ttbl_articulos_idarticulo'])),
                art_cantidad = request.POST['art_cantidad'],
                art_precio = request.POST['art_precio'],   
            )
            return redirect('ordenes_servicio')
        else:
            print('Error')
    else:
        form2 = TblRelOrdenServicioArticulosForm()