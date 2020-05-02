import logging

from django_telegrambot.apps import DjangoTelegramBot
from telegram import Update
from telegram.ext import CallbackContext, CommandHandler


logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext):
    update.message.bot.sendMessage(update.message.chat_id, text='Hi!')


def main():
    logger.info("Loading handlers for telegram bot")
    dp = DjangoTelegramBot.dispatcher
    dp.add_handler(CommandHandler("start", start))
