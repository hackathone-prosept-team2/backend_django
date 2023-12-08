from django.db.models import QuerySet
from django.db.transaction import atomic

from .crud import (
    change_status_to_declined,
    choose_one_decline_others,
    delete_connection_with_product,
    list_matches,
    set_product_for_dealer_key,
)
from .models import Match


@atomic
def decline_matches(key_pk: int) -> QuerySet[Match]:
    """Сменить всем предложениям статус на "Не подходит"."""
    matches = list_matches(key_pk=key_pk)
    change_status_to_declined(matches=matches)
    delete_connection_with_product(key_id=key_pk)
    return matches


@atomic
def choose_match(key_pk: int, product_id: int) -> QuerySet[Match]:
    """Выбрать продукт из списка предложений."""
    matches = list_matches(key_pk=key_pk)
    choose_one_decline_others(matches=matches, product_id=product_id)
    set_product_for_dealer_key(dealer_key_id=key_pk, product_id=product_id)
    return matches
