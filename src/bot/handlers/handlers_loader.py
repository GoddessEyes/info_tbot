from bot.handlers.command_static_text import CommandStaticTextGenerator
from bot.handlers.message_static_text import MessageStaticTextGenerator
from bot.handlers.restart import RestartBotHandlerGenerator
from bot.handlers.start import StartBotHandlerGenerator


DYNAMIC_HANDLERS = {
    CommandStaticTextGenerator,
    MessageStaticTextGenerator,
}

TECHNICAL_HANDLER = {
    StartBotHandlerGenerator,
    RestartBotHandlerGenerator
}


class HandlerLoader:
    def __init__(self, bot_instance) -> None:
        self.handlers = TECHNICAL_HANDLER | DYNAMIC_HANDLERS
        self.bot_instance = bot_instance

    def __call__(self, *args, **kwargs) -> None:
        for handler in self.handlers:
            handler.self_load(self.bot_instance)
