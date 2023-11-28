from django.db import models

from apps.dealers.models import DealerKey


class DealerPrice(models.Model):
    """Модель Цена Дилера."""

    key = models.ForeignKey(
        DealerKey, on_delete=models.CASCADE, verbose_name="Ключ дилера"
    )
    price = models.DecimalField(
        verbose_name="Цена",
        max_digits=7,
        decimal_places=2,
    )
    name = models.CharField(verbose_name="Наименование дилера", max_length=255)
    date = models.DateField(verbose_name="Дата получения цены")
    product_url = models.URLField(
        verbose_name="Ссылка на сайт дилера", max_length=255
    )
