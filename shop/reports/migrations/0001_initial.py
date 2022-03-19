# Generated by Django 4.0.2 on 2022-03-19 02:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products_category', '0005_alter_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Текст отзыва')),
                ('rating', models.PositiveIntegerField(verbose_name='Рейтинг')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products_category.product')),
            ],
        ),
    ]