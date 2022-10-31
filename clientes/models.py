from email.policy import default
from random import choices
from tabnanny import verbose
from django.utils.translation import gettext_lazy as _
from django.db import models

from articulos.models import Marcas
from empleadosuser.models import Servicios

# Create your models here.


class Departamentos(models.Model):
    id_depart = models.CharField(max_length=10, verbose_name="Código nacional")
    dep_nombre = models.CharField(max_length=45, verbose_name="Nombre")

    class Estado(models.TextChoices):
        ACTIVO = '1', _('Activo')
        INACTIVO = '0', _('Inactivo')
    dep_estado = models.CharField(
        max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")

    def __str__(self) -> str:
        return "%s" % (self.DepNombre)


class Ciudades(models.Model):
    id_ciudad = models.CharField(max_length=10, verbose_name="Código nacional")
    ciu_nombre = models.CharField(max_length=45, verbose_name="Nombre")
    tbl_departamento_iddepart = models.ForeignKey(
        Departamentos, on_delete=models.CASCADE, verbose_name="Departamento")

    class Estado(models.TextChoices):
        ACTIVO = '1', _('Activo')
        INACTIVO = '0', _('Inactivo')
    ciu_estado = models.CharField(
        max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")

    def __str__(self) -> str:
        return "%s - %s" % (self.CiuNombre, self.TblDepartamento_idDepart)


class Cliente(models.Model):
    id_identificacion = models.CharField(
        max_length=50, verbose_name="Identificación:")

    class TipoDocumento(models.TextChoices):
        TI = 'T.I', _('Tarjeta de Identidad')
        CC = 'C.C', _('Cédula de Ciudadanía')
        CE = 'C.E', _('Cédula de Extranjería')
        Pas = 'Pas', _('Pasaporte')
    cli_tipo_documento = models.CharField(max_length=3, choices=TipoDocumento.choices, default=TipoDocumento.CC, verbose_name="Tipo de documento")
    cli_nombres = models.CharField(max_length=50, verbose_name="Nombres:")
    cli_apellidos = models.CharField(max_length=50, verbose_name="Apellidos:")

    class Genero(models.TextChoices):
        FEMENINO = 'F', _('Femenino')
        MASCULINO = 'M', _('Maculino')
    cli_genero = models.CharField(max_length=2, choices=Genero.choices)
    cli_direccion = models.CharField(max_length=100, verbose_name="Dirección")
    tbl_ciudades_idciudad = models.ForeignKey(
        Ciudades, on_delete=models.CASCADE, verbose_name="Ciudad")
    cli_telefono = models.CharField(max_length=20, blank=True, verbose_name="Teléfono")
    cli_celular = models.CharField(max_length=20, verbose_name="Celular")
    cli_email = models.EmailField(max_length=100, verbose_name="Email")

    class Estado(models.TextChoices):
        ACTIVO = '1', _('Activo')
        INACTIVO = '0', _('Inactivo')
    cli_estado = models.CharField(
        max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")

    def __str__(self) -> str:
        return "%s - %s" % (self.CliNombres, self.CliApellidos)

class Vehiculo(models.Model):
    id_matricula = models.CharField(max_length=6, verbose_name="Matrícula")
    tbl_cliente_ididentificacion = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="Dueño")
    veh_modelo = models.CharField(max_length=45, verbose_name="Modelo")
    veh_color = models.CharField(max_length=20, verbose_name="Color")
    tbl_marcas_idmarca = models.ForeignKey(Marcas, on_delete=models.CASCADE, verbose_name="Marca")
    veh_version = models.CharField(max_length=20, verbose_name="Versión")
    veh_anio = models.CharField(max_length=4, verbose_name="Año")  # preguntas
    veh_chasis_vin = models.CharField(max_length=45, verbose_name="Chasis_VIN")
    veh_motor = models.CharField(max_length=45, verbose_name="Motor")
    veh_ultima_fecha_ingreso = models.DateField(
        verbose_name="Ultima fecha de ingreso")
    veh_ultima_fecha_salida = models.DateField(
        verbose_name="Ultima fecha de Salida")
    veh_informe_tecnico = models.TextField(
        max_length=200, verbose_name="Informe técnico")

    class Estado(models.TextChoices):
        ACTIVO = '1', _('Activo')
        INACTIVO = '0', _('Inactivo')
    veh_estado = models.CharField(
        max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")

    class EnTaller(models.TextChoices):
        EN_TALLER = 'Si', _('En taller')
        ENTREGADO = 'No', _('Entregado')
    veh_taller = models.CharField(max_length=2, choices=EnTaller.choices, default=EnTaller.EN_TALLER, verbose_name="Proceso:")


class TblRelClienteServicios(models.Model):
    tbl_cliente_ididentificacion=models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="Cliente:")
    tbl_servicios_idservicio=models.ForeignKey(Servicios, on_delete=models.CASCADE, verbose_name="Servicio:")
