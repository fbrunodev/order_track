# Generated by Django 4.2.17 on 2024-12-19 01:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orders', '0001_initial'),
        ('bills', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='contas',
            name='funcionario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='contas',
            name='mesa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.mesas'),
        ),
        migrations.AddField(
            model_name='contas',
            name='pedido',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='orders.pedidos'),
        ),
    ]
