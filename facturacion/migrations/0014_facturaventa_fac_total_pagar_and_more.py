# Generated by Django 4.1.3 on 2022-12-12 21:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0018_alter_empleados_emp_email_and_more'),
        ('facturacion', '0013_alter_facturaventa_fac_numero_serie'),
    ]

    operations = [
        migrations.AddField(
            model_name='facturaventa',
            name='fac_total_pagar',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Total a pagar:'),
        ),
        migrations.AlterField(
            model_name='facturaventa',
            name='tbl_ordenes_servicio_idorden_servicio',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.ordenservicio', verbose_name='Orden de servicio número:'),
        ),
    ]
