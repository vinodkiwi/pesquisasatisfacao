# Generated by Django 2.2 on 2019-04-07 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0009_remove_client_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_vencimento', models.DateField()),
                ('data_pagamento', models.DateField(blank=True, null=True)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=15)),
                ('operacao', models.CharField(blank=True, choices=[('d', 'Debito'), ('c', 'Credito')], default='d', max_length=1)),
                ('status', models.CharField(blank=True, choices=[('a', 'Aberta'), ('p', 'Paga')], default='a', max_length=1)),
                ('descricao', models.TextField(blank=True)),
            ],
            options={
                'ordering': ('-data_vencimento', 'valor'),
            },
        ),
        migrations.CreateModel(
            name='Historico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=50)),
                ('operacao', models.CharField(blank=True, choices=[('d', 'Debito'), ('c', 'Credito')], default='d', max_length=1)),
            ],
            options={
                'ordering': ('descricao',),
            },
        ),
        migrations.CreateModel(
            name='Pagamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_pagamento', models.DateField()),
                ('valor', models.DecimalField(decimal_places=2, max_digits=15)),
                ('conta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conta_pagamento', to='financeiro.Conta')),
            ],
            options={
                'verbose_name': 'Venda Detalhe',
                'verbose_name_plural': 'Vendas Detalhe',
            },
        ),
        migrations.AddField(
            model_name='conta',
            name='historico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='historico_conta', to='financeiro.Historico'),
        ),
        migrations.AddField(
            model_name='conta',
            name='pessoa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_conta', to='core.Client'),
        ),
    ]
