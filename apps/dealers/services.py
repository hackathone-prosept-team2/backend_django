from django.db.transaction import atomic

from .crud import list_matches, change_status_to_declined


@atomic
def decline_matches(key_pk):
    matches = list_matches(key_pk=key_pk, add_products=False)
    change_status_to_declined(matches=matches)
    return None
