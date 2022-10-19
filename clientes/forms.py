from dataclasses import field, fields
from socket import fromshare
from django import forms

from clientes.models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model= Cliente
        fields='__all__'