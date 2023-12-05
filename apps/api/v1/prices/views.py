from rest_framework.generics import ListAPIView
from rest_framework import views, status
from rest_framework.response import Response

from apps.prices.crud import list_key_prices, there_are_prices_in_db
from apps.prices.services import delete_prices_and_relations, create_prices

from ..pagination import NestedPagePagination
from . import serializer as ser


class KeyPriceView(ListAPIView):
    """Цены дилеров компании Просепт по 1 ключу."""

    pagination_class = NestedPagePagination
    serializer_class = ser.KeyPriceSerializer

    def get_queryset(self):
        key_pk = self.kwargs.get("pk")
        return list_key_prices(key_pk=key_pk)


class PricesView(views.APIView):
    """Загрузка и удаление цен дилеров и связанных ключей дилеров."""

    def post(self, request):
        if there_are_prices_in_db():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        create_prices()
        return Response(status=status.HTTP_201_CREATED)

    def delete(self, request):
        delete_prices_and_relations()
        return Response(status=status.HTTP_204_NO_CONTENT)
