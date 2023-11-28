from django.db import models


class Category(models.Model):
    """Модель Категории Продуктов."""

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    """Модель Продукта."""

    article = models.CharField(verbose_name="Артикул", max_length=255)
    name_1c = models.CharField(
        verbose_name="Название 1с", max_length=255, null=True
    )
    ean_13 = models.CharField(
        verbose_name="Код ean_13", max_length=20, null=True
    )
    name = models.CharField(verbose_name="Название", max_length=255, null=True)
    cost = models.DecimalField(
        verbose_name="Себестоимость",
        max_digits=7,
        decimal_places=2,
        blank=True,
        null=True,
    )
    recommended_price = models.DecimalField(
        verbose_name="Себестоимость",
        max_digits=7,
        decimal_places=2,
        blank=True,
        null=True,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="Категория",
        related_name="products",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self) -> str:
        return f"ID{self.id}. Артикул {self.article} {self.name}"
