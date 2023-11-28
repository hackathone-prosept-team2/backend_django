from django.contrib import admin

from .models import Dealer, DealerKey


@admin.register(Dealer)
class DealerAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    empty_value_display = "-пусто-"


@admin.register(DealerKey)
class DealerKeyAdmin(admin.ModelAdmin):
    list_display = ("id", "key", "dealer")
    empty_value_display = "-пусто-"
