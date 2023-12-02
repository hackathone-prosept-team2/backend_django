from drf_spectacular.utils import extend_schema_view
from rest_framework import views, status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ReadOnlyModelViewSet

from apps.dealers.crud import list_dealers, list_keys, list_matches
from apps.dealers.services import decline_matches

from ..pagination import CommonPagePagination
from .filters import DealerKeyFilter
from . import schema
from . import serializer as ser


@extend_schema_view(**schema.dealer_schema)
class DealerViewset(ReadOnlyModelViewSet):
    """Дилеры компании Просепт."""

    queryset = list_dealers()
    serializer_class = ser.DealerSerializer


@extend_schema_view(**schema.key_schema)
class DealerKeyViewset(ReadOnlyModelViewSet):
    """Ключи/артикулы Дилеров компании Просепт."""

    queryset = list_keys()
    serializer_class = ser.KeySerializer
    pagination_class = CommonPagePagination
    filterset_class = DealerKeyFilter


class MatchView(ListAPIView):
    """Список предлагаемых соответствий Ключ - Продукт."""

    serializer_class = ser.MatchSerializer

    def get_queryset(self):
        key_pk = self.kwargs.get("pk")
        return list_matches(key_pk=key_pk)


class DeclineMatchesView(views.APIView):
    """Отклонение всех предлагаемых соответствий Ключ - Продукт."""

    def post(self, request, pk):
        key_pk = self.kwargs.get("pk")
        decline_matches(key_pk=key_pk)
        return Response(status=status.HTTP_200_OK)
