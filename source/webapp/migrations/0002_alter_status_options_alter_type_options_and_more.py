# Generated by Django 4.0.1 on 2022-01-12 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name': 'Статус', 'verbose_name_plural': 'Статусы'},
        ),
        migrations.AlterModelOptions(
            name='type',
            options={'verbose_name': 'Тип', 'verbose_name_plural': 'Типы'},
        ),
        migrations.AlterModelTable(
            name='status',
            table='status',
        ),
        migrations.AlterModelTable(
            name='type',
            table='type',
        ),
    ]