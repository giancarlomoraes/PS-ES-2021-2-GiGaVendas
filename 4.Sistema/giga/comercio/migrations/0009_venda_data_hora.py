# Generated by Django 3.2.12 on 2022-02-10 17:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comercio', '0008_alter_venda_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='venda',
            name='data_hora',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
