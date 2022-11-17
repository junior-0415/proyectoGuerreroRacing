from django.shortcuts import render, redirect

from facturacion.forms import DetalleFacturaForm, FacturaVentaForm
from facturacion.models import FacturaVenta
from usuarios.models import Empleados
from django.contrib import messages

# Create your views here.

def facturar_venta(request, modal_status='hid'):
    titulo = "Registrar y facturar venta"
    facturas = FacturaVenta.objects.filter(fac_estado='1')

    ### cuerpo del modal ###
    modal_title = ""
    modal_txt = ""
    modal_submit = ""
    #######################

    pk_factura = ""
    tipo = None
    form_update = None
    form = FacturaVentaForm()

    if request.method == "POST" and 'form-crear' in request.POST:
        form = FacturaVentaForm(request.POST)
        if form.is_valid():
            aux = form.save(commit=False)
            aux.tbl_empleados_idempleado = Empleados.objects.get(user_id=request.user.id)
            aux.save()
            messages.success(
                request, f"La factura {aux.fac_numero_serie} ha sido abierta"
            )
            return redirect('detalle_fac_venta', aux.fac_numero_serie)
        else:
            form = FacturaVentaForm(request.POST)
            messages.error(
                request, "Error al abrir la factura"
            )
###################### configuracion modal de eliminacion ########################
    if  request.method == "POST" and 'form-eliminar' in request.POST:
        modal_status = 'show'
        pk_factura = request.POST['pk']
        factura = FacturaVenta.objects.get(id=pk_factura)

        ### Cuerpo del modal ###
        modal_title = f"Eliminar {factura}"
        modal_txt = f"Eliminar de la factura{factura}"
        modal_submit = "Eliminar"
        ########################

        tipo = "eliminar"

#################### Configuracon modal de edicion ##############################
    if request.method == "POST" and 'form-editar' in request.POST:
        modal_status = 'show'
        pk_factura = request.POST['pk']
        factura = FacturaVenta.objects.get(id=pk_factura)

        ### Cuerpo del modal ###
        modal_title = f"Editar {factura}"
        modal_submit = "Editar"
        ########################

        tipo = "editar"
        form_update = FacturaVentaUpdateForm(instance=factura)

################### Configuración de eliminación ###############################
    if request.method == 'POST' and 'modal-confirmar' in request.POST:
        if request.POST['tipo'] == 'eliminar':
            factura = FacturaVenta.objects.filter(id = int(request.POST['modal-pk'])).update(
                fac_estado = '0'
            )
            # mensajes de success o confirmacion de que se elimino
            return redirect('facturar_venta')

        if request.POST['tipo'] == 'editar':
            pk_factura = request.POST['modal-pk']
            factura = FacturaVenta.objects.get(id=pk_factura)
            form_update = FacturaVentaUpdateForm(request.POST, instance=factura)

            if form_update.is_valid():
                form_update.save()
                # Mensaja de edito la factura
                return redirect('facturar_venta')
    context = {
        'titulo':titulo,
        'facturas':facturas,
        'form':form,
        'modal_status':modal_status,
        'modal_submit':modal_submit,
        'modal_title':modal_title,
        'modal_text':modal_txt,
        'pk':pk_factura,
        'tipo':tipo,
        'form_update':form_update,
    }
    return render(request, 'facturacion/frm_registrar_ventas.html', context)

def detalle_fac_venta(request, pk):
    titulo = f"Detalle de la factura de venta {pk}"
    form = DetalleFacturaForm()
    context = {
        'titulo':titulo,
        'form':form,
    }
    return render(request, 'facturacion/detalle_factura_venta.html', context)