from drf_spectacular.utils import extend_schema_view
from rest_framework import status, views
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from apps.prices.crud import list_key_prices, there_are_prices_in_db
from apps.prices.services import create_prices, delete_prices_and_relations

from ..pagination import NestedPagePagination
from . import schema, serializer as ser


@extend_schema_view(**schema.key_prices_schema)
class KeyPriceView(ListAPIView):
    """Список цен по 1 указанному ключу."""

    pagination_class = NestedPagePagination
    serializer_class = ser.KeyPriceSerializer

    def get_queryset(self):
        key_pk = self.kwargs.get("pk")
        return list_key_prices(key_pk=key_pk)


@extend_schema_view(**schema.prices_schema)
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
