# Generated by Django 4.2.17 on 2024-12-28 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_produtos_unidade_medida'),
        ('dishes', '0002_pratos_categoria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itempratos',
            name='prato',
        ),
        migrations.RemoveField(
            model_name='itempratos',
            name='produto',
        ),
        migrations.AddField(
            model_name='itempratos',
            name='prato',
            field=models.ManyToManyField(to='dishes.pratos'),
        ),
        migrations.AddField(
            model_name='itempratos',
            name='produto',
            field=models.ManyToManyField(to='products.produtos'),
        ),
    ]