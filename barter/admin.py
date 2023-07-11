from django.contrib import admin

from barter.models import ItemModel


@admin.register(ItemModel)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'place')
