# Generated by Django 4.0.2 on 2022-03-19 02:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products_category', '0005_alter_product_price'),
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products_category.product', verbose_name='К какому продукту отзыв'),
        ),
    ]
