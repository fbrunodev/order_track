# Generated by Django 4.2.17 on 2024-12-18 02:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionarios',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
                ('cargo', models.CharField(max_length=15)),
                ('data_admissao', models.DateField()),
                ('data_nascimento', models.DateField()),
                ('status', models.IntegerField(choices=[(0, 'INATIVO'), (1, 'ATIVO')], default=0)),
                ('salario', models.DecimalField(decimal_places=2, max_digits=5)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='employee', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]