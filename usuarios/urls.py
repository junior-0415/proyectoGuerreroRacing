from django.urls import path

from usuarios.views import ciudades, clientes, departamentos, editar_ciudad, editar_cliente, editar_departamento, editar_vehiculo, editar_vehiculo_taller, eliminar_ciudad, eliminar_cliente, eliminar_departamento, eliminar_vehiculo, ingresar_vehiculo_taller, registrar_cliente, registrar_vehiculo, sacar_vehiculo_taller, vehiculos, vehiculos_taller


urlpatterns = [
    path('clientes/', clientes, name="clientes"),
    path('clientes/crear/', registrar_cliente, name="registrar_cliente"),
    path('clientes/editar/<int:pk>/', editar_cliente, name="editar_cliente"),
    path('clientes/eliminar/<int:pk>/', eliminar_cliente, name="eliminar_cliente"),
    path('extras/ciudades-municipios/', ciudades, name="ciudades"),
    path('extras/ciudades-municipios/editar/<int:pk>/', editar_ciudad, name="editar_ciudad"),
    path('extras/ciudades-municipios/eliminar/<int:pk>/', eliminar_ciudad, name="eliminar_ciudad"),
    path('extras/departamentos/', departamentos, name="departamentos"),
    path('extras/departamentos/editar/<int:pk>/', editar_departamento, name="editar_departamento"),
    path('extras/departamentos/eliminar/<int:pk>/', eliminar_departamento, name="eliminar_departamento"),
    path('vehiculos/', vehiculos, name="vehiculos"),
    path('vehiculos/crear/', registrar_vehiculo, name="registrar_vehiculo"),
    path('vehiculos/editar/<int:pk>/', editar_vehiculo, name="editar_vehiculo"),
    path('vehiculos/eliminar/<int:pk>/', eliminar_vehiculo, name="eliminar_vehiculo"),
    path('vehiculos/en-taller/', vehiculos_taller, name="vehiculos_taller"),
    path('vehiculos/en-taller/editar/<int:pk>/', editar_vehiculo_taller, name="editar_vehiculo_taller"),
    path('vehiculos/en-taller/sacar/<int:pk>/', sacar_vehiculo_taller, name="sacar_vehiculo_taller"),
    path('vehiculos/ingresar-al-taller//<int:pk>/', ingresar_vehiculo_taller, name="ingresar_vehiculo_taller"),
]