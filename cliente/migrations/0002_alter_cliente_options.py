# Generated by Django 5.0.3 on 2024-03-27 22:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cliente',
            options={'ordering': ['-data_cadastro'], 'verbose_name': 'Cadastro de cliente', 'verbose_name_plural': 'Cadastro de clientes'},
        ),
    ]