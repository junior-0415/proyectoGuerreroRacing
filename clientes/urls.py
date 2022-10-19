from django.urls import path
from clientes.views import clientes, registrar_cliente

urlpatterns = [
    path('',clientes,name="clientes"),
    path('crear/',registrar_cliente,name="registrar_cliente"),
]