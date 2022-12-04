from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

from articulos.models import Articulos, Marcas

# Create your models here.

class Departamentos(models.Model):
    id_depart = models.CharField(max_length=10, verbose_name="Código nacional:")
    dep_nombre = models.CharField(max_length=45, verbose_name="Nombre:")
    class Estado(models.TextChoices):
        ACTIVO = '1', _('Activo')
        INACTIVO = '0', _('Inactivo')
    dep_estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado:")
    def __str__(self) -> str:
        return "%s" % (self.dep_nombre)


class Ciudades(models.Model):
    id_ciudad = models.CharField(max_length=10, verbose_name="Código nacional_")
    ciu_nombre = models.CharField(max_length=45, verbose_name="Nombre:")
    tbl_departamento_iddepart = models.ForeignKey(
        Departamentos, on_delete=models.CASCADE, verbose_name="Departamento:")
    class Estado(models.TextChoices):
        ACTIVO = '1', _('Activo')
        INACTIVO = '0', _('Inactivo')
    ciu_estado = models.CharField(
        max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado:")

    def __str__(self) -> str:
        return "%s - %s" % (self.ciu_nombre, self.tbl_departamento_iddepart)


class Empresa(models.Model):
    empr_nombre = models.CharField(max_length=80, verbose_name="Nombre:")
    empr_nit = models.CharField(max_length=20, verbose_name="Nit:")
    empr_dueno = models.CharField(max_length=80, verbose_name="Dueño:")
    empr_sitio_web = models.CharField(max_length=100, verbose_name="Sitio Web:")
    empr_razon_social = models.TextField(max_length=300, verbose_name="Razon Social:")
    class Estado(models.TextChoices):
        ACTIVO = '1', _('Activo')
        INACTIVO = '0', _('Inactivo')
    empr_estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado:")
    empr_foto = models.ImageField(upload_to='images/empresa', blank=True, default='images/empresa/default.png', verbose_name = "Foto:")
    
    def __str__(self) -> str:
        return "%s" % (self.empr_nombre)

class Sucursales(models.Model):
    tbl_ciudad_idciudad = models.ForeignKey(Ciudades, on_delete=models. CASCADE, verbose_name="Ciudades:")
    tbl_empresas_idempresa = models.ForeignKey(Empresa, on_delete=models. CASCADE, verbose_name="Empresa:")
    suc_nombre = models.CharField(max_length=80, verbose_name="Nombre:")
    suc_administrador = models.CharField(max_length=80, verbose_name="Administrador:")
    suc_direccion = models.CharField(max_length=80, verbose_name="Direccion:")
    class Tipo(models.TextChoices):
        PRINCIPAL = '1', _('Principal')
        SEDE = '0', _('Sede')
    suc_tipo = models.CharField(max_length=1, choices=Tipo.choices, default=Tipo.SEDE, verbose_name="Tipo:")
    suc_telefono = models.CharField(max_length=20, verbose_name="Teléfono:")
    suc_celular = models.CharField(max_length=20, verbose_name="Celular:")
    suc_email = models.CharField(max_length=100, verbose_name="E-mail:")
    class Estado(models.TextChoices):
        ACTIVO = '1', _('Activo')
        INACTIVO = '0', _('Inactivo')
    suc_estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado:")

    def __str__(self) -> str:
        return "%s" % (self.suc_nombre)

class Servicios(models.Model):
    tbl_sucursales_idsucursal = models.ForeignKey(Sucursales, on_delete=models.CASCADE, verbose_name="Sucursal:")
    ser_nombre = models.CharField(max_length=50, verbose_name="Nombre:")
    ser_descripcion = models.TextField(max_length=200, verbose_name="Descripción:")
    class Estado(models.TextChoices):
        ACTIVO = '1', _('Activo')
        INACTIVO = '0', _('Inactivo')
    ser_estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO,  verbose_name="Estado:")

    def __str__(self) -> str:
        return "%s" % (self.ser_nombre)

