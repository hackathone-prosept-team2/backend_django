from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView

from apps.dealers.models import DealerKey
from apps.prices.crud import list_key_prices

from ..pagination import NestedPagePagination
from . import serializer as ser


class KeyPriceViewset(ListAPIView):
    """Цены дилеров компании Просепт по 1 ключу."""

    pagination_class = NestedPagePagination
    serializer_class = ser.KeyPriceSerializer

    def get_queryset(self):
        key_pk = self.kwargs.get("pk")
        dealer_key = get_object_or_404(DealerKey, pk=key_pk)
        return list_key_prices(dealer_key=dealer_key)
