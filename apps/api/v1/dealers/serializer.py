from rest_framework import serializers

from apps.dealers.models import Dealer, DealerKey, Match

from ..products.serializer import ProductShortSerializer


class DealerSerializer(serializers.ModelSerializer):
    """Сериализатор для полей модели Дилер."""

    class Meta:
        model = Dealer
        fields = ("id", "name")


class KeySerializer(serializers.ModelSerializer):
    """Сериализатор для полей Ключей/артикулов Дилера."""

    dealer = DealerSerializer()
    product = ProductShortSerializer()
    name = serializers.CharField()
    last_price = serializers.DecimalField(max_digits=7, decimal_places=2)
    status = serializers.CharField()

    class Meta:
        model = DealerKey
        fields = (
            "id",
            "key",
            "name",
            "last_price",
            "status",
            "dealer",
            "product",
        )


class MatchSerializer(serializers.ModelSerializer):
    product = ProductShortSerializer()

    class Meta:
        model = Match
        fields = ("id", "product", "metrics", "status")
