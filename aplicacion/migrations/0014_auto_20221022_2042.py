# Generated by Django 3.2.8 on 2022-10-23 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0013_alter_mascotas_telefono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascotas',
            name='telefono',
            field=models.IntegerField(null=True, verbose_name='Telefono'),
        ),
        migrations.AlterField(
            model_name='mascotas',
            name='titulo',
            field=models.CharField(max_length=30, verbose_name='Titulo'),
        ),
    ]