# Generated by Django 4.2.17 on 2024-12-28 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_movimentacaoprodutos_produto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtos',
            name='unidade_medida',
            field=models.IntegerField(choices=[(0, 'KILO'), (1, 'LITRO'), (2, 'GRAMA'), (3, 'ML'), (4, 'UNIDADE')]),
        ),
    ]
