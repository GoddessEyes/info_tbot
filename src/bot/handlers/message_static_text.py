from telegram import Update
from telegram.ext import CallbackContext

from apps.static_handlers.models import StaticContentHandler
from bot.core.generators import HandlerGenerator
from bot.core.handlers import StringHandler


class MessageStaticTextGenerator(HandlerGenerator):
    """Генерирует объекты-хендлеры для модели сообщений со статическим текстом."""

    def __init__(self, text):
        self.text = text

    def __call__(self, update: Update, context: CallbackContext, *args, **kwargs):
        update.message.reply_text(self.text)

    @classmethod
    def self_load(cls, dp=None):
        handlers = StaticContentHandler.objects.filter(
            handler_type=StaticContentHandler.TEXT
        )
        for handler in handlers:
            dp.add_handler(StringHandler(string=handler.handler_name, callback=cls(handler.text)))
