from email.policy import default
from random import choices
from tabnanny import verbose
from django.utils.translation import gettext_lazy as _
from django.db import models

# Create your models here.
class Departamentos(models.Model):
    DepNombre=models.CharField(max_length=45, verbose_name="Nombre")

class Ciudades(models.Model):
    CiuNombre=models.CharField(max_length=45, verbose_name="Nombre")
    TblDepartamento_idDepart=models.ForeignKey(Departamentos, on_delete=models.CASCADE, verbose_name="Departamento")

class Cliente(models.Model):
    idIdentificacion=models.CharField(max_length=50, verbose_name="Identificación")
    class TipoDocumento(models.TextChoices):
        TI='T.I', _('Tarjeta de Identidad')
        CC='C.C', _('Cédula de Ciudadanía')
        CE='C.E', _('Cédula de Extranjería')
        Pas='Pas', _('Pasaporte')
    CliTipoDocumento=models.CharField(max_length=4, choices=TipoDocumento.choices, default=TipoDocumento.CC, verbose_name="Tipo de documento")
    CliNombres=models.CharField(max_length=50, verbose_name="Nombres")
    CliApellidos=models.CharField(max_length=50, verbose_name="Apellidos")
    class Genero(models.TextChoices):
        FEMENINO='F', _('Femenino')
        MASCULINO='M', _('Maculino')
    CliGenero=models.CharField(max_length=2, choices=Genero.choices)
    CliDireccion=models.CharField(max_length=100, verbose_name="Dirección")
    TblCiudades_idCiudad=models.ForeignKey(Ciudades, on_delete=models.CASCADE, verbose_name="Ciudad")
    CliTelefono=models.CharField(max_length=20, verbose_name="Teléfono")
    CliCelular=models.CharField(max_length=20, verbose_name="Celular")
    CliEmail=models.CharField(max_length=100, verbose_name="Email")

class Marcas(models.Model):
    MarNombre=models.CharField(max_length=50, verbose_name="Nombre")
    class CategoriaMar(models.TextChoices):
        MOTO='Motos', _('Motos')
        CARRO='Carro', _('Carro')
    MarCategoria=models.CharField(max_length=5, choices=CategoriaMar.choices) #preguntas
    Marvaloracion=models.CharField(max_length=5, verbose_name="Valoración")

class Vehiculo(models.Model):
    idMatricula=models.CharField(max_length=6, verbose_name="Matrícula")
    TblCliente_idIdentificacion=models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="Dueño")
    VehModelo=models.CharField(max_length=45, verbose_name="Modelo")
    VehColor=models.CharField(max_length=20, verbose_name="Color")
    TblMarcas_idMarca=models.ForeignKey(Marcas, on_delete=models.CASCADE, verbose_name="Marca")
    VehVersion=models.CharField(max_length=20, verbose_name="Versión")
    VehAnio=models.DateField(verbose_name="Año", help_text=u"AAAA") #preguntas
    VehChasis_VIN=models.CharField(max_length=45, verbose_name="Chasis_VIN")
    VehMotor=models.CharField(max_length=45, verbose_name="Motor")
    VehUltima_Fecha_Ingreso=models.DateField(verbose_name="Ultima fecha de ingreso", help_text=u"MM/DD/AAA")
    VehUltima_Fecha_Salida=models.DateField(verbose_name="Ultima fecha de Salida", help_text=u"MM/DD/AAA")
    VehInforme_Tecnico=models.CharField(max_length=200, verbose_name="Informe técnico")

"""class TblRelClienteServicios(models.Model):
    TblCliente_idIdentificacion=models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="Cliente")
    TblServicios_idServicio=models.ForeignKey('Servicios', on_delete=models.CASCADE, verbose_name="Servicio")"""