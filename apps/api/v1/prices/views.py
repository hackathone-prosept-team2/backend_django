from rest_framework.viewsets import ReadOnlyModelViewSet

from apps.prices.crud import list_prices

from ..pagination import CustomPagePagination
from . import serializer as ser


class PriceViewset(ReadOnlyModelViewSet):
    #  пока readonly, потом расширим
    """Цены дилеров компании Просепт."""

    queryset = list_prices()
    pagination_class = CustomPagePagination

    def get_serializer_class(self):
        if self.action == "list":
            return ser.PriceListSerializer
        return ser.PriceDetailSerializer
