from django_filters import rest_framework as filters
from django.db.models import Q

from apps.dealers.models import DealerKey


class DealerKeyFilter(filters.FilterSet):
    article = filters.CharFilter(method="get_article")
    status = filters.CharFilter(method="get_status")

    class Meta:
        model = DealerKey
        fields = ("article", "dealer_id", "status")

    def get_article(self, queryset, name, value):
        """Поиск по вхождению."""
        if value:
            return queryset.filter(
                Q(key__icontains=value) | Q(name__icontains=value)
            )
        return queryset

    def get_status(self, queryset, name, value):
        """Поиск по статусу."""
        if not value:
            return queryset
        if value in ["-", "0"]:
            return queryset.filter(status=value)
        return queryset.exclude(status__in=["-", "0"])
