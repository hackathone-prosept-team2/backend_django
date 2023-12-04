from django.db.models import QuerySet

from .models import Product


def list_products() -> QuerySet[Product]:
    """Получение списка продуктов."""
    return Product.objects.all()


def product_exists(product_id: int) -> bool:
    """Флаг существования Продукта с указанным id"""
    return Product.objects.filter(id=product_id).exists()
