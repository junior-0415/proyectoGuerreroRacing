# Generated by Django 4.1.3 on 2022-12-07 22:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0015_alter_ordenservicio_ord_s_estado_pago'),
        ('facturacion', '0009_remove_facturaventa_fac_total_pagar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facturaventa',
            name='tbl_ordenes_servicio_idorden_servicio',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.ordenservicio', verbose_name='Órden de servicio número:'),
        ),
    ]
