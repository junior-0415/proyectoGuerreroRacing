from email.policy import default
from random import choices
from tabnanny import verbose
from django.utils.translation import gettext_lazy as _
from django.db import models

from articulos.models import Marcas

# Create your models here.


class Departamentos(models.Model):
    idDepart = models.CharField(max_length=10, verbose_name="Código nacional")
    DepNombre = models.CharField(max_length=45, verbose_name="Nombre")

    class Estado(models.TextChoices):
        ACTIVO = '1', _('Activo')
        INACTIVO = '0', _('Inactivo')
    DepEstado = models.CharField(
        max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")

    def __str__(self) -> str:
        return "%s" % (self.DepNombre)


class Ciudades(models.Model):
    idCiudad = models.CharField(max_length=10, verbose_name="Código nacional")
    CiuNombre = models.CharField(max_length=45, verbose_name="Nombre")
    TblDepartamento_idDepart = models.ForeignKey(
        Departamentos, on_delete=models.CASCADE, verbose_name="Departamento")

    class Estado(models.TextChoices):
        ACTIVO = '1', _('Activo')
        INACTIVO = '0', _('Inactivo')
    CiuEstado = models.CharField(
        max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")

    def __str__(self) -> str:
        return "%s - %s" % (self.CiuNombre, self.TblDepartamento_idDepart)


class Cliente(models.Model):
    idIdentificacion = models.CharField(
        max_length=50, verbose_name="Identificación:")

    class TipoDocumento(models.TextChoices):
        TI = 'T.I', _('Tarjeta de Identidad')
        CC = 'C.C', _('Cédula de Ciudadanía')
        CE = 'C.E', _('Cédula de Extranjería')
        Pas = 'Pas', _('Pasaporte')
    CliTipoDocumento = models.CharField(max_length=4, choices=TipoDocumento.choices, default=TipoDocumento.CC, verbose_name="Tipo de documento")
    CliNombres = models.CharField(max_length=50, verbose_name="Nombres")
    CliApellidos = models.CharField(max_length=50, verbose_name="Apellidos")

    class Genero(models.TextChoices):
        FEMENINO = 'F', _('Femenino')
        MASCULINO = 'M', _('Maculino')
    CliGenero = models.CharField(max_length=2, choices=Genero.choices)
    CliDireccion = models.CharField(max_length=100, verbose_name="Dirección")
    TblCiudades_idCiudad = models.ForeignKey(
        Ciudades, on_delete=models.CASCADE, verbose_name="Ciudad")
    CliTelefono = models.CharField(max_length=20, blank=True, verbose_name="Teléfono")
    CliCelular = models.CharField(max_length=20, verbose_name="Celular")
    CliEmail = models.EmailField(max_length=100, verbose_name="Email")

    class Estado(models.TextChoices):
        ACTIVO = '1', _('Activo')
        INACTIVO = '0', _('Inactivo')
    CliEstado = models.CharField(
        max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")

    def __str__(self) -> str:
        return "%s - %s" % (self.CliNombres, self.CliApellidos)

class Vehiculo(models.Model):
    idMatricula = models.CharField(max_length=6, verbose_name="Matrícula")
    TblCliente_idIdentificacion = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="Dueño")
    VehModelo = models.CharField(max_length=45, verbose_name="Modelo")
    VehColor = models.CharField(max_length=20, verbose_name="Color")
    TblMarcas_idMarca = models.ForeignKey(Marcas, on_delete=models.CASCADE, verbose_name="Marca")
    VehVersion = models.CharField(max_length=20, verbose_name="Versión")
    VehAnio = models.CharField(max_length=4, verbose_name="Año")  # preguntas
    VehChasis_VIN = models.CharField(max_length=45, verbose_name="Chasis_VIN")
    VehMotor = models.CharField(max_length=45, verbose_name="Motor")
    VehUltima_Fecha_Ingreso = models.DateField(
        verbose_name="Ultima fecha de ingreso")
    VehUltima_Fecha_Salida = models.DateField(
        verbose_name="Ultima fecha de Salida")
    VehInforme_Tecnico = models.TextField(
        max_length=200, verbose_name="Informe técnico")

    class Estado(models.TextChoices):
        ACTIVO = '1', _('Activo')
        INACTIVO = '0', _('Inactivo')
    VehEstado = models.CharField(
        max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")

    class EnTaller(models.TextChoices):
        EN_TALLER = 'Si', _('En taller')
        ENTREGADO = 'No', _('Entregado')
    VehTaller = models.CharField(max_length=2, choices=EnTaller.choices, default=EnTaller.EN_TALLER, verbose_name="Proceso:")


"""class TblRelClienteServicios(models.Model):
    TblCliente_idIdentificacion=models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="Cliente")
    TblServicios_idServicio=models.ForeignKey('Servicios', on_delete=models.CASCADE, verbose_name="Servicio")"""
