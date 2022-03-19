from django.db import models
from products_category.models import Product


class Report(models.Model):
    """Модель отзывов"""

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name='К какому продукту отзыв'
    )

    text = models.TextField(
        verbose_name='Текст отзыва',
        null=True,
        blank=True,
    )

    rating = models.PositiveIntegerField(
        verbose_name='Рейтинг'
    )
