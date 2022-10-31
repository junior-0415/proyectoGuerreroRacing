from dataclasses import field, fields
from datetime import datetime
from pyexpat import model
from socket import fromshare
from django import forms

from clientes.models import Ciudades, Cliente, Departamentos, Vehiculo

class ClienteForm(forms.ModelForm):
    class Meta:
        model= Cliente
        exclude = ['cli_estado']

class CiudadesForm(forms.ModelForm):
    class Meta:
        model= Ciudades
        exclude = ['ciu_estado']

class DepartamentosForm(forms.ModelForm):
    class Meta:
        model= Departamentos
        exclude = ['dep_estado']

class VehiculosForm(forms.ModelForm):
    class Meta:
        model= Vehiculo
        exclude = ['veh_estado', 'veh_taller']