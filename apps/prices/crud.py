from django.db.models import QuerySet
from django.shortcuts import get_object_or_404

from apps.dealers.models import DealerKey

from .models import DealerPrice


def list_key_prices(key_pk: int) -> QuerySet[DealerPrice]:
    qs = DealerKey.objects.prefetch_related("prices")
    key = get_object_or_404(qs, pk=key_pk)
    return key.prices.all()


def list_prices() -> QuerySet[DealerPrice]:
    return DealerPrice.objects.select_related(
        "key", "key__dealer", "key__product"
    )
