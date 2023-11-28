from django.contrib import admin

from .models import DealerPrice


@admin.register(DealerPrice)
class DealerPriceAdmin(admin.ModelAdmin):
    list_display = ("id", "date", "key", "price", "name")
    search_fields = ("name", "key")
    empty_value_display = "-пусто-"
