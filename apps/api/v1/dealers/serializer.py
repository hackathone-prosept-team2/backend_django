from rest_framework import serializers

from apps.dealers.models import Dealer, DealerKey

from ..products.serializer import ProductShortSerializer


class BaseDealerSerializer(serializers.ModelSerializer):
    """Базовый сериализатор для полей модели Дилер."""

    class Meta:
        model = Dealer
        fields = ("id", "name")


class DealerSerializer(BaseDealerSerializer):
    """Сериализатор полей для списка Дилеров."""

    pass


class DealerReportSerializer(BaseDealerSerializer):
    """Сериализатор полей для отчета по Дилерам."""

    total_prices = serializers.IntegerField()
    total_keys = serializers.IntegerField()
    keys_with_product = serializers.IntegerField()
    keys_without_product = serializers.SerializerMethodField()
    confirmed_matches = serializers.IntegerField()
    to_be_checked = serializers.IntegerField()
    no_matches = serializers.IntegerField()

    class Meta(BaseDealerSerializer.Meta):
        fields = BaseDealerSerializer.Meta.fields + (
            "total_prices",
            "total_keys",
            "keys_with_product",
            "keys_without_product",
            "confirmed_matches",
            "to_be_checked",
            "no_matches",
        )

    def get_keys_without_product(self, obj):
        return obj.total_keys - obj.keys_with_product


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
