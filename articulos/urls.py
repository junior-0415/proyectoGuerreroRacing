from tokenize import Name
from django.urls import path

from articulos.views import articulos, categorias, editar_articulo, editar_categoria, editar_marca, editar_proveedor, eliminar_articulo, eliminar_categoria, eliminar_marca, eliminar_proveedor, marcas, proveedores, registrar_articulo, registrar_proveedor

urlpatterns = [
    path('articulos/', articulos, name="articulos"),
    path('articulos/crear/', registrar_articulo, name="registrar_articulo"),
    path('articulos/editar/<int:pk>/', editar_articulo, name="editar_articulo"),
    path('articulos/eliminar/<int:pk>/', eliminar_articulo, name="eliminar_articulo"),
    path('articulos/categorias/', categorias, name="categorias"),
    path('articulos/categorias/editar/<int:pk>/', editar_categoria, name="editar_categoria"),
    path('articulos/categorias/eliminar/<int:pk>/', eliminar_categoria, name="eliminar_categoria"),
    path('vehiculos/marcas/', marcas, name="marcas"),
    path('vehiculos/marcas/editar/<int:pk>/', editar_marca, name="editar_marca"),
    path('vehiculos/marcas/eliminar/<int:pk>/', eliminar_marca, name="eliminar_marca"),
    path('proveedores/', proveedores, name="proveedores"),
    path('proveedores/crear/', registrar_proveedor, name="registrar_proveedor"),
    path('proveedores/editar/<int:pk>/', editar_proveedor, name="editar_proveedor"),
    path('proveedores/eliminar/<int:pk>/', eliminar_proveedor, name="eliminar_proveedor"),

]