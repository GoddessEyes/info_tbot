from django.contrib import admin

from apps.buttons.models import Button


@admin.register(Button)
class ButtonAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )
