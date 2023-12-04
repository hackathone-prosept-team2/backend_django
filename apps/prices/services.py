from django.db.transaction import atomic

from apps.dealers.crud import delete_new_dealer_keys

from .crud import delete_all_prices


@atomic
def delete_prices_and_relations() -> None:
    delete_all_prices()
    delete_new_dealer_keys()
    return None
