# Generated by Django 4.1.3 on 2022-12-03 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0008_rename_artestado_articulos_art_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulos',
            name='art_precio',
            field=models.DecimalField(decimal_places=2, default=2, max_digits=10, verbose_name='Precio:'),
            preserve_default=False,
        ),
    ]
