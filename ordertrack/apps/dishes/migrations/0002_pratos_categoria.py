# Generated by Django 4.2.17 on 2024-12-27 00:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_movimentacaoprodutos_produto_and_more'),
        ('dishes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pratos',
            name='categoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.categorias'),
        ),
    ]
