from django.db.models import QuerySet, OuterRef, Subquery, Case, When, Value

from apps.prices.models import DealerPrice

from .models import Dealer, DealerKey


def list_dealers() -> QuerySet[Dealer]:
    """Получение списка дилеров."""
    return Dealer.objects.all()


def list_keys() -> QuerySet[DealerKey]:
    """Получение списка ключей/артикулов дилеров."""
    return (
        DealerKey.objects.select_related("dealer", "product").annotate(
            name=Subquery(
                DealerPrice.objects.filter(key__pk=OuterRef("pk")).values(
                    "name"
                )[:1]
            ),
            last_price=Subquery(
                DealerPrice.objects.filter(key__pk=OuterRef("pk")).values(
                    "price"
                )[:1]
            ),
            status=Case(
                When(product__isnull=False, then=Value("-")),
                # TODO код для расчета статуса по рекомендациям
                default=Value("число рекомендаций"),
            ),
        )
        # фильтр позволяет выгружать только ключи, которые есть в списке цен
        .filter(name__isnull=False)
    )


def get_keys_values():
    return dict(DealerKey.objects.values_list("key", "id"))


def bulk_create_keys(new_keys: list[DealerKey]) -> None:
    DealerKey.objects.bulk_create(new_keys)
    return None
