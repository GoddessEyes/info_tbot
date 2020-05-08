from typing import List

from telegram import KeyboardButton, Update
from telegram.ext import CallbackContext, CommandHandler

from apps.static_handlers.models import StartBotHandler
from bot.core.generators import HandlerGenerator
from bot.keyboards.common import build_three_column_menu


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
    def self_load(cls, dp=None) -> None:
        handler = StartBotHandler.get_solo()
        buttons_text = handler.keyboard.values_list('title', flat=True)
        keyboard = cls.init_keyboards(buttons_text)
        dp.add_handler(CommandHandler(
            handler.handler_name, cls(keyboard=keyboard, text=handler.text)
        ))
