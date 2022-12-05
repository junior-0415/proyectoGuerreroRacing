from django.urls import path

from facturacion.views import eliminar_art_detalle_fac, facturar_venta, detalle_fac_venta

urlpatterns = [
    path('facturar-venta/', facturar_venta, name='facturar_venta'),
    path('facturar-venta/detalles/<int:pk>/', detalle_fac_venta, name='detalle_fac_venta'),
    path('quitar-articulo-factura/<int:pk>/', eliminar_art_detalle_fac, name="quitar_art_dell_fac"),
]