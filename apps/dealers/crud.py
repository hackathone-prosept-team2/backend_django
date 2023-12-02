from django.db.models import (
    QuerySet,
    OuterRef,
    Subquery,
    Case,
    When,
    Value,
    Prefetch,
)
from django.shortcuts import get_object_or_404

from apps.prices.models import DealerPrice

from .models import Dealer, DealerKey, Match


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


def list_matches(key_pk: int, add_products: bool = True) -> QuerySet[Match]:
    """Получение списка возможных соответствий Ключ - Продукт."""
    subquery = Match.objects.filter(key_id=key_pk)
    if add_products:
        subquery = subquery.select_related("product")
    query = DealerKey.objects.prefetch_related(
        Prefetch(
            "matches",
            queryset=subquery,
        )
    )

    dealer_key = get_object_or_404(query, id=key_pk)
    return dealer_key.matches.all()


def change_status_to_declined(matches):
    """Изменение статуса у всех предложений на 'Не подходит'."""
    for match in matches:
        match.status = Match.MatchStatus.NO
    Match.objects.bulk_update(matches, ["status"])
    return None


# def get_keys_values():
#     return dict(DealerKey.objects.values_list("key", "id"))


# def bulk_create_keys(new_keys: list[DealerKey]) -> None:
#     DealerKey.objects.bulk_create(new_keys)
#     return None
