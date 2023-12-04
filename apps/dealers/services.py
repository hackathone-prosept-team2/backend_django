from django.db.models import QuerySet
from django.db.transaction import atomic

from .crud import (
    list_matches,
    change_status_to_declined,
    choose_one_decline_others,
    set_product_for_dealer_key,
)
from .models import Match


@atomic
def decline_matches(key_pk: int) -> QuerySet[Match]:
    matches = list_matches(key_pk=key_pk, add_products=False)
    change_status_to_declined(matches=matches)
    return matches


@atomic
def choose_match(key_pk: int, product_id: int) -> QuerySet[Match]:
    matches = list_matches(key_pk=key_pk, add_products=False)
    choose_one_decline_others(matches=matches, product_id=product_id)
    set_product_for_dealer_key(dealer_key_id=key_pk, product_id=product_id)
    return matches
