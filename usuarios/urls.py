from django.urls import path

from usuarios.views import ImprimirOrdenServicio, cerrar_orden_servicio, ciudades, clientes, departamentos, editar_ciudad, editar_cliente, editar_departamento, editar_empleado, editar_empresa, editar_servicio, editar_sucursal, editar_vehiculo, editar_vehiculo_taller, eliminar_ciudad, eliminar_cliente, eliminar_departamento, eliminar_empleado, eliminar_orden_ser, eliminar_servicio, eliminar_sucursal, eliminar_vehiculo, empleado, empresa, historial_ord_servicio, ingresar_vehiculo_taller, ordenes_servicio, quitar_art_rel_ord_art, registrar_cliente, registrar_empleado, registrar_empresa, registrar_vehiculo, sacar_vehiculo_taller, servicios, sucursales, tbl_rel_orden_ser_art_hist, tbl_rel_orden_ser_articulos, vehiculos, vehiculos_taller


urlpatterns = [
    path('tu-empresa/', empresa, name='empresa'),
    path('tu-empresa/registrar/', registrar_empresa, name='registrar_empresa'),
    path('tu-empresa/editar/<int:pk>/', editar_empresa, name='editar_empresa'),
    path('sucursales/', sucursales, name='sucursales'),
    path('sucursales/editar/<int:pk>/', editar_sucursal, name='editar_sucursal'),
    path('sucursales/eliminar/<int:pk>/', eliminar_sucursal, name='eliminar_sucursal'),
    path('clientes/', clientes, name='clientes'),
    path('clientes/crear/', registrar_cliente, name='registrar_cliente'),
    path('clientes/editar/<int:pk>/', editar_cliente, name='editar_cliente'),
    path('clientes/eliminar/<int:pk>/', eliminar_cliente, name='eliminar_cliente'),
    path('extras/ciudades-municipios/', ciudades, name='ciudades'),
    path('extras/ciudades-municipios/editar/<int:pk>/', editar_ciudad, name='editar_ciudad'),
    path('extras/ciudades-municipios/eliminar/<int:pk>/', eliminar_ciudad, name='eliminar_ciudad'),
    path('extras/departamentos/', departamentos, name='departamentos'),
    path('extras/departamentos/editar/<int:pk>/', editar_departamento, name='editar_departamento'),
    path('extras/departamentos/eliminar/<int:pk>/', eliminar_departamento, name='eliminar_departamento'),
    path('vehiculos/', vehiculos, name='vehiculos'),
    path('vehiculos/crear/', registrar_vehiculo, name='registrar_vehiculo'),
    path('vehiculos/editar/<int:pk>/', editar_vehiculo, name='editar_vehiculo'),
    path('vehiculos/eliminar/<int:pk>/', eliminar_vehiculo, name='eliminar_vehiculo'),
    path('vehiculos/en-taller/', vehiculos_taller, name='vehiculos_taller'),
    path('vehiculos/en-taller/editar/<int:pk>/', editar_vehiculo_taller, name='editar_vehiculo_taller'),
    path('vehiculos/en-taller/sacar/<int:pk>/', sacar_vehiculo_taller, name='sacar_vehiculo_taller'),
    path('vehiculos/ingresar-al-taller//<int:pk>/', ingresar_vehiculo_taller, name='ingresar_vehiculo_taller'),
    path('empleados/', empleado, name='empleados'),
    path('empleados/crear/', registrar_empleado, name= 'registrar_empleado'),
    path('empleados/editar/<int:pk>/', editar_empleado, name='editar_empleado'),
    path('empleados/eliminar/<int:pk>/', eliminar_empleado, name='eliminar_empleado'),
    path('ordenes-de-servicio/', ordenes_servicio, name='ordenes_servicio'),
    path('ordenes-de-servicio/articulos/<int:pk>/', tbl_rel_orden_ser_articulos, name='detalle_orden_servicio'),
    path('quitar-articulo-orden-compra/<int:pk>/', quitar_art_rel_ord_art, name="quitar_art_rel_ord_art"),
    path('ordenes-de-servicio/cerrar/<int:pk>/', cerrar_orden_servicio, name='cerrar_orden_servicio'),
    path('ordenes-de-servicio/historial/', historial_ord_servicio, name='historial_ord_servicio'),
    path('ordenes-de-servicio/historial/detalles/<int:pk>/', tbl_rel_orden_ser_art_hist, name='tbl_rel_orden_ser_art_hist'),
    path('ordenes-de-servicio/historial/eliminar/<int:pk>/', eliminar_orden_ser, name='eliminar_orden_ser'),
    path('ordenes-de-servicio/imprimir/<int:pk>/', ImprimirOrdenServicio.as_view(), name='imprimir_factura_venta'),
    path('servicios/', servicios, name='servicios'),
    path('servicios/editar/<int:pk>/', editar_servicio, name='editar_servicio'),
    path('servicios/eliminar/<int:pk>/', eliminar_servicio, name='eliminar_servicio'),
]