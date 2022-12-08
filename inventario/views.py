from django.shortcuts import render, redirect
from django.contrib import messages
from inventario.forms import OrdenCompraForm, PedidosComprasForm, TblRelOrdenCompraArticulosForm, TblRelPedidosArticulosForm
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import View
import os
from django.conf import settings
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.urls import reverse_lazy
from django.contrib.staticfiles import finders

from inventario.models import OrdenCompra, Pedidos, TblRelOrdenCompraArticulos, TblRelPedidosArticulos
from usuarios.models import Empleados, Empresa

# Create your views here.

def ordenes_compra(request):
    titulo = "Crear órden de compra"
    ordenes_compra = OrdenCompra.objects.filter(ord_estado = '1')
    if request.method == "POST":
        form = OrdenCompraForm(request.POST)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.ord_empleado =  Empleados.objects.get(user_id=request.user.id)
            temp.save()
            messages.success(
                request, f"La Órden de servicio {temp.id} ha sido abierta"
            )
            return redirect('detalle_orden_compra', temp.id)
        else:
            print('Error')
    else:
        form = OrdenCompraForm()

    context = {
        'titulo': titulo,
        'form': form,
        'ordenes_compra':ordenes_compra,
    }
    return render(request, 'inventario/frm_orden_de_compra.html', context)

def tbl_rel_orden_com_articulos(request, pk):
    titulo = f"Detalle de la orden de compra {pk}"
    rel = TblRelOrdenCompraArticulos.objects.filter(tbl_orden_compras_idorden_compra_id=pk)
    print(rel)
    if request.method == "POST":
        form = TblRelOrdenCompraArticulosForm(request.POST)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.tbl_orden_compras_idorden_compra_id = pk
            temp.save()
            messages.success(
                request, f"Se agregó el artículo con codígo {request.POST['tbl_articulos_idarticulo']} existosamente"
            )
            return redirect('detalle_orden_compra', pk)
        else:
            print('Error')
    else:
        form = TblRelOrdenCompraArticulosForm()
    context = {
        'titulo':titulo,
        'form':form,
        'rel':rel,
    }
    return render(request, 'inventario/rel_orden_compra_articulos.html', context)

def historial_compras(request):
     titulo = "Historial de compras"
     pedidos = Pedidos.objects.filter(ped_estado = '2')
     context = {
        'titulo':titulo,
        'pedidos':pedidos
     }
     return render(request, 'inventario/interfaz_historial_compras.html', context)

def historial_ord_compra(request):
     titulo = "Historial órdenes de compras"
     orden_compra = OrdenCompra.objects.filter(ord_estado = '2')
     context = {
        'titulo':titulo,
        'orden_compra':orden_compra
     }
     return render(request, 'inventario/interfaz_historial_ord_compras.html', context)

def eliminar_orden_compra(request, pk):
    OrdenCompra.objects.filter(id=pk).update(
        ord_estado='0'
    )
    messages.success(
        request,f"La órden de compra se eliminó exitosamente"
    )
    return redirect('historial_ord_compra')


def reporte_semanal(request):
    titulo = "Reporte semanal"

    labels_compras = ['Enero']
    data_compras = [15]


    context = {
        'titulo':titulo,
        'labels_compras':labels_compras,
        'data_compras':data_compras,
    }
    return render(request, 'inventario/interfaz_reporte_semanal.html', context)

def registrar_pedidos_compras(request, modal_status='hid'):
    titulo = "Registrar compra o pedido"
    pedidos = Pedidos.objects.filter(ped_estado='1')

    ### cuerpo del modal ###
    modal_title = ""
    modal_txt = ""
    modal_submit = ""
    #######################

    pk_pedido = ""
    tipo = None
    form_update = None
    form = PedidosComprasForm()

    if request.method == "POST" and 'form-crear' in request.POST:
        form = PedidosComprasForm(request.POST)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.save()
            messages.success(
                request, f"La compra o pedido número {temp.id} ha sido abierto"
            )
            return redirect('detalle_compra_pedidos', temp.id)
        else:
            form = PedidosComprasForm(request.POST)
            messages.error(
                request, f"Error al abrir la compra o pedido"
            )
###################### configuracion modal de eliminacion ########################
    if  request.method == "POST" and 'form-eliminar' in request.POST:
        modal_status = 'show'
        pk_pedido = request.POST['pk']
        pedido = Pedidos.objects.get(id=pk_pedido)

        ### Cuerpo del modal ###
        modal_title = f"Eliminar {pedido}"
        modal_txt = f"Eliminar la el pedido {pedido}"
        modal_submit = "Eliminar"
        ########################

        tipo = "eliminar"

