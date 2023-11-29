from django.db.models import QuerySet

from apps.dealers.models import DealerKey

from .models import DealerPrice


def list_key_prices(dealer_key: DealerKey) -> QuerySet[DealerPrice]:
    return dealer_key.prices.only("date", "product_url", "name", "price")


def list_prices() -> QuerySet[DealerPrice]:
    return DealerPrice.objects.select_related(
        "key", "key__dealer", "key__product"
    )
