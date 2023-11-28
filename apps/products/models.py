from django.db import models
from django.core.validators import MinValueValidator


class Category(models.Model):
    """Модель Категории Продуктов."""

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self) -> str:
        return f"Категория {self.id}"


class Product(models.Model):
    """Модель Продукта."""

    article = models.CharField(
        verbose_name="Артикул", max_length=255, unique=True
    )
    name_1c = models.CharField(
        verbose_name="Название 1с", max_length=255, blank=True
    )
    ean_13 = models.CharField(
        verbose_name="Код ean_13", max_length=20, blank=True
    )
    name = models.CharField(
        verbose_name="Название", max_length=255, blank=True
    )
    cost = models.DecimalField(
        verbose_name="Себестоимость",
        max_digits=7,
        decimal_places=2,
        blank=True,
        null=True,
        validators=[MinValueValidator(0)],
    )
    recommended_price = models.DecimalField(
        verbose_name="Рекомендованная цена",
        max_digits=7,
        decimal_places=2,
        blank=True,
        null=True,
        validators=[MinValueValidator(0)],
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
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self) -> str:
        return f"ID{self.id}. Артикул {self.article} {self.name}"
