from django.contrib import admin
from solo.admin import SingletonModelAdmin

from apps.static_handlers.forms import StaticContentHandlerEmodjiFieldForm
from apps.static_handlers.models import StartBotHandler, StaticContentHandler


@admin.register(StaticContentHandler)
class StaticCommandHandlerAdmin(admin.ModelAdmin):
    list_display = (
        'handler_name',
        'handler_type',
        'text'
    )

    form = StaticContentHandlerEmodjiFieldForm


@admin.register(StartBotHandler)
class StartBotHandlerAdmin(SingletonModelAdmin):
    list_display = (
        'handler_name',
    )
