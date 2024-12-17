# Generated by Django 4.2.17 on 2024-12-17 02:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acompanhamentos',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Adicionais',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=30)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=5)),
                ('unidade_medida', models.IntegerField(choices=[(0, 'KILO'), (1, 'LITRO'), (2, 'GRAMA'), (3, 'ML')])),
            ],
        ),
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Contas',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('valor_total', models.DecimalField(decimal_places=2, max_digits=5)),
                ('data', models.DateField()),
                ('hora_abertura', models.TimeField()),
                ('hora_fechamento', models.TimeField()),
                ('status', models.IntegerField(choices=[(0, 'ABERTA'), (1, 'FECHADA')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Funcionarios',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
                ('cargo', models.CharField(max_length=15)),
                ('data_admissao', models.DateField()),
                ('data_nascimento', models.DateField()),
                ('email', models.CharField(max_length=30)),
                ('status', models.IntegerField(choices=[(0, 'INATIVO'), (1, 'ATIVO')], default=0)),
                ('senha', models.CharField(max_length=30)),
                ('permissao', models.IntegerField(choices=[(0, 'ADMIN'), (1, 'GARCOM'), (2, 'CHAPEIRO'), (3, 'MONTADOR')], default=1)),
                ('salario', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Mesas',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('numero', models.IntegerField()),
                ('status', models.IntegerField(choices=[(0, 'DISPONIVEL'), (1, 'INDISPONIVEL'), (2, 'RESERVADA')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Produtos',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=30)),
                ('unidade_medida', models.IntegerField(choices=[(0, 'KILO'), (1, 'LITRO'), (2, 'GRAMA'), (3, 'ML')])),
                ('quantidade', models.IntegerField()),
                ('data_validade', models.DateField()),
                ('custo_unitario', models.DecimalField(decimal_places=2, max_digits=5)),
                ('status', models.IntegerField(choices=[(0, 'DISPONIVEL'), (1, 'INDISPONIVEL')], default=0)),
                ('preco_venda', models.DecimalField(decimal_places=2, max_digits=5)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.categorias')),
            ],
        ),
        migrations.CreateModel(
            name='Pratos',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=30)),
                ('preco_venda', models.DecimalField(decimal_places=2, max_digits=5)),
                ('status', models.IntegerField(choices=[(0, 'DISPONIVEL'), (1, 'INDISPONIVEL')], default=0)),
                ('acompanhamento', models.ManyToManyField(to='orders.acompanhamentos')),
            ],
        ),
        migrations.CreateModel(
            name='Pedidos',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('status', models.IntegerField(choices=[(0, 'NA_FILA'), (1, 'PREPARANDO'), (2, 'PRONTO')], default=0)),
                ('data', models.DateField()),
                ('hora_abertura', models.TimeField()),
                ('hora_fechamento', models.TimeField()),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.funcionarios')),
                ('mesa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.mesas')),
            ],
        ),
        migrations.CreateModel(
            name='Pagamentos',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('metodo', models.IntegerField(choices=[(0, 'DINHEIRO'), (1, 'CREDITO'), (2, 'DEBITO'), (3, 'PIX')], default=0)),
                ('valor_pago', models.DecimalField(decimal_places=2, max_digits=5)),
                ('conta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.contas')),
            ],
        ),
        migrations.CreateModel(
            name='MovimentacaoProdutos',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('tipo', models.IntegerField(choices=[(0, 'ENTRADA'), (1, 'SAIDA')])),
                ('quantidade', models.IntegerField()),
                ('data', models.DateField()),
                ('hora', models.TimeField()),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.funcionarios')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.produtos')),
            ],
        ),
        migrations.CreateModel(
            name='ItemPratos',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('quantidade_por_porcao', models.DecimalField(decimal_places=2, max_digits=5)),
                ('prato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.pratos')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.produtos')),
            ],
        ),
        migrations.CreateModel(
            name='ItemPedidos',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('quantidade', models.IntegerField()),
                ('preco_unitario', models.DecimalField(decimal_places=2, max_digits=5)),
                ('acompanhamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.acompanhamentos')),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.pedidos')),
            ],
        ),
        migrations.CreateModel(
            name='ItemAdicionais',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('preco_unitario', models.DecimalField(decimal_places=2, max_digits=5)),
                ('adicional', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.adicionais')),
                ('item_pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.itempedidos')),
            ],
        ),
        migrations.CreateModel(
            name='HistoricoCustoProdutos',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('preco_custo', models.DecimalField(decimal_places=2, max_digits=5)),
                ('data', models.DateField()),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.produtos')),
            ],
        ),
        migrations.AddField(
            model_name='contas',
            name='funcionario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.funcionarios'),
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
