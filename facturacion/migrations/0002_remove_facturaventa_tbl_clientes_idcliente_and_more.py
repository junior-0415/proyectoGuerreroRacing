# Generated by Django 4.1.2 on 2022-11-13 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facturaventa',
            name='tbl_clientes_idcliente',
        ),
        migrations.RemoveField(
            model_name='facturaventa',
            name='tbl_empleados_idempleado',
        ),
        migrations.RemoveField(
            model_name='facturaventa',
            name='tbl_ordenes_servicio_idorden_servicio',
        ),
        migrations.DeleteModel(
            name='DetalleFactura',
        ),
        migrations.DeleteModel(
            name='FacturaVenta',
        ),
    ]