#################### Configuracon modal de edicion ##############################
    if request.method == "POST" and 'form-editar' in request.POST:
        modal_status = 'show'
        pk_pedido = request.POST['pk']
        pedido = Pedidos.objects.get(id=pk_pedido)

        ### Cuerpo del modal ###
        modal_title = f"Editar {pedido}"
        modal_submit = "Editar"
        ########################

        tipo = "editar"
        form_update = PedidosUpdateForm(instance=pedido)

################### Configuración de eliminación ###############################
    if request.method == 'POST' and 'modal-confirmar' in request.POST:
        if request.POST['tipo'] == 'eliminar':
            pedido = Pedidos.objects.filter(id = int(request.POST['modal-pk'])).update(
                ped_estado = '0'
            )
            messages.success(
                request,f"Se eliminó la compra o pedido {pedido.id} exitosamente!"
            )
            return redirect('registrar_pedido_compra')

        if request.POST['tipo'] == 'editar':
            pk_pedido = request.POST['modal-pk']
            pedido = Pedidos.objects.get(id=pk_pedido)
            form_update = PedidosUpdateForm(request.POST, instance=pedido)

            if form_update.is_valid():
                form_update.save()
                messages.success(
                    request,f"Se editó la compra o pedido {pedido.id} exitosamente!"
                )
                return redirect('registrar_pedido_compra')
    context = {
        'titulo':titulo,
        'pedidos':pedidos,
        'form':form,
        'modal_status':modal_status,
        'modal_submit':modal_submit,
        'modal_title':modal_title,
        'modal_text':modal_txt,
        'pk':pk_pedido,
        'tipo':tipo,
        'form_update':form_update,
    }
    return render(request, 'inventario/frm_pedidos_compras.html', context)

def tbl_rel_pedido_articulos(request, pk):
    titulo = f"Detalle del pedido {pk}"
    rel = TblRelPedidosArticulos.objects.filter(tbl_pedidos_idpedido_id=pk)
    print(rel)
    if request.method == "POST":
        form = TblRelPedidosArticulosForm(request.POST)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.tbl_pedidos_idpedido_id = pk
            temp.save()
            messages.success(
                request, f"Se agregó el artículo con codígo {request.POST['tbl_articulos_idarticulo']} existosamente"
            )
            return redirect('detalle_compra_pedidos', pk)
        else:
            print('Error')
    else:
        form = TblRelPedidosArticulosForm()
    context = {
        'titulo':titulo,
        'form':form,
        'rel':rel,
    }
    return render(request, 'inventario/rel_pedidos_articulos.html', context)

def quitar_art_det_ord_compra(request, pk):
    TblRelOrdenCompraArticulos.objects.filter(id=pk).delete()
    messages.success(
        request,f"Se ha quitado el artículo"
    )
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
    
def cerrar_orden_compra(request, pk):
    OrdenCompra.objects.filter(id=pk).update(
        ord_estado='2'
    )
    messages.success(
        request,f"La órden de compra se ha cerrado exitosamente"
    )
    return redirect('ordenes_compra')

def historial_delt_ord_compra(request, pk):
    titulo = f"Detalle de la orden de compra {pk}"
    rel = TblRelOrdenCompraArticulos.objects.filter(tbl_orden_compras_idorden_compra_id=pk)
    print(rel)
    context = {
        'titulo':titulo,
        'rel':rel,
    }
    return render(request, 'inventario/interfaz_historial_dell_ord_compra.html', context)

class ImprimirOrdenCompra(View):
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
            template = get_template('inventario/imprimir_orden_compra.html')
            context = {
                'orden_compra': OrdenCompra.objects.get(pk=self.kwargs['pk']),
                'icon': 'static/img/logo_racing.png',
                'detalle_orden': TblRelOrdenCompraArticulos.objects.filter(tbl_orden_compras_idorden_compra=self.kwargs['pk']),
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
        return HttpResponseRedirect(reverse_lazy('ordenes_compra'))

def eliminar_compra_pedido(request, pk):
    Pedidos.objects.filter(id=pk).update(
        ped_estado='0'
    )
    messages.success(
        request,f"La compra o pedido se eliminó exitosamente"
    )
    return redirect('historial_compras')

def quitar_art_rel_pedido(request, pk):
    TblRelPedidosArticulos.objects.filter(id=pk).delete()
    messages.success(
        request,f"Se ha quitado el artículo"
    )
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

def cerrar_pedido(request, pk):
    Pedidos.objects.filter(id=pk).update(
        ped_estado='2'
    )
    messages.success(
        request,f"El pedido se ha cerrado exitosamente"
    )
    return redirect('registrar_pedido_compra')

def historial_delt_pedido(request, pk):
    titulo = f"Detalle de la orden de servicio {pk}"
    rel = TblRelPedidosArticulos.objects.filter(tbl_pedidos_idpedido_id=pk)
    print(rel)
    context = {
        'titulo':titulo,
        'rel':rel,
    }
    return render(request, 'inventario/interfaz_historial_dell_pedido.html', context)