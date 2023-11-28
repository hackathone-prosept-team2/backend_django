from rest_framework import serializers

from apps.products.models import Product


class BaseProductSerializer(serializers.ModelSerializer):
    """Базовый сериализатор для Продуктов."""

    class Meta:
        model = Product
        fields = ("id", "name_1c", "article", "cost", "recommended_price")


class ProductShortSerializer(BaseProductSerializer):
    """Краткий сериализатор Продукта для списков."""

    pass


class ProductDetailedSerializer(BaseProductSerializer):
    """Подробный сериализатор Продукта для единичной выдачи."""

    class Meta(BaseProductSerializer.Meta):
        fields = BaseProductSerializer.Meta.fields + (
            "category_id",
            "name",
            "ean_13",
        )
