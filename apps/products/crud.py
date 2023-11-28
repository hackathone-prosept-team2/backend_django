from django.db.models import QuerySet

from .models import Product


def list_products() -> QuerySet[Product]:
    """Получение списка продуктов."""
    return Product.objects.all()
