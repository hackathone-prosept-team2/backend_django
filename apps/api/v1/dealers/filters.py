from django_filters import rest_framework as filters
from django.db.models import Q

from apps.dealers.models import DealerKey
from config.constants import KeyStatus, MATCH_NUMBER


class DealerKeyFilter(filters.FilterSet):
    article = filters.CharFilter(method="get_article")
    status = filters.CharFilter(method="get_status")
    # similarity = filters.NumberFilter(method="get_similarity")

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
        if value == KeyStatus.FOUND:
            return queryset.filter(product_id__isnull=False)
        if value == KeyStatus.DECLINED:
            return queryset.filter(declined=MATCH_NUMBER)
        return queryset.filter(
            product_id__isnull=True, declined__lt=MATCH_NUMBER
        )

    # def get_similarity(self, queryset, name, value):
    #     """Поиск по показателю схожести."""
    #     if value:
    #         return queryset.filter(similarity__gte=value)
    #     return queryset
