from django.urls import path
from clientes.views import ciudades, clientes, departamentos, editar_ciudad, editar_cliente, editar_departamento, eliminar_ciudad, eliminar_cliente, eliminar_departamento, registrar_cliente

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
]