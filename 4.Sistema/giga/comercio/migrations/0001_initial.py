# Generated by Django 3.2.12 on 2022-02-09 18:41

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bairro', models.CharField(max_length=100)),
                ('cidade', models.CharField(max_length=100)),
                ('rua', models.CharField(max_length=100)),
                ('numero', models.IntegerField()),
                ('telefone', models.CharField(blank=True, max_length=15, null=True, validators=[django.core.validators.RegexValidator(code='nomatch', message='Telefone Inválido', regex='^.{15}$')])),
                ('cpf', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(code='nomatch', message='CPF Inválido', regex='/^\\d{3}\\.\\d{3}\\.\\d{3}\\-\\d{2}$/')])),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cliente_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'ordering': ['user'],
            },
        ),
    ]