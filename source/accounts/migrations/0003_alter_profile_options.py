# Generated by Django 4.0.1 on 2022-02-20 22:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_create_profile_for_users'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'permissions': [('can_look_list_of_users', 'Может просмотреть страницу со списком пользователей')], 'verbose_name': 'Профиль', 'verbose_name_plural': 'Профили'},
        ),
    ]