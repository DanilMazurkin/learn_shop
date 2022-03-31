from django.db import models


class Feedback(models.Model):
    """Модель feedback
    :param user_name: имя пользователя
    """
    user_name = models.CharField(
        max_length=50,
        verbose_name='Имя пользователя',
    )

    email = models.EmailField(verbose_name='Email')

    text = models.TextField(
        verbose_name='Ваш отзыв'
    )

    def __str__(self):
        return f'{self.text[0:100]}'

