# Generated by Django 4.2.17 on 2025-01-03 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_adicionais_unidade_medida'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedidos',
            name='hora_fechamento',
            field=models.TimeField(null=True),
        ),
    ]