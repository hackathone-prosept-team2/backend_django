from drf_spectacular.utils import extend_schema_view

from rest_framework import views, status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ReadOnlyModelViewSet

from apps.dealers.crud import (
    list_dealers,
    list_keys,
    list_matches,
    list_dealers_report_data,
)
from apps.dealers.services import decline_matches, choose_match

from ..pagination import CommonPagePagination
from .filters import DealerKeyFilter
from . import schema
from . import serializer as ser


@extend_schema_view(**schema.dealer_schema)
class DealerViewset(ReadOnlyModelViewSet):
    """Дилеры компании Просепт."""

    queryset = list_dealers()
    serializer_class = ser.DealerSerializer


class DealersReport(ListAPIView):
    """Отчет по дилерам Просепт."""

    queryset = list_dealers_report_data()
    serializer_class = ser.DealerReportSerializer


@extend_schema_view(**schema.key_schema)
class DealerKeyViewset(ReadOnlyModelViewSet):
    """Ключи/артикулы Дилеров компании Просепт."""

    queryset = list_keys()
    serializer_class = ser.KeySerializer
    pagination_class = CommonPagePagination
    filterset_class = DealerKeyFilter


@extend_schema_view(**schema.matches_schema)
class MatchView(ListAPIView):
    """Список предлагаемых соответствий Ключ - Продукт."""

    serializer_class = ser.MatchSerializer

    def get_queryset(self):
        key_pk = self.kwargs.get("pk")
        return list_matches(key_pk=key_pk)


@extend_schema_view(**schema.matches_schema)
class DeclineMatchesView(views.APIView):
    """Отклонение всех предлагаемых соответствий Ключ - Продукт."""

    def post(self, request, pk):
        key_pk = self.kwargs.get("pk")
        matches = decline_matches(key_pk=key_pk)
        serializer = ser.MatchSerializer(instance=matches, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@extend_schema_view(**schema.choose_match_schema)
class ChooseMatchView(views.APIView):
    """Выбор 1 предлагаемого соответствия Ключ - Продукт."""

    def post(self, request, pk):
        key_pk = self.kwargs.get("pk")
        serializer = ser.ChooseMatchSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        product_id = serializer.validated_data["product_id"]
        matches = choose_match(key_pk=key_pk, product_id=product_id)
        serializer = ser.MatchSerializer(instance=matches, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
