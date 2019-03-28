# Generated by Django 2.1.3 on 2019-03-22 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20190317_1130'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.ManyToManyField(to='core.Client', verbose_name='Clientes')),
                ('products', models.ManyToManyField(to='core.Product', verbose_name='Produtos')),
            ],
            options={
                'verbose_name': 'Venda',
                'verbose_name_plural': 'Vendas',
            },
        ),
    ]