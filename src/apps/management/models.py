from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from telegram.ext import Filters
from django.utils.translation import gettext_lazy as _

from apps.management.validators import validate_tgusername


class CustomUser(AbstractUser):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Никнейм в телеграм, должен начинаться с `@` и не содержать пробелов.'),
        validators=(username_validator, validate_tgusername),
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    bot_manager = models.BooleanField(
        verbose_name='Управление ботом',
        default=False,
        help_text=(
            'При выборе этой опциии пользователь сможет перезагружать бота командой `/restart`.'
        )
    )

    @classmethod
    def get_all_bot_managers(cls):
        return cls.objects.filter(
            bot_manager=True
        ).values_list('username', flat=True)

    @classmethod
    def get_tgfilters_managers_username(cls):
        return Filters.user(username=cls.get_all_bot_managers())
