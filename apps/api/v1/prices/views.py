from rest_framework.generics import ListAPIView
from rest_framework import views, status
from rest_framework.response import Response

from apps.prices.crud import list_key_prices
from apps.prices.services import delete_prices_and_relations

from ..pagination import NestedPagePagination
from . import serializer as ser


class KeyPriceViewset(ListAPIView):
    """Цены дилеров компании Просепт по 1 ключу."""

    pagination_class = NestedPagePagination
    serializer_class = ser.KeyPriceSerializer

    def get_queryset(self):
        key_pk = self.kwargs.get("pk")
        return list_key_prices(key_pk=key_pk)


class DeletePricesView(views.APIView):
    """Удаление всех загруженных цен дилеров и связанных ключей дилеров."""

    def delete(self, request):
        delete_prices_and_relations()
        return Response(status=status.HTTP_204_NO_CONTENT)
