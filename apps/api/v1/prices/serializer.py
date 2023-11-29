from rest_framework import serializers

from apps.prices.models import DealerPrice

from ..products.serializer import ProductShortSerializer


class BasePriceSerializer(serializers.ModelSerializer):
    """Базовый сериализатор для полей цен дилеров."""

    class Meta:
        model = DealerPrice
        fields = (
            "id",
            "price",
            "name",
            "date",
            "product_url",
        )


class KeyPriceSerializer(BasePriceSerializer):
    """Сериализатор для полей списка цен."""

    pass


class PriceDetailSerializer(BasePriceSerializer):
    """Сериализатор для полей просмотр экземпляра цен."""

    matches = ProductShortSerializer(many=True)

    class Meta(BasePriceSerializer.Meta):
        fields = BasePriceSerializer.Meta.fields + ("matches",)
