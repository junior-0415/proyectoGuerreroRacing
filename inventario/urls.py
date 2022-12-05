from django.urls import path

from inventario.views import crear_orden_compra, historial_compras, historial_ord_compra, registrar_pedidos_compras

urlpatterns = [
    path('compras/crear-orden-de-compra/', crear_orden_compra, name='crear_orden_compra'),
    path('compras/registrar-compra-pedido/',registrar_pedidos_compras, name='registrar_pedido_compra'),
    path('compras/historial/', historial_compras, name='historial_compras'),
    path('compras/historial-ordenes-de-compra/', historial_ord_compra, name='historial_ord_compra'),
]