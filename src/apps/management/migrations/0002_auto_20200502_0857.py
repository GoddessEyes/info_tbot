# Generated by Django 3.0.5 on 2020-05-02 08:57

import django.contrib.auth.validators
from django.db import migrations, models

import apps.management.validators


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='bot_manager',
            field=models.BooleanField(default=False, help_text='При выборе этой опциии пользователь сможет перезагружать бота командой `/restart`.', verbose_name='Управление ботом'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Никнейм в телеграм, должен начинаться с `@` и не содержать пробелов.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator(), apps.management.validators.validate_tgusername], verbose_name='username'),
        ),
    ]
