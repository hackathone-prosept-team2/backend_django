from django.db.models import Q
from django_filters import rest_framework as filters

from apps.dealers.models import DealerKey
from config.constants import MATCH_NUMBER, KeyStatus


class DealerKeyFilter(filters.FilterSet):
    """Фильтр для ключей дилеров."""

    article = filters.CharFilter(method="get_article")
    status = filters.CharFilter(method="get_status")

    class Meta:
        model = DealerKey
        fields = ("article", "dealer_id", "status")

    def get_article(self, queryset, name, value):
        """Поиск по вхождению значения в артикул или наименование."""
        if value:
            return queryset.filter(
                Q(key__icontains=value) | Q(name__icontains=value)
            )
        return queryset

    def get_status(self, queryset, name, value):
        """Поиск по статусу."""
        if value:
            if value == KeyStatus.FOUND:
                return queryset.filter(product_id__isnull=False)
            if value == KeyStatus.DECLINED:
                return queryset.filter(declined=MATCH_NUMBER)
            if value == KeyStatus.CHECK:
                return queryset.filter(
                    product_id__isnull=True, declined__lt=MATCH_NUMBER
                )
        return queryset


class DealerKeyExportFilter(filters.FilterSet):
    new = filters.BooleanFilter(method="get_new")
    since = filters.DateFilter(method="get_since")
    date = filters.DateFilter(method="get_date")

    class Meta:
        model = DealerKey
        fields = ("new", "since", "date")

    def get_new(self, queryset, name, value):
        """Фильтр по is_provided - ключи, которых не было в начальном csv."""
        if value:
            return queryset.filter(is_provided=False)
        return queryset

    def get_since(self, queryset, name, value):
        """Фильтр по дате присвоения продукта - начиная с даты."""
        if value:
            return queryset.filter(edited_at__gte=value)
        return queryset

    def get_date(self, queryset, name, value):
        """Фильтр по дате присвоения продукта - в дату."""
        if value:
            return queryset.filter(edited_at=value)
        return queryset
