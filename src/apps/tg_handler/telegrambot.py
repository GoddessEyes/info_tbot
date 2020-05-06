import logging
import os
import sys
from threading import Thread

from apps.management.models import CustomUser
from apps.tg_handler.generators import CommandStaticTextGenerator, MessageStaticTextGenerator
from django_telegrambot.apps import DjangoTelegramBot
from telegram.ext import CommandHandler


logger = logging.getLogger(__name__)


def main():
    logger.info("Loading handlers for telegram bot")
    dp = DjangoTelegramBot.dispatcher
    CommandStaticTextGenerator.init_handlers_for_tg(dp)
    MessageStaticTextGenerator.init_handlers_for_tg(dp)

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
