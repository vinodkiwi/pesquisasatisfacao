# Generated by Django 2.1.3 on 2019-03-14 23:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20190313_1749'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='compensacao',
            options={'verbose_name': 'Dia compensado', 'verbose_name_plural': 'Dias compensados'},
        ),
        migrations.AlterModelOptions(
            name='feriado',
            options={'verbose_name': 'Feriado', 'verbose_name_plural': 'Feriados'},
        ),
    ]