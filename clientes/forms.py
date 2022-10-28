from dataclasses import field, fields
from pyexpat import model
from socket import fromshare
from django import forms

from clientes.models import Ciudades, Cliente, Departamentos

class ClienteForm(forms.ModelForm):
    class Meta:
        model= Cliente
        exclude = ['CliEstado']

class CiudadesForm(forms.ModelForm):
    class Meta:
        model= Ciudades
        exclude = ['CiuEstado']

class DepartamentosForm(forms.ModelForm):
    class Meta:
        model= Departamentos
        exclude = ['DepEstado']