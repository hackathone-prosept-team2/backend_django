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
