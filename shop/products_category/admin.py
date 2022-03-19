from django.contrib import admin
from .models import Product
from .models import Category
from .models import ProductImage


class InlineImageAdmin(admin.TabularInline):
    model = ProductImage


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Регистрация модели с продуктами."""
    list_display = ('name', 'price', 'description', )
    fields = ('name', 'price', 'get_name_length', 'description', )
    readonly_fields = ('get_name_length', )
    inlines = (InlineImageAdmin, )

    def get_name_length(self, obj):
        return len(obj.name)

    get_name_length.short_description = 'Длина имени товара'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Представление категорий в админке."""
    ...
