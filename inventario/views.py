from django.shortcuts import render, redirect
from django.contrib import messages
from inventario.forms import OrdenCompraForm, PedidosComprasForm

from inventario.models import OrdenCompra, Pedidos

# Create your views here.

def crear_orden_compra(request):
    titulo = "Crear órden de compra"
    if request.method == "POST":
        form = OrdenCompraForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,f"Se creo la órden de compra número{request.POST['pk']} exitosamente"
            )
            return redirect('historial_compras')
        else:
            print('Error')
    else:
        form = OrdenCompraForm()

    context = {
        'titulo': titulo,
        'form': form
    }
    return render(request, 'inventario/frm_orden_de_compra.html', context)

def registrar_pedidos_compras(request):
    titulo = "Registrar pedido o compra"
    if request.method == "POST":
        form = PedidosComprasForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,f"Se registro el pedido número{request.POST['pk']} exitosamente"
            )
            return redirect('historial_compras')
        else:
            print('Error')
    else:
        form = PedidosComprasForm()

    context = {
        'titulo': titulo,
        'form': form
    }
    return render(request, 'inventario/frm_pedidos_compras.html', context)

def historial_compras(request):
     titulo = "Historial de compras"
     pedido = Pedidos.objects.filter(ped_estado = '1')
     context = {
        'titulo':titulo,
        'pedido':pedido
     }
     return render(request, 'inventario/interfaz_historial_compras.html', context)

def historial_ord_compra(request):
     titulo = "Historial órdenes de compras"
     orden_compra = OrdenCompra.objects.filter(ord_estado = '1')
     context = {
        'titulo':titulo,
        'orden_compra':orden_compra
     }
     return render(request, 'inventario/interfaz_historial_ord_compras.html', context)

def reporte_semanal(request):
    titulo = "Reporte semanal"
    context = {
        'titulo':titulo,
    }