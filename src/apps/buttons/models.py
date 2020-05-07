from django.db import models


class Button(models.Model):
    title = models.CharField(
        verbose_name='Тайтл клавиши',
        unique=True,
        blank=False,
        null=False,
        help_text='Кнопки для взаимодействия с ботом',
        max_length=255,
    )
    description = models.TextField(
        verbose_name='Описание клавиши',
        blank=False,
        null=False,
    )

    class Meta:
        verbose_name = 'Клавиша'
        verbose_name_plural = 'Клавиши'

    def __str__(self) -> str:
        return self.title
