# Generated by Django 3.2.12 on 2022-02-11 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comercio', '0014_auto_20220210_1938'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='descontado_estoque',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='venda',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='itens_venda', to='comercio.venda'),
        ),
    ]