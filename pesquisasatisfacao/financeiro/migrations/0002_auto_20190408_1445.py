# Generated by Django 2.2 on 2019-04-08 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('financeiro', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pagamento',
            old_name='valor',
            new_name='valor_pago',
        ),
    ]
