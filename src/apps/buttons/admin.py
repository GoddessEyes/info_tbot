from apps.buttons.models import Button
from django.contrib import admin


@admin.register(Button)
class ButtonAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )
