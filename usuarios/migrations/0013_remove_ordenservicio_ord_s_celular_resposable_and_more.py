# Generated by Django 4.1.3 on 2022-12-03 22:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0012_remove_ordenservicio_ord_s_direccion_cli_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordenservicio',
            name='ord_s_celular_resposable',
        ),
        migrations.RemoveField(
            model_name='ordenservicio',
            name='ord_s_direccion_responsable',
        ),
        migrations.RemoveField(
            model_name='ordenservicio',
            name='ord_s_email_responsable',
        ),
        migrations.RemoveField(
            model_name='ordenservicio',
            name='ord_s_identificacion_responsable',
        ),
        migrations.RemoveField(
            model_name='ordenservicio',
            name='ord_s_telefono_responsable',
        ),
    ]