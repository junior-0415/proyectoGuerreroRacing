from django.urls import path

from facturacion.views import facturar_venta, detalle_fac_venta

urlpatterns = [
    path('facturar-venta/', facturar_venta, name='facturar_venta'),
    path('facturar-venta/detalles/<int:pk>/', detalle_fac_venta, name='detalle_fac_venta'),
]