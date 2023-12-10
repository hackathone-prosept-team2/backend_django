from django.db.models import QuerySet, Q
from django.http import HttpRequest

from config.constants import MATCH_NUMBER

from .models import DealerKey, Match


def filter_keys(
    qs: QuerySet[DealerKey], request: HttpRequest
) -> QuerySet[DealerKey]:
    """Фильтрация списка ключей по наименованию/артикулу/статусу/дилеру."""
    text = request.GET.get("text")
    status = request.GET.get("status")
    dealer = request.GET.get("dealer")

    if text:
        qs = qs.filter(Q(name__icontains=text) | Q(article__icontains=text))
    if dealer:
        qs = qs.filter(dealer=dealer)
    if status:
        if status == Match.MatchStatus.YES:
            return qs.filter(product_id__isnull=False)
        if status == Match.MatchStatus.NO:
            return qs.filter(declined=MATCH_NUMBER)
        else:
            return qs.filter(
                product_id__isnull=True, declined__lt=MATCH_NUMBER
            )
    return qs
