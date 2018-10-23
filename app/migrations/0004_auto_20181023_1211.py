# Generated by Django 2.1.2 on 2018-10-23 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20181019_2218'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Status',
            },
        ),
        migrations.RemoveField(
            model_name='projeto',
            name='tarefas',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='projetos',
        ),
        migrations.AddField(
            model_name='projeto',
            name='usuario',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='app.Usuario'),
        ),
        migrations.AddField(
            model_name='tarefa',
            name='data_criacao',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='tarefa',
            name='data_vencimento',
            field=models.DateField(null=True, verbose_name='Data de Vencimento'),
        ),
        migrations.AddField(
            model_name='tarefa',
            name='projeto',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='app.Projeto'),
        ),
        migrations.AlterField(
            model_name='tarefa',
            name='descricao',
            field=models.CharField(max_length=200, verbose_name='Descrição'),
        ),
        migrations.AddField(
            model_name='tarefa',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Status'),
        ),
    ]
