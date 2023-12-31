# Generated by Django 4.2.7 on 2023-11-28 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "article",
                    models.CharField(max_length=255, verbose_name="Артикул"),
                ),
                (
                    "name_1c",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="Название 1с"
                    ),
                ),
                (
                    "ean_13",
                    models.CharField(
                        blank=True, max_length=20, verbose_name="Код ean_13"
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="Название"
                    ),
                ),
                (
                    "cost",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=7,
                        null=True,
                        verbose_name="Себестоимость",
                    ),
                ),
                (
                    "recommended_price",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=7,
                        null=True,
                        verbose_name="Себестоимость",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="products",
                        to="products.category",
                        verbose_name="Категория",
                    ),
                ),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
            },
        ),
    ]
