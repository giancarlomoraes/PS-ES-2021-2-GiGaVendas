# Generated by Django 3.2.12 on 2022-02-10 13:12

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('comercio', '0003_cliente_complemento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cpf',
            field=models.CharField(max_length=14, validators=[django.core.validators.RegexValidator(code='nomatch', message='CPF Inválido', regex='^\\d{3}\\.\\d{3}\\.\\d{3}\\-\\d{2}$')]),
        ),
        migrations.CreateModel(
            name='FuncaoColaborador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, unique=True)),
                ('permissoes', models.ManyToManyField(blank=True, related_name='permissoes_funcao_colaborador', to='auth.Permission', verbose_name='Permissões')),
            ],
            options={
                'verbose_name': 'Função',
                'verbose_name_plural': 'Funções',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Colaborador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bairro', models.CharField(max_length=100)),
                ('cidade', models.CharField(max_length=100)),
                ('complemento', models.CharField(max_length=100)),
                ('rua', models.CharField(max_length=100)),
                ('numero', models.IntegerField()),
                ('telefone', models.CharField(blank=True, max_length=15, null=True, validators=[django.core.validators.RegexValidator(code='nomatch', message='Telefone Inválido', regex='^.{15}$')])),
                ('cpf', models.CharField(max_length=14, validators=[django.core.validators.RegexValidator(code='nomatch', message='CPF Inválido', regex='^\\d{3}\\.\\d{3}\\.\\d{3}\\-\\d{2}$')])),
                ('salario', models.FloatField()),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='colaborador_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Colaborador',
                'verbose_name_plural': 'Colaboradores',
                'ordering': ['user'],
            },
        ),
    ]
