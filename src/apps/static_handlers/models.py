from django.db import models
from solo.models import SingletonModel


class StaticContentHandler(models.Model):
    COMMAND = 0
    TEXT = 1
    HANDLER_TYPE_CHOICES = (
        (COMMAND, 'Команда'),
        (TEXT, 'Текст'),
    )
    handler_type = models.PositiveSmallIntegerField(
        verbose_name='Тип обработчика',
        choices=HANDLER_TYPE_CHOICES,
        blank=False,
        null=False,
    )
    handler_name = models.CharField(
        verbose_name='Параметр обработчика',
        help_text='Сообщение на которое должен реагировать обработчик',
        max_length=255,
        blank=False,
        null=False,
    )
    text = models.TextField(
        verbose_name='Текст ответа',
        help_text='Текст который отправит бот в ответ на вызов `параметра обработчика`',
        blank=False,
        null=False,
    )

    def __str__(self):
        return f'{self.handler_name} {self.HANDLER_TYPE_CHOICES[self.handler_type][1]}'

    class Meta:
        verbose_name = 'Статический текстовый обработчик'
        verbose_name_plural = 'Статические текстовые обработчики'


class StartBotHandler(SingletonModel):
    handler_name = models.CharField(
        verbose_name='Параметр обработчика',
        help_text='Сообщение на которое должен реагировать обработчик',
        max_length=255,
        blank=False,
        null=False,
        default='start'
    )
    text = models.TextField(
        verbose_name='Текст ответа',
        help_text='Текст который отправит бот в ответ на вызов `параметра обработчика`',
        blank=False,
        null=False,
        default='Hello',
    )
    keyboard = models.ManyToManyField(
        verbose_name='Клавиатура',
        to='buttons.Button',
        help_text='Клавиатура возвращаемая при команде /start'
    )

    class Meta:
        verbose_name = 'Стартовый обработчик'

    def __str__(self) -> str:
        return self.handler_name
