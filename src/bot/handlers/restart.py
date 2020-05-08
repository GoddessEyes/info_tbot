import os
import sys
from threading import Thread

from telegram.ext import CommandHandler

from apps.management.models import CustomUser


class RestartBotHandlerGenerator:
    """Обработчик рестарта бота."""

    @classmethod
    def self_load(cls, dp=None) -> None:
        def stop_and_restart():
            dp.stop()
            os.execl(sys.executable, sys.executable, *sys.argv)

        def restart(update, context):
            update.message.reply_text('Bot is restarting...')
            Thread(target=stop_and_restart).start()

        try:
            dp.add_handler(
                CommandHandler(
                    'restart', restart, filters=CustomUser.get_tgfilters_managers_username()
                )
            )
        except ValueError:
            # Нет ни одного пользователя. Первый запуск бота или никому не назначены права.
            dp.add_handler(
                CommandHandler('restart', restart)
            )
