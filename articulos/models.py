from email.policy import default
from tabnanny import verbose
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Proveedores(models.Model):
    ProNit = models.CharField(max_length=20, verbose_name="Nit/Referencia:")
    ProNombre = models.CharField(max_length=50, verbose_name="Nombre:")
    ProCategoria = models.CharField(max_length=50, verbose_name="Categoría:") #Pregunta seleccion multiple
    ProPersonaNat = models.CharField(max_length=50, verbose_name="Persona natural:")
    ProDireccion = models.CharField(max_length=100, verbose_name="Dirección:")
    ProTelefono = models.CharField(max_length=20, verbose_name="Teléfono:")
    ProCelular = models.CharField(max_length=20, verbose_name="Celular:")
    ProEmail = models.EmailField(max_length=100, verbose_name="Email:")
    ProSitioWeb = models.CharField(max_length=300, verbose_name="Sitio web:")

    class Estado(models.TextChoices):
        ACTIVO = '1', _('Activo')
        INACTIVO = '0', _('Inactivo')
    ProEstado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")

    def __str__(self) -> str:
        return "%s" % (self.ProNombre)

class Categoria(models.Model):
    CatNombre = models.CharField(max_length=50, verbose_name="Nombre:")
    CatDescripcion = models.TextField(max_length=100, verbose_name="Descripción:")

    class Estado(models.TextChoices):
        ACTIVO = '1', _('Activo')
        INACTIVO = '0', _('Inactivo')
    CatEstado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")        

    def __str__(self) -> str:
        return "%s" % (self.CatNombre)

class Marcas(models.Model):
    MarNombre = models.CharField(max_length=50, verbose_name="Nombre:")
    MarDescripcion = models.TextField(max_length=200, verbose_name="Descripción:")

    class Estado(models.TextChoices):
        ACTIVO = '1', _('Activo')
        INACTIVO = '0', _('Inactivo')
    MarEstado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")

    def __str__(self) -> str:
        return "%s" % (self.MarNombre)

class Articulos(models.Model):
    ArtNombre = models.CharField(max_length=50, verbose_name="Nombre:")
    TblCategoria_idCategoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categoría:")
    ArtStockDisp = models.SmallIntegerField(blank=True, default=0, verbose_name="Stock Disponible:")
    ArtDescripcion = models.TextField(max_length=200, verbose_name="Descripción:")
    ArtStockMinimo = models.SmallIntegerField(verbose_name="Stock mínimo:")
    ArtStockMaximo = models.SmallIntegerField(verbose_name="Stock máximo:")
    TblProveedores_idProveedor = models.ForeignKey(Proveedores, on_delete=models.CASCADE, verbose_name="Proveedor:")
    TblMarcas_idMarca = models.ForeignKey(Marcas, on_delete=models.CASCADE, verbose_name="Marca:")
    ArtFoto = models.ImageField(upload_to='images/articulos', blank=True, default='images/articulos/default.png', verbose_name="Foto:")

    class Estado(models.TextChoices):
        ACTIVO = '1', _('Activo')
        INACTIVO = '0', _('Inactivo')
    ArtEstado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")

    def __str__(self) -> str:
        return "%s" % (self.ArtNombre)