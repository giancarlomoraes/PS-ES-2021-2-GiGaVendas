# Generated by Django 3.2.12 on 2022-02-10 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comercio', '0004_auto_20220210_1012'),
    ]

    operations = [
        migrations.AddField(
            model_name='colaborador',
            name='funcao',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='funcao_colaborador', to='comercio.funcaocolaborador'),
        ),
    ]
