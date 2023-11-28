from drf_spectacular.utils import extend_schema_view
from rest_framework.viewsets import ReadOnlyModelViewSet

from apps.dealers.crud import list_dealers, list_keys

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
