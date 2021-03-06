# Generated by Django 3.2.12 on 2022-02-10 22:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comercio', '0013_auto_20220210_1602'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venda',
            name='item',
        ),
        migrations.AddField(
            model_name='item',
            name='venda',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='itens_vendavenda_item', to='comercio.venda'),
        ),
        migrations.AlterField(
            model_name='item',
            name='quantidade',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
