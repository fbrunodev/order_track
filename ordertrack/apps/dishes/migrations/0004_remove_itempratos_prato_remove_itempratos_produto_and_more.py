# Generated by Django 4.2.17 on 2024-12-28 23:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_produtos_unidade_medida'),
        ('dishes', '0003_remove_itempratos_prato_remove_itempratos_produto_and_more'),
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
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='dishes.pratos'),
        ),
        migrations.AddField(
            model_name='itempratos',
            name='produto',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='products.produtos'),
        ),
    ]
