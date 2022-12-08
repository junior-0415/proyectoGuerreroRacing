from django.urls import path

from inventario.views import ImprimirOrdenCompra, cerrar_orden_compra, cerrar_pedido, eliminar_compra_pedido, eliminar_orden_compra, historial_compras, historial_delt_ord_compra, historial_ord_compra, ordenes_compra, quitar_art_det_ord_compra, quitar_art_rel_pedido, registrar_pedidos_compras, reporte_semanal, tbl_rel_orden_com_articulos, tbl_rel_pedido_articulos

urlpatterns = [
    path('compras/crear-orden-de-compra/', ordenes_compra, name='ordenes_compra'),
    path('compras/crear-orden-de-compra/articulos/<int:pk>/', tbl_rel_orden_com_articulos, name='detalle_orden_compra'),
    path('compras/crear-orden-de-compra/articulos/eliminar/<int:pk>/', quitar_art_det_ord_compra, name='quitar_art_det_ord_compra'),
    path('compras/crear-orden-de-compra/imprimir/<int:pk>/', ImprimirOrdenCompra.as_view(), name='imprimir_orden_compra'),
    path('compras/crear-orden-de-compra/cerrar/<int:pk>/', cerrar_orden_compra, name='cerrar_orden_compra'),
    path('compras/registrar-compra-pedido/', registrar_pedidos_compras, name='registrar_pedido_compra'),
    path('compras/registrar-compra-pedido/cerrar/<int:pk>/', cerrar_pedido, name='cerrar_pedido'),
    path('compras/historial/eliminar/<int:pk>/', eliminar_compra_pedido, name='eliminar_compra_pedido'),
    path('compras/registrar-compra-pedido/articulos/<int:pk>/', tbl_rel_pedido_articulos, name='detalle_compra_pedidos'),
    path('compras/registrar-compra-pedido/articulos/quitar/<int:pk>/', quitar_art_rel_pedido, name='quitar_art_rel_pedido'),
    path('compras/historial/', historial_compras, name='historial_compras'),
    path('compras/historial-ordenes-de-compra/', historial_ord_compra, name='historial_ord_compra'),
    path('compras/historial-ordenes-de-compra/articulos/<int:pk>/', historial_delt_ord_compra, name='historial_delt_ord_compra'),
    path('compras/historial-ordenes-de-compra/eliminar/<int:pk>/', eliminar_orden_compra, name='eliminar_orden_compra'),
    path('reportes/semanal/', reporte_semanal, name='reporte_semanal')
]