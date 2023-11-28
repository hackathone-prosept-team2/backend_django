from rest_framework import serializers

from apps.dealers.models import Dealer, DealerKey

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

    class Meta:
        model = DealerKey
        fields = ("id", "key", "dealer", "product")
