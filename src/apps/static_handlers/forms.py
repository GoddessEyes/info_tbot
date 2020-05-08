from django import forms
from emoji_picker.widgets import EmojiPickerTextareaAdmin, EmojiPickerTextInput

from apps.static_handlers.models import StaticContentHandler


class StaticContentHandlerEmodjiFieldForm(forms.ModelForm):
    text = forms.CharField(widget=EmojiPickerTextareaAdmin)
    handler_name = forms.CharField(widget=EmojiPickerTextInput)
    handler_type = forms.ChoiceField(choices=StaticContentHandler.HANDLER_TYPE_CHOICES)

    class Meta:
        model = StaticContentHandler
        fields = ('text', 'handler_name', 'handler_type')
