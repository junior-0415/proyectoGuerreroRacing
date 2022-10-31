from django.db import models
from django.utils.translation import gettext_lazy as _
from articulos.models import Articulos

from clientes.models import Cliente

# Create your models here.

class Servicios(models.Model):
    Tbl_sucursales_idsucursal = models.ForeignKey('Sucursales', on_delete=models.CASCADE, verbose_name="Sucursal:")
    ser_nombre = models.CharField(max_length=50, verbose_name="Nombre:")
    ser_descripcion = models.TextField(max_length=200, verbose_name="Descripción:")
    class Estado(models.TextChoices):
        ACTIVO = '1', _('Activo')
        INACTIVO = '0', _('Inactivo')
    ser_estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO,  verbose_name="Estado:")

class TblRelServiciosEmpleados(models.Model):
    tbl_empleados_idempleado = models.ForeignKey('Empleados', on_delete=models.CASCADE, verbose_name="Empleado:")
    tbl_servicios_idservicio = models.ForeignKey(Servicios, on_delete=models.CASCADE, verbose_name="Servicios:")

class OrdenServicio(models.Model):
    tbl_empleados_idempleado = models.ForeignKey('Empleados', on_delete=models.CASCADE, verbose_name="Nombre:")
    ord_s_identificacion_responsable = models.CharField(max_length=20, verbose_name="Identificación:")
    ord_s_fecha = models.DateField(verbose_name="Fecha:")
    ord_s_telefono_responsable = models.CharField(max_length=20, blank=True, verbose_name="Teléfono:")
    ord_s_celular_resposable = models.CharField(max_length=20, verbose_name="Celular:")
    ord_s_direccion_responsable = models.CharField(max_lenth=100, verbose_name="Dirección:")
    ord_s_fecha_entrega = models.DateField(verbose_name="Entrega:")
    tbl_clientes_idcliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="Nombre:")
    ord_s_identificacion_cli = models.CharField(max_length=20, verbose_name="Identificación:")
    ord_s_telefono_cli = models.CharField(max_length=20, blank=True, verbose_name="Teléfono:")
    ord_s_celular_cli = models.CharField(max_length=20, verbose_name="Celular:")
    ord_s_direccion_cli = models.CharField(max_length=100, blank=True, verbose_name="Dirección:")
    tbl_servicos_idservicio = models.ForeignKey(Servicios, on_delete=models.CASCADE, verbose_name="Servicio:")
    ord_s_vehiculo = models.CharField(max_length=6, verbose_name="Vehículo:")
    ord_s_informe_tecnico = models.TextField(max_length=300, verbose_name="Informe técnico:")
    class EstadoPago(models.TextChoices):
        PAGADO = '1', _('Pagado')
        SINPAGAR = '0', _('Sin pagar')  
    ord_s_estado_pago = models.CharField(max_length=1, choices=EstadoPago.choices, default=EstadoPago.PAGADO, verbose_name="Estado de pago")
    class Estado(models.TextChoices):
        ACTIVO = '1', _('Activo')
        INACTIVO = '0', _('Inactivo')
    ser_estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO,  verbose_name="Estado:")

class TblRelOrdenServicioArticulos(models.Model):
    tbl_orden_servicio_idorden_servicio = models.ForeignKey(OrdenServicio, blank=True, on_delete=models.CASCADE, verbose_name="Orden de servicio:")
    Ttbl_articulos_idarticulo = models.ForeignKey(Articulos, blank=True, on_delete=models.CASCADE, verbose_name="Artículos:")
    art_cantidad = models.SmallIntegerField(max_length=10, blank=True, verbose_name="Cantidad:")
    art_precio = models.DecimalField(max_digts=None, decimal_places=2, blank=True, verbose_name="Precio:")