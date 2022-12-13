from django.urls import path

from facturacion.views import ImprimirFacturaVenta, cerrar_factura, eliminar_art_detalle_fac, eliminar_factura_venta, facturar_venta, detalle_fac_venta, historial_ventas, tbl_rel_factura_art_hist

urlpatterns = [
    path('facturar-venta/', facturar_venta, name='facturar_venta'),
    path('facturar-venta/detalles/<int:pk>/', detalle_fac_venta, name='detalle_fac_venta'),
    path('quitar-articulo-factura/<int:pk>/<int:tbl_facturas_idfactura>/', eliminar_art_detalle_fac, name="quitar_art_dell_fac"),
    path('facturar-venta/imprimir-factura/<int:pk>/', ImprimirFacturaVenta.as_view(), name='imprimir_factura_venta'),
    path('facturar-venta/cerrar/<int:pk>/', cerrar_factura, name='cerrar_factura'),
    path('facturar-venta/historial-ventas/', historial_ventas, name='historial_ventas'),
    path('facturar-venta/historial-ventas/detalles/<int:pk>/', tbl_rel_factura_art_hist, name='historial_detalle_factura'),
    path('facturar-venta/historial-ventas/eliminar/<int:pk>/', eliminar_factura_venta, name='eliminar_factura_venta')
]