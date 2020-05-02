from django.core.exceptions import ValidationError


def validate_tgusername(username):
    if username.startswith('@') and ' ' not in username:
        return True
    raise ValidationError(
        u'Имя пользователя должно начинаться с `@` и не содержать пробелов.'
    )
