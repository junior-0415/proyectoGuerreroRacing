# Generated by Django 4.1.3 on 2022-12-08 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0011_alter_facturaventa_fac_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='facturaventa',
            name='fac_costo_servicio',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Costo del servicio:'),
        ),
    ]
