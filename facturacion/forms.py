from dataclasses import field, fields
from pyexpat import model
from socket import fromshare
from django import forms
from django.forms import widgets
#from django_select2 import forms as s2form

from facturacion.models import DetalleFacturaVenta, FacturaVenta

# class ArticuloWidget(s2form.ModelSelect2Widget):
#     search_fields = {
#         "art_nombre__icontains",
#         "id__icontains",
#     }

class FacturaVentaForm(forms.ModelForm):
    class Meta:
        model = FacturaVenta
        exclude = ['fac_estado', 'tbl_empleados_idempleado', 'fac_total_pagar']
        widgets = {
            'fac_fecha': widgets.DateInput(attrs={'type':'date'}, format='%Y-%m-%d')
        }

class DetalleFacturaVentaForm(forms.ModelForm):
    class Meta:
        model = DetalleFacturaVenta
        exclude = ['tbl_facturas_idfactura',]