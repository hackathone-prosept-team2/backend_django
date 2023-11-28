from django.db.models import QuerySet

from .models import Dealer, DealerKey


def list_dealers() -> QuerySet[Dealer]:
    """Получение списка дилеров."""
    return Dealer.objects.all()


def list_keys() -> QuerySet[DealerKey]:
    """Получение списка ключей/артикулов дилеров."""
    return DealerKey.objects.select_related("dealer", "product")
