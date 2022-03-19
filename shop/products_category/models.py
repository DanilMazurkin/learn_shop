from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Имя категории',
    )

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    """Модель товара."""

    name = models.CharField(
        max_length=255,
        verbose_name='Name'
    )

    price = models.PositiveIntegerField(
        verbose_name='Price'
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
    )

    description = models.TextField(
        null=True,
        blank=True,
        verbose_name='Описание продукта'
    )

    def __str__(self):
        return f'{self.name}'
    

class ProductImage(models.Model):
    """Картинки для продуктов."""
    image_product = models.ImageField(
        upload_to='media/products/',
        null=True,
        blank=True,
    )

    product = models.ForeignKey(
        Product,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return f'{self.image_product}'

