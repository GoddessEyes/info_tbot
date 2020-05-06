from apps.static_handlers.models import StaticCommandHandler
from django import forms
from django.contrib import admin
from emoji_picker.widgets import EmojiPickerTextareaAdmin


class EmodjiFieldForm(forms.ModelForm):
    text = forms.CharField(widget=EmojiPickerTextareaAdmin)
    handler_name = forms.CharField()
    handler_type = forms.ChoiceField(choices=StaticCommandHandler.HANDLER_TYPE_CHOICES)

    class Meta:
        model = StaticCommandHandler
        fields = ('text', 'handler_name', 'handler_type')


@admin.register(StaticCommandHandler)
class StaticCommandHandlerAdmin(admin.ModelAdmin):
    list_display = (
        'handler_name',
        'handler_type',
        'text'
    )

    form = EmodjiFieldForm
