from telegram import Update
from telegram.ext import CallbackContext, CommandHandler

from apps.static_handlers.models import StaticContentHandler
from bot.core.generators import HandlerGenerator


class CommandStaticTextGenerator(HandlerGenerator):
    """Генерирует объекты-хендлеры для модели команд со статическим текстом."""

    def __init__(self, text):
        self.text = text

    def __call__(self, update: Update, context: CallbackContext, *args, **kwargs):
        update.message.reply_text(self.text)

    @classmethod
    def self_load(cls, dp=None):
        handlers = StaticContentHandler.objects.filter(
            handler_type=StaticContentHandler.COMMAND
        )
        for handler in handlers:
            dp.add_handler(CommandHandler(handler.handler_name, cls(handler.text)))
