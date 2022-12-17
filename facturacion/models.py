from django.db import models
from django.utils.translation import gettext_lazy as _
from articulos.models import Articulos

from usuarios.models import Cliente, Empleados, OrdenServicio

# Create your models here.

class FacturaVenta(models.Model):
    fac_numero_serie = models.AutoField(primary_key=True, verbose_name="Número de serie:", unique=True)
    tbl_ordenes_servicio_idorden_servicio = models.OneToOneField(OrdenServicio, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Orden de servicio número:")
    tbl_empleados_idempleado = models.ForeignKey(Empleados, on_delete=models.CASCADE, verbose_name="Empleado:")
    tbl_clientes_idcliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="Cliente:")
    fac_fecha = models.DateField(auto_now=True, verbose_name="Fecha:")
    fac_costo_servicio = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name="Costo del servicio:")
    fac_caja = models.CharField(max_length=10, verbose_name="Caja número:")
    fac_descuentos = models.DecimalField(max_digits=7, decimal_places=2, default=0, verbose_name="Descuento:")
    fac_total_pagar = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Total a pagar:")
    fac_observaciones = models.TextField(max_length=500, verbose_name="Observaciones:")
    class Estado(models.TextChoices):
        ACTIVO = '1', _('Activo')
        INACTIVO = '0', _('Inactivo')
        CERRADA = '2', _('Cerrada')
    fac_estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO,  verbose_name="Estado:")
    def _pagar_cliente(self):
        costo_ser = self.fac_costo_servicio
        costo_art = self.fac_total_pagar
        descuento = self.fac_descuentos
        total = (costo_ser + costo_art) - descuento
        return total
    fac_pagar_cliente = property(_pagar_cliente)

    # def _pagar(self):
    #     from django.db.models import Sum
    #     from facturacion.models import DetalleFacturaVenta

    #     articulos = DetalleFacturaVenta.objects.filter(
    #         tbl_facturas_idfactura = self
    #     ).aggregate(Sum('dep_total'))
        
    #     costo_art = articulos.get('dep_total__sum') if articulos.get('dep_total__sum') is not None else 0

    #     costo_ser = self.fac_costo_servicio

    #     descuento = self.fac_descuentos

    #     total = (costo_art + costo_ser)-descuento

    #     return total
    
    # fac_total_pagar = property(_pagar)

    def __str__(self) -> str:
        return "%s" % (self.fac_numero_serie)

class DetalleFacturaVenta(models.Model):
    tbl_facturas_idfactura = models.ForeignKey(FacturaVenta, on_delete=models.CASCADE, verbose_name="Factura número:")
    tbl_articulos_idarticulo = models.ForeignKey(Articulos, on_delete=models.CASCADE, verbose_name="Artículos:")
    dep_precio = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Precio:")
    dep_cantidad = models.SmallIntegerField(verbose_name="Cantidad:")
    class Estado(models.TextChoices):
        ACTIVO = '1', _('Activo')
        INACTIVO = '0', _('Inactivo')
    
    def _dep_total(self):
        return self.dep_cantidad*self.dep_precio
    dep_total = property(_dep_total)

    def __str__(self) -> str:
        return "%s" % (self.tbl_articulos_idarticulo)