from django import forms
from django.forms import widgets
from django_select2 import forms as s2forms

from usuarios.models import Ciudades, Cliente, Departamentos, Empleados, Empresa, OrdenServicio, Servicios, Sucursales, Vehiculo, TblRelOrdenServicioArticulos

class CiudadesForm(forms.ModelForm):
    class Meta:
        model= Ciudades
        exclude = ['ciu_estado']

class CiudadesWidget(s2forms.ModelSelect2Widget):
    search_fields = {
        "ciu_nombre__icontains",
        "id__icontains",
    } # campos de busqueda

class DepartamentosForm(forms.ModelForm):
    class Meta:
        model= Departamentos
        exclude = ['dep_estado']

class ServiciosForm(forms.ModelForm):
    class Meta:
        model= Servicios
        exclude = ['ser_estado']

class ClienteForm(forms.ModelForm):
    class Meta:
        model= Cliente
        exclude = ['cli_estado']
        widgets = {
            'tbl_ciudades_idciudad':CiudadesWidget,
        }

class VehiculosForm(forms.ModelForm):
    class Meta:
        model= Vehiculo
        exclude = ['veh_estado', 'veh_taller']

class EmpleadosForm(forms.ModelForm):
    class Meta:
        model = Empleados
        exclude = ['emp_estado', 'user']
        widgets = {
            'emp_fecha_nacimiento': widgets.DateInput(attrs={'type':'date'}),
            'emp_fecha_ingreso': widgets.DateInput(attrs={'type':'date'})
        }

class OrdenServicioForm(forms.ModelForm):
    class Meta:
        model = OrdenServicio
        exclude = ['ser_estado']

class TblRelOrdenServicioArticulosForm(forms.ModelForm):
    class Meta:
        model = TblRelOrdenServicioArticulos
        exclude = ['tbl_orden_servicio_idorden_servicio', 'tbl_estado', 'art_costo']

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        exclude = ['empr_estado']

class SucursalesForm(forms.ModelForm):
    class Meta:
        model = Sucursales
        exclude = ['suc_estado']