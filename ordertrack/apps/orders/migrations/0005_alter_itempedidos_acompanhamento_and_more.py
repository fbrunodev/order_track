# Generated by Django 4.2.17 on 2025-01-04 23:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_alter_pedidos_data_alter_pedidos_funcionario_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itempedidos',
            name='acompanhamento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.acompanhamentos'),
        ),
        migrations.AlterField(
            model_name='itempedidos',
            name='pedido',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.pedidos'),
        ),
        migrations.AlterField(
            model_name='itempedidos',
            name='preco_unitario',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='itempedidos',
            name='quantidade',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='status',
            field=models.IntegerField(choices=[(0, 'NA_FILA'), (1, 'PREPARANDO'), (2, 'PRONTO'), (3, 'FECHADO')], default=0),
        ),
    ]
