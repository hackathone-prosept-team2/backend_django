from django.db import models

from apps.products.models import Product


class Dealer(models.Model):
    """Модель компании-Дилера."""

    name = models.CharField(verbose_name="Наименование дилера", max_length=50)

    class Meta:
        ordering = ("id",)
        verbose_name = "Дилер"
        verbose_name_plural = "Дилеры"

    def __str__(self) -> str:
        return self.name


class DealerKey(models.Model):
    """Модель Ключа/артикула Дилера."""

    key = models.CharField(verbose_name="Ключ дилера", max_length=250)
    dealer = models.ForeignKey(
        Dealer, on_delete=models.CASCADE, verbose_name="Дилер"
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name="Продукт",
        blank=True,
        null=True,
    )
    is_provided = models.BooleanField(
        verbose_name="Есть в исходном csv", default=False
    )

    class Meta:
        ordering = ("id",)
        verbose_name = "Ключ дилера"
        verbose_name_plural = "Ключи дилера"
        default_related_name = "dealer_keys"
        constraints = (
            models.UniqueConstraint(
                fields=("dealer_id", "key"), name="unique_pair_dealer_and_key"
            ),
        )

    def __str__(self) -> str:
        return f"ID{self.id}. Dealer {self.dealer_id}: {self.key}"


class Match(models.Model):
    """Модель предлагаемых соответствий Ключ дилера - Продукт Просепт."""

    class MatchStatus(models.TextChoices):
        NEW = "new", "На проверку"
        YES = "yes", "Подтверждено"
        NO = "no", "Не подходит"

    key = models.ForeignKey(
        DealerKey, on_delete=models.CASCADE, verbose_name="Ключ дилера"
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name="Продукт"
    )
    similarity = models.IntegerField(verbose_name="Метрика соответствия в %")
    status = models.CharField(
        verbose_name="Статус предложения",
        max_length=3,
        choices=MatchStatus.choices,
        default=MatchStatus.NEW,
    )

    class Meta:
        ordering = ("-similarity", "id")
        verbose_name = "Предложение соответствия"
        verbose_name_plural = "Предложения соответствия"
        default_related_name = "matches"
        constraints = (
            models.UniqueConstraint(
                fields=("key_id", "product_id"),
                name="unique_pair_key_and_product",
            ),
        )

    def __str__(self) -> str:
        return (
            f"ID{self.id}. {self.status}: "
            f"Key{self.key_id} - Product{self.product_id}"
        )
