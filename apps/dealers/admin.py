from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest

from .crud import list_keys_in_admin
from .models import Dealer, DealerKey, Match


class ProductFilter(admin.SimpleListFilter):
    title = "has product"
    parameter_name = "has_product"

    def lookups(self, request, model_admin):
        return [
            ("Yes", "продукт назначен"),
            ("No", "продукт не назначен"),
        ]

    def queryset(self, request, queryset):
        value = self.value()
        if value == "Yes":
            return queryset.filter(product_id__isnull=False)
        if value == "No":
            qs = queryset.filter(product_id__isnull=True)
            return qs


@admin.register(Dealer)
class DealerAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    empty_value_display = "-пусто-"


class MatchInline(admin.TabularInline):
    model = Match
    extra = 0


@admin.register(DealerKey)
class DealerKeyAdmin(admin.ModelAdmin):
    readonly_fields = ("name",)
    fields = ("key", "name", "dealer", "product")
    inlines = [MatchInline]
    list_display = ("id", "key", "name", "dealer", "product")
    list_filter = (ProductFilter,)
    empty_value_display = "-пусто-"

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return list_keys_in_admin()

    def name(self, obj):
        return obj.name
