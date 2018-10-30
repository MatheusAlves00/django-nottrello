# Generated by Django 2.1.2 on 2018-10-24 14:33

import app.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20181024_0306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projeto',
            name='detalhes',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='usuario',
            field=models.ForeignKey(default=app.models.Usuario, on_delete=django.db.models.deletion.CASCADE, to='app.Usuario'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(max_length=50),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nome',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='senha',
            field=models.CharField(max_length=50),
        ),
    ]