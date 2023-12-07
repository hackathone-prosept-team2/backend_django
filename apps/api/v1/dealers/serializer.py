from rest_framework import serializers

from apps.dealers.models import Dealer, DealerKey, Match
from apps.products.crud import product_exists
from config.constants import MATCH_NUMBER, KeyStatus

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
    no_matches = serializers.SerializerMethodField()

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

    def get_no_matches(self, obj):
        return obj.total_keys - obj.keys_with_product - obj.to_be_checked


class BaseKeySerializer(serializers.ModelSerializer):
    """Базовый сериализатор для Ключей/артикулов Дилера."""

    class Meta:
        model = DealerKey
        fields = (
            "id",
            "key",
            "dealer",
            "product",
        )


class KeyExportSerializer(BaseKeySerializer):
    """Сериализатор для экспорта Ключей/артикулов Дилера."""

    chosen_at = serializers.DateField(source="edited_at")

    class Meta(BaseKeySerializer.Meta):
        fields = BaseKeySerializer.Meta.fields + ("chosen_at",)


class KeySerializer(BaseKeySerializer):
    """Сериализатор для полей просмотра Ключей/артикулов Дилера."""

    dealer = DealerSerializer()
    product = ProductShortSerializer()
    name = serializers.CharField()
    last_price = serializers.DecimalField(max_digits=7, decimal_places=2)
    status = serializers.SerializerMethodField()

    class Meta(BaseKeySerializer.Meta):
        model = DealerKey
        fields = BaseKeySerializer.Meta.fields + (
            "name",
            "last_price",
            "status",
        )

    def get_status(self, obj):
        if obj.product_id is not None:
            return KeyStatus.FOUND
        if obj.declined == MATCH_NUMBER:
            return KeyStatus.DECLINED
        return KeyStatus.CHECK


class MatchSerializer(serializers.ModelSerializer):
    """Сериализатор полей списка предлагаемых соответствий Ключ - Продукт."""

    product = ProductShortSerializer()

    class Meta:
        model = Match
        fields = ("id", "product", "similarity", "status")

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["status"] = instance.get_status_display()
        return rep


class ChooseMatchSerializer(serializers.Serializer):
    """Сериализатор выбора Продукта из предлагаемых соответствий."""

    product_id = serializers.IntegerField()

    def validate_product_id(self, value):
        if not product_exists(product_id=value):
            raise serializers.ValidationError(
                "Указанный id продукта отсутствует в базе."
            )
        return value
