from apps.core.generators import HandlerGenerator
from apps.core.handlers import StringHandler
from apps.static_handlers.models import StaticCommandHandler
from telegram import Update
from telegram.ext import CallbackContext, CommandHandler


class CommandStaticTextGenerator(HandlerGenerator):
    """Генерирует объекты-хендлеры для модели команд со статическим текстом."""

    model = StaticCommandHandler

    def __init__(self, text):
        self.text = text

    def __call__(self, update: Update, context: CallbackContext, *args, **kwargs):
        update.message.reply_text(self.text)

    @classmethod
    def init_handlers_for_tg(cls, dp=None):
        handlers = StaticCommandHandler.objects.filter(
            handler_type=StaticCommandHandler.COMMAND
        )
        for handler in handlers:
            dp.add_handler(CommandHandler(handler.handler_name, cls(handler.text)))


class MessageStaticTextGenerator(HandlerGenerator):
    """Генерирует объекты-хендлеры для модели сообщений со статическим текстом."""

    def __init__(self, text):
        self.text = text

    def __call__(self, update: Update, context: CallbackContext, *args, **kwargs):
        update.message.reply_text(self.text)

    @classmethod
    def init_handlers_for_tg(cls, dp=None):
        handlers = StaticCommandHandler.objects.filter(
            handler_type=StaticCommandHandler.TEXT
        )
        for handler in handlers:
            dp.add_handler(StringHandler(string=handler.handler_name, callback=cls(handler.text)))
