from dataclasses import field, fields
from pyexpat import model
from socket import fromshare
from django import forms

from inventario.models import OrdenCompra, Pedidos

class OrdenCompraForm(forms.ModelForm):
    class Meta:
        model= OrdenCompra
        exclude = ['ord_estado']

class PedidosComprasForm(forms.ModelForm):
    class Meta:
        model= Pedidos
        exclude = ['ped_estado']