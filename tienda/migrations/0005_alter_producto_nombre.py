# Generated by Django 5.1.4 on 2025-01-09 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0004_alter_producto_categoria_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='nombre',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
