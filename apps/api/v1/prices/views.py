from rest_framework.viewsets import ReadOnlyModelViewSet

from apps.prices.crud import list_prices

from . import serializer as ser


class PriceViewset(ReadOnlyModelViewSet):
    #  пока readonly, потом расширим
    """Цены дилеров компании Просепт."""

    queryset = list_prices()

    def get_serializer_class(self):
        if self.action == "list":
            return ser.PriceListSerializer
        return ser.PriceDetailSerializer
