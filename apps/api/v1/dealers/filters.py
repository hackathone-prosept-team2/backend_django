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
