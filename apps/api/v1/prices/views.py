from rest_framework.generics import ListAPIView

from apps.prices.crud import list_key_prices

from ..pagination import NestedPagePagination
from . import serializer as ser


class KeyPriceViewset(ListAPIView):
    """Цены дилеров компании Просепт по 1 ключу."""

    pagination_class = NestedPagePagination
    serializer_class = ser.KeyPriceSerializer

    def get_queryset(self):
        key_pk = self.kwargs.get("pk")
        return list_key_prices(key_pk=key_pk)
