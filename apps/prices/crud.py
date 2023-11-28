from django.db.models import QuerySet

from .models import DealerPrice


def list_prices() -> QuerySet[DealerPrice]:
    return DealerPrice.objects.select_related(
        "key", "key__dealer", "key__product"
    )
