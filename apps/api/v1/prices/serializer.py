from rest_framework import serializers

from apps.prices.models import DealerPrice

from ..dealers.serializer import KeySerializer
from ..products.serializer import ProductShortSerializer


class BasePriceSerializer(serializers.ModelSerializer):
    key = KeySerializer()
    product = ProductShortSerializer(source="key.product")
    status = serializers.SerializerMethodField()

    class Meta:
        model = DealerPrice
        fields = (
            "id",
            "key",
            "price",
            "name",
            "date",
            "product_url",
            "product",
            "status",
        )

    def get_status(self, obj):
        return "Тут будет какой-то статус"


class PriceListSerializer(BasePriceSerializer):
    """Сериализатор для полей списка цен."""

    pass


class PriceDetailSerializer(BasePriceSerializer):
    """Сериализатор для полей просмотр экземпляра цен."""

    matches = ProductShortSerializer(many=True)

    class Meta(BasePriceSerializer.Meta):
        fields = BasePriceSerializer.Meta.fields + ("matches",)
