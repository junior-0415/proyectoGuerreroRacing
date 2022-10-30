from dataclasses import field, fields
from datetime import datetime
from pyexpat import model
from socket import fromshare
from django import forms

from clientes.models import Ciudades, Cliente, Departamentos, Vehiculo

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

class VehiculosForm(forms.ModelForm):
    class Meta:
        model= Vehiculo
        exclude = ['VehEstado', 'VehTaller']