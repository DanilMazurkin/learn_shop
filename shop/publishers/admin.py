from django.contrib import admin
from publishers.models import Publisher


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    ...
