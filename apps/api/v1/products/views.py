from drf_spectacular.utils import extend_schema_view
from rest_framework.viewsets import ReadOnlyModelViewSet

from apps.products.crud import list_products

from ..pagination import CommonPagePagination
from . import schema, serializer as ser


@extend_schema_view(**schema.product_schema)
class ProductViewset(ReadOnlyModelViewSet):
    """Продукты компании Просепт."""

    queryset = list_products()
    pagination_class = CommonPagePagination

    def get_serializer_class(self):
        if self.action == "list":
            return ser.ProductShortSerializer
        return ser.ProductDetailedSerializer
