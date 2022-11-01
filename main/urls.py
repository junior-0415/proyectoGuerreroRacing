"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404

###### Importes para subir imagenes #####
from django.conf import settings
from django.conf.urls.static import static
#########################################

from main.views import eliminar_def_articulo, eliminar_def_categoria, eliminar_def_ciudad, eliminar_def_cliente, eliminar_def_depart, eliminar_def_marca, eliminar_def_proveedor, eliminar_def_vehiculo, inicio, inicioAdmin, login, papelera_reciclaje, restablecer_articulo, restablecer_categoria, restablecer_ciudad, restablecer_cliente, restablecer_departamento, restablecer_marca, restablecer_proveedor, restablecer_vehiculo

# handler404= Error_404.as_view()s

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),
    path('adm/', inicioAdmin, name='inicio-admin'),
    path('login/', login, name="login"),
    path('', include('articulos.urls')),
    path('', include('usuarios.urls')),
    path('papelera-de-reciclaje/', papelera_reciclaje, name="papelera"),
    path('papelera-de-reciclaje/clientes/restablecer/<int:pk>/', restablecer_cliente, name="restablecer_cliente"),
    path('papelera-de-reciclaje/clientes/eliminar/<int:pk>/', eliminar_def_cliente, name="eliminar_def_cliente"),
    path('papelera-de-reciclaje/ciudades/restablecer/<int:pk>/', restablecer_ciudad, name="restablecer_ciudad"),
    path('papelera-de-reciclaje/ciudades/eliminar/<int:pk>/', eliminar_def_ciudad, name="eliminar_def_ciudad"),
    path('papelera-de-reciclaje/departamentos/restablecer/<int:pk>/', restablecer_departamento, name="restablecer_departamento"),
    path('papelera-de-reciclaje/departamentos/eliminar/<int:pk>/', eliminar_def_depart, name="eliminar_def_depart"),
    path('papelera-de-reciclaje/marcas/restablecer/<int:pk>/', restablecer_marca, name="restablecer_marca"),
    path('papelera-de-reciclaje/marcas/eliminar/<int:pk>/', eliminar_def_marca, name="eliminar_def_marca"),
    path('papelera-de-reciclaje/categorias/restablecer/<int:pk>/', restablecer_categoria, name="restablecer_categoria"),
    path('papelera-de-reciclaje/categorias/eliminar/<int:pk>/', eliminar_def_categoria, name="eliminar_def_categoria"),
    path('papelera-de-reciclaje/proveedores/restablecer/<int:pk>/', restablecer_proveedor, name="restablecer_proveedor"),
    path('papelera-de-reciclaje/proveedores/eliminar/<int:pk>/', eliminar_def_proveedor, name="eliminar_def_proveedor"),
    path('papelera-de-reciclaje/articulos/restablecer/<int:pk>/', restablecer_articulo, name="restablecer_articulo"),
    path('papelera-de-reciclaje/articulos/eliminar/<int:pk>/', eliminar_def_articulo, name="eliminar_def_articulo"),
    path('papelera-de-reciclaje/vehiculos/restablecer/<int:pk>/', restablecer_vehiculo, name="restablecer_vehiculo"),
    path('papelera-de-reciclaje/vehiculos/eliminar/<int:pk>/', eliminar_def_vehiculo, name="eliminar_def_vehiculo"),
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)