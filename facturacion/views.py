from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import View
import os
from django.conf import settings
from django.template import Context
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.urls import reverse_lazy
from django.contrib.staticfiles import finders
from django.db.models import Q

from facturacion.forms import DetalleFacturaVentaForm, FacturaVentaForm
from facturacion.models import DetalleFacturaVenta, FacturaVenta
from usuarios.models import Empleados, Empresa, Sucursales
from django.contrib import messages

# Create your views here.

def facturar_venta(request, modal_status='hid'):
    titulo = "Registrar y facturar venta"
    facturas = FacturaVenta.objects.filter(fac_estado='1')
    #detalle_factura = DetalleFacturaVenta.objects.get().all

    #print(detalle_factura)

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
                request, f"Error al abrir la factura"
            )
###################### configuracion modal de eliminacion ########################
    if  request.method == "POST" and 'form-eliminar' in request.POST:
        modal_status = 'show'
        pk_factura = request.POST['pk']
        factura = FacturaVenta.objects.get(id=pk_factura)

        ### Cuerpo del modal ###
        modal_title = f"Eliminar {factura}"
        modal_txt = f"Eliminar la factura{factura}"
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
            messages.success(
                request,f"Se eliminó la factura {factura.fac_numero_serie} exitosamente!"
            )
            return redirect('facturar_venta')

        if request.POST['tipo'] == 'editar':
            pk_factura = request.POST['modal-pk']
            factura = FacturaVenta.objects.get(id=pk_factura)
            form_update = FacturaVentaUpdateForm(request.POST, instance=factura)

            if form_update.is_valid():
                form_update.save()
                messages.success(
                    request,f"Se editó la factura {factura.fac_numero_serie} exitosamente!"
                )
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
        #'detalle_factura':detalle_factura,
    }
    return render(request, 'facturacion/frm_registrar_ventas.html', context)

def detalle_fac_venta(request, pk):
    titulo = f"Detalle de la factura de venta {pk}"
    detalles = DetalleFacturaVenta.objects.filter(tbl_facturas_idfactura_id=pk)
    print(detalles)
    if request.method == "POST":
        form = DetalleFacturaVentaForm(request.POST)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.tbl_facturas_idfactura_id = pk
            temp.save()
            messages.success(
                request, f"Se agregó el artículo con codígo {request.POST['tbl_articulos_idarticulo']} existosamente"
            )
            return redirect('detalle_fac_venta', pk)
        else:
            print('Error')
    else:
        form = DetalleFacturaVentaForm()
    context = {
        'titulo':titulo,
        'form':form,
        'detalles':detalles,
    }
    return render(request, 'facturacion/detalle_factura_venta.html', context)

def eliminar_art_detalle_fac(request, pk):
    DetalleFacturaVenta.objects.filter(id=pk).delete()
    messages.success(
        request,f"Se ha quitado el artículo"
    )
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

class ImprimirFacturaVenta(View,):
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
            template = get_template('facturacion/imprimir_factura.html')
            context = {
                'venta': FacturaVenta.objects.get(pk=self.kwargs['pk']),
                'icon': 'static/img/logo_racing.png',
                'detalle_venta': DetalleFacturaVenta.objects.filter(tbl_facturas_idfactura=self.kwargs['pk']),
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
        return HttpResponseRedirect(reverse_lazy('facturar_venta'))

def cerrar_factura(request, pk):
    FacturaVenta.objects.filter(fac_numero_serie=pk).update(
        fac_estado='2'
    )
    messages.success(
        request,f"La factura se ha cerrado exitosamente"
    )
    return redirect('ordenes_servicio')

def historial_ventas(request):
    titulo = "Historial ventas"
    historial_ventas_ = FacturaVenta.objects.filter(fac_estado='2')
    busqueda = request.GET.get('venta_busqueda')
    if busqueda:
        historial_ventas_ = FacturaVenta.objects.filter(
            Q(fac_numero_serie__icontains = busqueda)
        ).distinct()
    context = {
        'titulo':titulo,
        'historial_ventas_':historial_ventas_,
    }
    return render(request, 'facturacion/interfaz_historial_ventas.html', context)

def tbl_rel_factura_art_hist(request, pk):
    titulo = f"Detalle de la factura {pk}"
    rel = DetalleFacturaVenta.objects.filter(tbl_facturas_idfactura_id=pk)
    print(rel)
    context = {
        'titulo':titulo,
        'rel':rel,
    }
    return render(request, 'facturacion/interfaz_historial_dell_factura.html', context)

def eliminar_factura_venta(request, pk):
    FacturaVenta.objects.filter(fac_numero_serie=pk).update(
        fac_estado='0'
    )
    messages.success(
        request,f"La factura se eliminó exitosamente"
    )
    return redirect('historial_ventas')
