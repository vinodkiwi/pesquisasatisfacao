# Generated by Django 2.1.3 on 2019-03-12 17:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feriado',
            options={'verbose_name': 'Feriado/Sábado compensado', 'verbose_name_plural': 'Feriados/Sábados compensados'},
        ),
        migrations.AddField(
            model_name='feriado',
            name='users',
            field=models.ManyToManyField(related_name='users', to=settings.AUTH_USER_MODEL, verbose_name='Usuário'),
        ),
    ]
