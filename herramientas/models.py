from django.db import models
from django.utils.translation import gettext_lazy as _
from articulos.models import Articulos, Proveedores

from usuarios.models import Empleados

# Create your models here.

class CotizacionesCompras(models.Model):
    tbl_empleados_idempleado = models.ForeignKey(Empleados, on_delete=models.CASCADE, verbose_name="Empleado:")
    cot_proveedor = models.ForeignKey(Proveedores, on_delete=models.CASCADE, verbose_name="Proveedor:")
    cot_fecha = models.DateField(verbose_name="Fecha:")
    cot_costo_total = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Costo total:")
    class Estado(models.TextChoices):
        ACTIVO = '1', _('Activo')
        INACTIVO = '0', _('Inactivo')
    ord_estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO,  verbose_name="Estado:")

class TblRelCotizacionesComprasArticulos(models.Model):
    tbl_cotizaciones_compras_idcotizacion_compra = models.ForeignKey(CotizacionesCompras, on_delete=models.CASCADE, verbose_name="Cotización de compra número:")
    tbl_articulos_idarticulo = models.ForeignKey(Articulos, on_delete=models.CASCADE, verbose_name="Artículo:")
    rel_cantidad = models.SmallIntegerField(verbose_name="Cantidad:")
    rel_precio_compra = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Precio compra:")
    rel_precio_venta = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Precio venta:")
    rel_total = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Precio total:")