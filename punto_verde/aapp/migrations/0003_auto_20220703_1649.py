# Generated by Django 3.2.3 on 2022-07-03 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aapp', '0002_alter_contenedorlleno_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id_empresa', models.AutoField(primary_key=True, serialize=False)),
                ('razon_social', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('pais', models.CharField(max_length=20)),
                ('region', models.CharField(max_length=20)),
                ('contacto', models.IntegerField()),
                ('correo', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'empresa',
                'managed': False,
            },
        ),
        migrations.RemoveField(
            model_name='factura',
            name='id_venta',
        ),
        migrations.DeleteModel(
            name='Boleta',
        ),
        migrations.DeleteModel(
            name='Compra',
        ),
        migrations.DeleteModel(
            name='Factura',
        ),
    ]
