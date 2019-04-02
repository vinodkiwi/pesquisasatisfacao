# Generated by Django 2.1.3 on 2019-03-21 01:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_auto_20190319_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atendimento',
            name='feedback',
            field=models.TextField(blank=True, null=True, verbose_name='Parecer Anterior'),
        ),
        migrations.AlterField(
            model_name='atendimento',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Produtos', to='core.Product', verbose_name='Produto'),
        ),
        migrations.AlterField(
            model_name='atendimento',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='TipoDeAtendimento', to='crm.Typeofservice', verbose_name='Tipo de atendimento'),
        ),
    ]
