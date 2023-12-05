from django.db.models import QuerySet
from django.shortcuts import get_object_or_404

from apps.dealers.models import DealerKey

from .models import DealerPrice


def list_key_prices(key_pk: int) -> QuerySet[DealerPrice]:
    """Получение списка цен дилеров по ключу дилера."""
    qs = DealerKey.objects.prefetch_related("prices")
    key = get_object_or_404(qs, pk=key_pk)
    return key.prices.all()


def list_prices() -> QuerySet[DealerPrice]:
    """Получение всех цен."""
    return DealerPrice.objects.select_related(
        "key", "key__dealer", "key__product"
    )


def there_are_prices_in_db() -> bool:
    """Проверяет наличие в БД загруженных цен."""
    return DealerPrice.objects.exists()


def delete_all_prices() -> None:
    """Удаление всех цен."""
    DealerPrice.objects.all().delete()
    return None


def prices_bulk_create(fields_sets: dict) -> None:
    fields = []
    for field_set in fields_sets:
        fields.append(DealerPrice(**field_set))
    DealerPrice.objects.bulk_create(fields)
    return None
