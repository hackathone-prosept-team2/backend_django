from django.db.models import (
    QuerySet,
    OuterRef,
    Subquery,
    Count,
    Q,
    Prefetch,
)
from django.shortcuts import get_object_or_404

from apps.prices.models import DealerPrice

from .models import Dealer, DealerKey, Match


def list_dealers() -> QuerySet[Dealer]:
    """Получение списка дилеров."""
    return Dealer.objects.all()


def list_dealers_report_data() -> QuerySet[Dealer]:
    """Получение списка дилеров с данными для отчета."""
    return Dealer.objects.annotate(
        total_prices=Count("dealer_keys__prices", distinct=True),
        total_keys=Count(
            "dealer_keys",
            distinct=True,
            filter=Q(dealer_keys__prices__isnull=False),
        ),
        keys_with_product=Count(
            "dealer_keys",
            distinct=True,
            filter=(
                Q(dealer_keys__product_id__isnull=False)
                & Q(dealer_keys__prices__isnull=False)
            ),
        ),
        confirmed_matches=Count(
            "dealer_keys",
            distinct=True,
            filter=Q(dealer_keys__matches__status=Match.MatchStatus.YES),
        ),
        to_be_checked=Count(
            "dealer_keys",
            distinct=True,
            filter=Q(dealer_keys__matches__status=Match.MatchStatus.NEW),
        ),
    )


def list_keys() -> QuerySet[DealerKey]:
    """Получение списка ключей/артикулов дилеров."""
    return (
        DealerKey.objects.select_related("dealer", "product").annotate(
            name=Subquery(
                DealerPrice.objects.filter(key_id=OuterRef("pk")).values(
                    "name"
                )[:1]
            ),
            last_price=Subquery(
                DealerPrice.objects.filter(key_id=OuterRef("pk")).values(
                    "price"
                )[:1]
            ),
            declined=Count(
                "matches", filter=Q(matches__status=Match.MatchStatus.NO)
            ),
            # similarity=Subquery(
            #     Match.objects.filter(key_id=OuterRef("pk")).values(
            #         "similarity"
            #     )[:1]
            # ),
        )
        # фильтр позволяет выгружать только ключи, которые есть в списке цен
        .filter(name__isnull=False)
    )


def list_matches(key_pk: int, add_products: bool = True) -> QuerySet[Match]:
    """Получение списка возможных соответствий Ключ - Продукт."""
    subquery = Match.objects.filter(key_id=key_pk).select_related("product")
    query = DealerKey.objects.prefetch_related(
        Prefetch(
            "matches",
            queryset=subquery,
        )
    )

    dealer_key = get_object_or_404(query, id=key_pk)
    return dealer_key.matches.all()


def change_status_to_declined(matches: QuerySet[Match]) -> None:
    """Изменение статуса у всех предложений на "Не подходит"."""
    for product_match in matches:
        product_match.status = Match.MatchStatus.NO
    Match.objects.bulk_update(matches, ["status"])
    return None


def choose_one_decline_others(
    matches: QuerySet[Match], product_id: int
) -> None:
    """
    Изменение статуса у всех предложений ключа:
    "Подтверждено" для выбранного; "Не подходит" для остальных.
    """
    for product_match in matches:
        if product_match.product_id == product_id:
            product_match.status = Match.MatchStatus.YES
        else:
            product_match.status = Match.MatchStatus.NO
    Match.objects.bulk_update(matches, ["status"])
    return None


def set_product_for_dealer_key(dealer_key_id: int, product_id: int) -> None:
    """Назначение продукта уникальному ключу дилера."""
    key = DealerKey.objects.filter(id=dealer_key_id).first()
    key.product_id = product_id
    key.save()
    return None


def delete_new_dealer_keys() -> None:
    """Удаление всех ключей дилеров, которых не было в начальном csv."""
    DealerKey.objects.filter(is_provided=False).delete()
    return None


def delete_all_matches() -> None:
    """Удаление всех предложений по соответствию Ключ - Продукт."""
    Match.objects.all().delete()
    return None


def get_or_create_dealer_key(
    id: int, dealer_key: str, dealer_id: int
) -> tuple[DealerKey, bool]:
    return DealerKey.objects.get_or_create(
        key=dealer_key,
        dealer_id=dealer_id,
        defaults={"id": id},
    )


def get_first_free_dealer_key_id():
    return DealerKey.objects.last().id + 1


def matches_bulk_create(field_sets: list[dict]) -> None:
    fields = []
    for field_set in field_sets:
        fields.append(Match(**field_set))
    Match.objects.bulk_create(fields)
    return None


# def get_keys_values():
#     return dict(DealerKey.objects.values_list("key", "id"))