class Empleados(models.Model):
    tbl_sucursal_idsucursal = models.ForeignKey(Sucursales, on_delete=models. CASCADE, verbose_name="Sucursal:")
    id_emp_identificacion = models.CharField(max_length=50, verbose_name="Identificación:")
    class TipoDocumento(models.TextChoices): 
        TI = 'T.I', _('Tarjeta de Identidad')
        CC = 'C.C', _('Cédula de Ciudadanía')
        CE = 'C.E', _('Cédula de Extranjería')
        Pas = 'Pas', _('Pasaporte')
    emp_tipo_documento = models.CharField(max_length=3, choices=TipoDocumento.choices, default=TipoDocumento.CC, verbose_name="Tipo de documento:")
    tbl_ciudad_idciudad = models.ForeignKey(Ciudades, on_delete=models. CASCADE, verbose_name="Ciudades:")
    emp_nombre = models.CharField(max_length=50, verbose_name="Nombres:")
    emp_apellidos = models.CharField(max_length=50, verbose_name="Apellidos:")
    class Genero(models.TextChoices):
        FEMENINO = 'F', _('Femenino')
        MASCULINO = 'M', _('Masculino')
    emp_genero = models.CharField(max_length=1, choices=Genero.choices, verbose_name="Genero:")
    emp_direccion = models.CharField(max_length=100, verbose_name="Dirección:")
    emp_telefono = models.CharField(max_length=20, verbose_name="Teléfono:")
    emp_celular = models.CharField(max_length=20, verbose_name="Celular:")
    emp_email = models.EmailField(max_length=100, verbose_name="E-mail:")
    emp_fecha_nacimiento = models.DateField( verbose_name="Fecha de nacimiento:")
    emp_cargo = models.CharField(max_length=50, verbose_name="Cargo:")
    emp_num_contrato = models.CharField(max_length=50, verbose_name="Número de Contrato:")
    emp_fecha_ingreso = models.DateField( verbose_name="Fecha de ingreso:")
    class Estado(models.TextChoices):
        ACTIVO = '1', _('Activo')
        INACTIVO = '0', _('Inactivo')
    emp_estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    emp_foto = models.ImageField(upload_to='images/usuarios', blank=True, default='images/usuarios/default.png', verbose_name = "Foto:")
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, default=None)

    def __str__(self) -> str:
        return "%s - %s" % (self.emp_nombre, self.emp_apellidos)

class Cliente(models.Model):
    id_identificacion = models.CharField(max_length=50, verbose_name="Identificación:")
    class TipoDocumento(models.TextChoices):
        TI = 'T.I', _('Tarjeta de Identidad')
        CC = 'C.C', _('Cédula de Ciudadanía')
        CE = 'C.E', _('Cédula de Extranjería')
        Pas = 'Pas', _('Pasaporte')
    cli_tipo_documento = models.CharField(max_length=3, choices=TipoDocumento.choices, default=TipoDocumento.CC, verbose_name="Tipo de documento:")
    cli_nombres = models.CharField(max_length=50, verbose_name="Nombres:")
    cli_apellidos = models.CharField(max_length=50, verbose_name="Apellidos:")
    class Genero(models.TextChoices):
        FEMENINO = 'F', _('Femenino')
        MASCULINO = 'M', _('Masculino')
    cli_genero = models.CharField(max_length=2, choices=Genero.choices, verbose_name="Genero:")
    cli_direccion = models.CharField(max_length=100, verbose_name="Dirección:")
    tbl_ciudades_idciudad = models.ForeignKey(Ciudades, on_delete=models.CASCADE, verbose_name="Ciudad")
    cli_telefono = models.CharField(max_length=20, blank=True, verbose_name="Teléfono:")
    cli_celular = models.CharField(max_length=20, verbose_name="Celular")
    cli_email = models.EmailField(max_length=100, verbose_name="Email")
    class Estado(models.TextChoices):
        ACTIVO = '1', _('Activo')
        INACTIVO = '0', _('Inactivo')
    cli_estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")

    def __str__(self) -> str:
        return "%s - %s" % (self.cli_nombres, self.cli_apellidos)

