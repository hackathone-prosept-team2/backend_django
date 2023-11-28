from django.db.models import QuerySet

from .models import Dealer, DealerKey


def list_dealers() -> QuerySet[Dealer]:
    """Получение списка дилеров."""
    return Dealer.objects.all()


def list_keys() -> QuerySet[DealerKey]:
    """Получение списка ключей/артикулов дилеров."""
    return DealerKey.objects.select_related("dealer", "product")


def get_keys_values():
    return dict(DealerKey.objects.values_list("key", "id"))


def bulk_create_keys(new_keys: list[DealerKey]) -> None:
    DealerKey.objects.bulk_create(new_keys)
    return None
