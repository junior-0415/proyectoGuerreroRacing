from dataclasses import field, fields
from pyexpat import model
from socket import fromshare
from django import forms
from django.forms import widgets

from inventario.models import OrdenCompra, Pedidos, TblRelOrdenCompraArticulos, TblRelPedidosArticulos

class OrdenCompraForm(forms.ModelForm):
    class Meta:
        model= OrdenCompra
        exclude = ['ord_estado', 'ord_empleado']
        widgets = {
            'ord_fecha': widgets.DateInput(attrs={'type':'date'})
        }

class TblRelOrdenCompraArticulosForm(forms.ModelForm):
    class Meta:
        model = TblRelOrdenCompraArticulos
        exclude = ['tbl_orden_compras_idorden_compra']

class PedidosComprasForm(forms.ModelForm):
    class Meta:
        model= Pedidos
        exclude = ['ped_estado']
        widgets = {
            'ped_fecha_recivido': widgets.DateInput(attrs={'type':'date'}, format='%Y-%m-%d')
        }

class TblRelPedidosArticulosForm(forms.ModelForm):
    class Meta:
        model= TblRelPedidosArticulos
        exclude = ['tbl_pedidos_idpedido']