class Vehiculo(models.Model):
    id_matricula = models.CharField(max_length=6, verbose_name="Matrícula:")
    tbl_cliente_ididentificacion = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="Dueño:")
    veh_modelo = models.CharField(max_length=45, verbose_name="Modelo:")
    veh_color = models.CharField(max_length=20, verbose_name="Color:")
    tbl_marcas_idmarca = models.ForeignKey(Marcas, on_delete=models.CASCADE, verbose_name="Marca:")
    veh_version = models.CharField(max_length=20, verbose_name="Versión:")
    veh_anio = models.CharField(max_length=4, verbose_name="Año:")  # preguntas
    veh_chasis_vin = models.CharField(max_length=45, verbose_name="Chasis_VIN:")
    veh_motor = models.CharField(max_length=45, verbose_name="Motor:")
    veh_ultima_fecha_ingreso = models.DateField(verbose_name="Ultima fecha de ingreso:")
    veh_ultima_fecha_salida = models.DateField(verbose_name="Ultima fecha de salida:")
    veh_informe_tecnico = models.TextField(max_length=200, verbose_name="Informe técnico:")
    class Estado(models.TextChoices):
        ACTIVO = '1', _('Activo')
        INACTIVO = '0', _('Inactivo')
    veh_estado = models.CharField(
        max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    class EnTaller(models.TextChoices):
        EN_TALLER = 'Si', _('En taller')
        ENTREGADO = 'No', _('Entregado')
    veh_taller = models.CharField(max_length=2, choices=EnTaller.choices, default=EnTaller.EN_TALLER, verbose_name="Proceso:")

    def __str__(self) -> str:
        return "%s" % (self.id_matricula)

class TblRelServiciosEmpleados(models.Model):
    tbl_empleados_idempleado = models.ForeignKey(Empleados, on_delete=models.CASCADE, verbose_name="Empleado:")
    tbl_servicios_idservicio = models.ForeignKey(Servicios, on_delete=models.CASCADE, verbose_name="Servicios:")

class TblRelClienteServicios(models.Model):
    tbl_cliente_ididentificacion=models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="Cliente:")
    tbl_servicios_idservicio=models.ForeignKey(Servicios, on_delete=models.CASCADE, verbose_name="Servicio:")

class OrdenServicio(models.Model):
    tbl_empleados_idempleado = models.ForeignKey(Empleados, on_delete=models.CASCADE, verbose_name="Nombre:")
    ord_s_fecha = models.DateField(verbose_name="Fecha de registro:")
    ord_s_fecha_entrega = models.DateField(verbose_name="Entrega:")
    tbl_clientes_idcliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="Cliente:")
    ord_s_identificacion_cli = models.CharField(max_length=20, verbose_name="Identificación:")
    ord_s_celular_cli = models.CharField(max_length=20, verbose_name="Celular:")
    tbl_servicos_idservicio = models.ForeignKey(Servicios, on_delete=models.CASCADE, verbose_name="Servicio:")
    ord_s_vehiculo = models.CharField(max_length=6, verbose_name="Vehículo:")
    ord_s_informe_tecnico = models.TextField(max_length=300, verbose_name="Informe técnico:")
    class EstadoPago(models.TextChoices):
        PAGADO = '1', _('Pagado')
        SINPAGAR = '0', _('Sin pagar')
    ord_s_estado_pago = models.CharField(max_length=1, choices=EstadoPago.choices, verbose_name="Estado de pago")
    class Estado(models.TextChoices):
        ACTIVO = '1', _('Activo')
        INACTIVO = '0', _('Inactivo')
    ser_estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO,  verbose_name="Estado:")

    def __str__(self) -> str:
        return "%s" % (self.id)

class TblRelOrdenServicioArticulos(models.Model):
    tbl_orden_servicio_idorden_servicio = models.ForeignKey(OrdenServicio, on_delete=models.CASCADE, verbose_name="Orden de servicio:")
    Ttbl_articulos_idarticulo = models.ForeignKey(Articulos, blank=True, on_delete=models.CASCADE, verbose_name="Artículos:")
    art_cantidad = models.SmallIntegerField(blank=True, verbose_name="Cantidad:")
    art_precio = models.DecimalField(max_digits=9, decimal_places=2, blank=True, verbose_name="Precio:")
    class Estado(models.TextChoices):
        ACTIVO = '1', _('Activo')
        INACTIVO = '0', _('Inactivo')
    def _get_costo(self):
        return self.art_cantidad*self.art_precio
    art_costo = property(_get_costo)