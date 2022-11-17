from dataclasses import field, fields
from pyexpat import model
from socket import fromshare
from django import forms
from django_select2 import forms as s2form

from articulos.models import Articulos, Categoria, Marcas, Proveedores

class ArticulosForm(forms.ModelForm):
    art_nombre = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'Ingrese el nombre de artículo'})
    )
    class Meta:
        model= Articulos
        exclude = ['art_stock_disp', 'art_estado']

class ArticulosWidget(s2form.ModelSelect2Widget):
    search_fields = {
        "art_nombre__icontains",
        "id__icontains",
    }

class CategoriasForm(forms.ModelForm):
    class Meta:
        model= Categoria
        exclude = ['cat_estado']

class MarcasForm(forms.ModelForm):
    class Meta:
        model= Marcas
        exclude = ['mar_estado']

class ProveedoresForm(forms.ModelForm):
    class Meta:
        model= Proveedores
        exclude = ['pro_estado']