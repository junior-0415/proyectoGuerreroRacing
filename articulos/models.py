from email.policy import default
from tabnanny import verbose
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Proveedores(models.Model):
    pro_nit = models.CharField(max_length=20, verbose_name="Nit/Referencia:")
    pro_nombre = models.CharField(max_length=50, verbose_name="Nombre:")
    pro_categoria = models.CharField(max_length=50, verbose_name="Categoría:") #Pregunta seleccion multiple
    pro_persona_nat = models.CharField(max_length=50, verbose_name="Persona natural:")
    pro_direccion = models.CharField(max_length=100, verbose_name="Dirección:")
    pro_telefono = models.CharField(max_length=20, verbose_name="Teléfono:")
    pro_celular = models.CharField(max_length=20, verbose_name="Celular:")
    pro_email = models.EmailField(max_length=100, verbose_name="Email:")
    pro_sitio_web = models.CharField(max_length=300, verbose_name="Sitio web:")

    class Estado(models.TextChoices):
        ACTIVO = '1', _('Activo')
        INACTIVO = '0', _('Inactivo')
    pro_estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")

    def __str__(self) -> str:
        return "%s" % (self.pro_nombre)

class Categoria(models.Model):
    cat_nombre = models.CharField(max_length=50, verbose_name="Nombre:")
    cat_descripcion = models.TextField(max_length=100, verbose_name="Descripción:")

    class Estado(models.TextChoices):
        ACTIVO = '1', _('Activo')
        INACTIVO = '0', _('Inactivo')
    cat_estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")        

    def __str__(self) -> str:
        return "%s" % (self.cat_nombre)

class Marcas(models.Model):
    mar_nombre = models.CharField(max_length=50, verbose_name="Nombre:")
    mar_descripcion = models.TextField(max_length=200, verbose_name="Descripción:")

    class Estado(models.TextChoices):
        ACTIVO = '1', _('Activo')
        INACTIVO = '0', _('Inactivo')
    mar_estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")

    def __str__(self) -> str:
        return "%s" % (self.mar_nombre)

class Articulos(models.Model):
    art_nombre = models.CharField(max_length=50, verbose_name="Nombre:")
    tbl_categoria_idcategoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categoría:")
    art_precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio:")
    art_descripcion = models.TextField(max_length=200, verbose_name="Descripción:")
    art_stock_minimo = models.SmallIntegerField(verbose_name="Stock mínimo:")
    art_stock_maximo = models.SmallIntegerField(verbose_name="Stock máximo:")
    tbl_proveedores_idproveedor = models.ForeignKey(Proveedores, on_delete=models.CASCADE, verbose_name="Proveedor:")
    tbl_marcas_idmarca = models.ForeignKey(Marcas, on_delete=models.CASCADE, verbose_name="Marca:")
    art_foto = models.ImageField(upload_to='images/articulos', blank=True, default='images/articulos/default.png', verbose_name="Foto:")

    class Estado(models.TextChoices):
        ACTIVO = '1', _('Activo')
        INACTIVO = '0', _('Inactivo')
    art_estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")

    def _stock(self):
        from django.db.models import Sum
        from inventario.models import TblRelPedidosArticulos
        from facturacion.models import DetalleFacturaVenta

        compras = TblRelPedidosArticulos.objects.filter(
            tbl_articulos_idarticulo = self
        ).aggregate(Sum('rel_articulo_cantidad'))

        ventas = DetalleFacturaVenta.objects.filter(
            tbl_articulos_idarticulo = self
        ).aggregate(Sum('dep_cantidad'))

        total = ((compras.get('rel_articulo_cantidad__sum') if compras.get('rel_articulo_cantidad__sum') is not None else 0)-(ventas.get('dep_cantidad__sum') if ventas.get('dep_cantidad__sum') is not None else 0))

        return total

    art_stock_disp = property(_stock)

    def __str__(self) -> str:
        return "%s | %s" % (self.art_nombre, self.art_stock_disp)
