# Generated by Django 2.1.2 on 2018-10-23 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20181023_1242'),
    ]

    operations = [
        migrations.AddField(
            model_name='projeto',
            name='data_vencimento',
            field=models.DateField(null=True, verbose_name='Concluir em:'),
        ),
    ]
