from django.db import models
from django.utils.translation import gettext_lazy as _
from articulos.models import Articulos, Proveedores

from usuarios.models import Empleados

# Create your models here.

class OrdenCompra(models.Model):
    ord_empleado = models.ForeignKey(Empleados, on_delete=models.CASCADE, verbose_name="Empleado responsable:")
    ord_lugar_emision = models.CharField(max_length=50, verbose_name="Lugar de emisión:")
    ord_direccion = models.CharField(max_length=80, verbose_name="Dirección:")
    ord_telefono = models.CharField(max_length=20, blank=True, verbose_name="Teléfono:")
    ord_celular = models.CharField(max_length=20, verbose_name="Celular:")
    ord_email = models.EmailField(max_length=100, verbose_name="Email:")
    ord_fecha = models.DateField(verbose_name="Fecha:")
    ord_proveedor = models.ForeignKey(Proveedores, on_delete=models.CASCADE, verbose_name="Proveedor:")
    class TerminoPago(models.TextChoices):
        METODO1 = 'Pago de contado con efectivo', _('Pago de contado con efectivo')
        METODO2 = 'Pago de contado con tarjeta', _('Pago de contado con tarjeta')
        METODO3 = 'A crédito', _('A crédito')
        METODO4 = 'Pago anticipado con efectivo', _('Pago anticipado con efectivo')
        METODO5 = 'Pago anticipado con tarjeta', _('Pago anticipado con tarjeta')
        METODO6 = 'Otro', _('Otro')
    ord_termino_pago = models.CharField(max_length=28, choices=TerminoPago.choices, verbose_name="Término de pago:")
    class TerminoEntrega(models.TextChoices):
        DOMICILIO = 'Domicilio', _('Domicilio')
        PERSONAL = 'Entrega persononal', _('Entrega personal')
        OTRO = 'Otro', _('Otro')
    ord_termino_entrega = models.CharField(max_length=18, choices=TerminoEntrega.choices, verbose_name="Término de entrega para el pedido")
    ord_otras_tarifas = models.DecimalField(max_digits=7, decimal_places=2, default=0, verbose_name="Ótras tarifas:", blank=True)
    #ord_costo_total = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Costo total estimado:")
    class Estado(models.TextChoices):
        ACTIVO = '1', _('Activo')
        INACTIVO = '0', _('Inactivo')
        CAERRADA = '2', _('Cerrada')
    ord_estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO,  verbose_name="Estado:")

    def _ord_costo_estimado(self):
        from django.db.models import Sum
        from inventario.models import TblRelOrdenCompraArticulos

        articulos = TblRelOrdenCompraArticulos.objects.filter(
            tbl_orden_compras_idorden_compra = self
        ).aggregate(Sum('rel_precio'))
        
        costo_total = articulos.get('rel_precio__sum') if articulos.get('rel_precio__sum') is not None else 0

        return costo_total
    
    ord_costo_estimado = property(_ord_costo_estimado)

    def __str__(self) -> str:
        return "%s" % (self.id)

class TblRelOrdenCompraArticulos(models.Model):
    tbl_orden_compras_idorden_compra = models.ForeignKey(OrdenCompra, on_delete=models.CASCADE, verbose_name="Órden de compra:")
    tbl_articulos_idarticulo = models.ForeignKey(Articulos, on_delete=models.CASCADE, verbose_name="Artículo:")
    rel_cantidad = models.SmallIntegerField(verbose_name="Cantidad:")
    rel_precio = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Precio unitario:")
    def _rel_total(self):
        return self.rel_cantidad*self.rel_precio
    rel_total = property(_rel_total)

class Pedidos(models.Model):
    ped_recivido_por = models.CharField(max_length=80, verbose_name="Recibido por:")
    ped_fecha_recivido = models.DateField(verbose_name="Fecha de recibido:")
    ped_precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio total:")
    class Estado(models.TextChoices):
        ACTIVO = '1', _('Activo')
        INACTIVO = '0', _('Inactivo')
        CERRADO = '2', _('Cerrado')
    ped_estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO,  verbose_name="Estado:")
    def __str__(self) -> str:
        return "%s" % (self.id)

class TblRelPedidosArticulos(models.Model):
    tbl_pedidos_idpedido = models.ForeignKey(Pedidos, on_delete=models.CASCADE, verbose_name="Pedido número:")
    tbl_articulos_idarticulo = models.ForeignKey(Articulos, on_delete=models.CASCADE, verbose_name="Artículo:")
    rel_articulo_cantidad = models.SmallIntegerField(verbose_name="Cantidad:")
    rel_precio_compra = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Precio compra:")
    #rel_precio_venta = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Precio venta:")
    def _get_costo(self):
        return self.rel_articulo_cantidad*self.rel_precio_compra
    art_total = property(_get_costo)