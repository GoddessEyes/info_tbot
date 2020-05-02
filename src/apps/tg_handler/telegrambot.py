import logging
from threading import Thread

from django_telegrambot.apps import DjangoTelegramBot
from telegram import Update
from telegram.ext import CallbackContext, CommandHandler, Filters
import os
import sys
from apps.management.models import CustomUser

logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext):
    update.message.bot.sendMessage(update.message.chat_id, text='Hi!')


def main():
    logger.info("Loading handlers for telegram bot")
    dp = DjangoTelegramBot.dispatcher
    dp.add_handler(CommandHandler("start", start))

    def stop_and_restart():
        """Gracefully stop the Updater and replace the current process with a new one"""
        dp.stop()
        os.execl(sys.executable, sys.executable, *sys.argv)

    def restart(update, context):
        update.message.reply_text('Bot is restarting...')
        Thread(target=stop_and_restart).start()

    dp.add_handler(
        CommandHandler('r', restart, filters=CustomUser.get_tgfilters_managers_username())
    )
