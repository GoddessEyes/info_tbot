from telegram.ext import MessageHandler

from bot.core.filters import StringFilter


class StringHandler(MessageHandler):
    def __init__(self,
                 filters=None,
                 callback=None,
                 pass_update_queue=False,
                 pass_job_queue=False,
                 pass_user_data=False,
                 pass_chat_data=False,
                 message_updates=None,
                 channel_post_updates=None,
                 edited_updates=None,
                 string=None):
        if callback is None:
            raise RuntimeError('Parameter callback for StringHandler required!')
        if string and not filters:
            filters = StringFilter.button(string)
        super().__init__(
            filters,
            callback,
            pass_update_queue=False,
            pass_job_queue=False,
            pass_user_data=False,
            pass_chat_data=False,
            message_updates=None,
            channel_post_updates=None,
            edited_updates=None,
        )
