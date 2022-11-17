from dataclasses import field, fields
from pyexpat import model
from socket import fromshare
from django import forms
from django.forms import widgets
from articulos.forms import ArticulosWidget

from facturacion.models import DetalleFactura, FacturaVenta

class FacturaVentaForm(forms.ModelForm):
    class Meta:
        model = FacturaVenta
        exclude = ['fac_estado', 'tbl_empleados_idempleado', 'fac_total_pagar']
        widgets = {
            'fac_fecha': widgets.DateInput(attrs={'type':'date'}, format='%Y-%m-%d')
        }

class DetalleFacturaForm(forms.ModelForm):
    class Meta:
        model = DetalleFactura
        exclude = ['dep_estado', 'tbl_facturas_idfactura']
        widgets = {
            'tbl_articulos_idarticulo':ArticulosWidget,
        }