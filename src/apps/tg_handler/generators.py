from typing import List

from apps.core.generators import HandlerGenerator
from apps.core.handlers import StringHandler
from apps.static_handlers.models import StartBotHandler, StaticContentHandler
from apps.tg_handler.keyboard.common import build_three_column_menu
from telegram import KeyboardButton, Update
from telegram.ext import CallbackContext, CommandHandler


class StartBotHandlerGenerator(HandlerGenerator):
    """Обработчик старта бота."""

    def __init__(self, keyboard, text):
        self.keyboard = keyboard
        self.text = text

    def __call__(self, update: Update, context: CallbackContext, *args, **kwargs):
        update.message.reply_text(self.text, reply_markup=self.keyboard)

    @staticmethod
    def init_keyboards(buttons_text: List[str]):
        buttons = [KeyboardButton(item) for item in buttons_text]
        return build_three_column_menu(buttons)

    @classmethod
    def init_handlers_for_tg(cls, dp=None) -> None:
        handler = StartBotHandler.get_solo()
        buttons_text = handler.keyboard.values_list('title', flat=True)
        keyboard = cls.init_keyboards(buttons_text)
        dp.add_handler(CommandHandler(
            handler.handler_name, cls(keyboard=keyboard, text=handler.text)
        ))


class CommandStaticTextGenerator(HandlerGenerator):
    """Генерирует объекты-хендлеры для модели команд со статическим текстом."""

    def __init__(self, text):
        self.text = text

    def __call__(self, update: Update, context: CallbackContext, *args, **kwargs):
        update.message.reply_text(self.text)

    @classmethod
    def init_handlers_for_tg(cls, dp=None):
        handlers = StaticContentHandler.objects.filter(
            handler_type=StaticContentHandler.COMMAND
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
        handlers = StaticContentHandler.objects.filter(
            handler_type=StaticContentHandler.TEXT
        )
        for handler in handlers:
            dp.add_handler(StringHandler(string=handler.handler_name, callback=cls(handler.text)))
