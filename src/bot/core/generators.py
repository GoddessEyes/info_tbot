from abc import ABCMeta, abstractmethod

from telegram import Update
from telegram.ext import CallbackContext


class HandlerGenerator(metaclass=ABCMeta):
    """Базовый класс для всех динамических телеграм-хэндлэров."""

    @abstractmethod
    def __call__(self, update: Update, context: CallbackContext, *args, **kwargs):
        """Логика работы с телеграм API.
        Пример:
        update.message.reply_text(self.text)
        """
        raise NotImplementedError(
            'Handler must be callable and return `reply` or another telegram response'
        )

    @classmethod
    @abstractmethod
    def self_load(cls, dp=None) -> None:
        """Загрузка телеграм-хэндлэров.
        Пример:
        handlers = YourModel.objects.all()
        for handler in handlers:
            dp.add_handler(StringHandler(string=handler.handler_name, callback=cls(handler.text)))
        """

        raise NotImplementedError(
            'Implement your logic for load dynamic telegram handlers here.'
        )
