from drf_spectacular.utils import extend_schema_view
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ReadOnlyModelViewSet

from apps.dealers.crud import list_dealers, list_keys, list_dealers_report_data

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
