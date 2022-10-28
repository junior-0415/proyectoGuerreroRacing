from dataclasses import field, fields
from pyexpat import model
from socket import fromshare
from django import forms

from articulos.models import Articulos, Categoria, Marcas, Proveedores

class ArticulosForm(forms.ModelForm):
    ArtNombre = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'Ingrese el nombre de artículo'})
    )
    class Meta:
        model= Articulos
        exclude = ['ArtStockDisp', 'ArtEstado']

class CategoriasForm(forms.ModelForm):
    class Meta:
        model= Categoria
        exclude = ['CatEstado']

class MarcasForm(forms.ModelForm):
    class Meta:
        model= Marcas
        exclude = ['MarEstado']

class ProveedoresForm(forms.ModelForm):
    class Meta:
        model= Proveedores
        exclude = ['ProEstado']