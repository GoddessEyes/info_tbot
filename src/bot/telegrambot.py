import logging

from django_telegrambot.apps import DjangoTelegramBot

from bot.handlers.handlers_loader import HandlerLoader


logger = logging.getLogger(__name__)


def main():
    logger.info("Loading handlers for telegram bot")
    bot_instance = DjangoTelegramBot.dispatcher
    loader = HandlerLoader(bot_instance=bot_instance)
    loader()
