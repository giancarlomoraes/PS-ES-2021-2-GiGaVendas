# Generated by Django 3.2.12 on 2022-02-09 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comercio', '0002_alter_cliente_cpf'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='complemento',
            field=models.CharField(default='teste', max_length=100),
            preserve_default=False,
        ),
    ]
