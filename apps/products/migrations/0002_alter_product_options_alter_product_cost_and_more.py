# Generated by Django 4.2.7 on 2023-11-28 07:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
            },
        ),
        migrations.AlterField(
            model_name="product",
            name="cost",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=7,
                null=True,
                validators=[django.core.validators.MinValueValidator(0)],
                verbose_name="Себестоимость",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="recommended_price",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=7,
                null=True,
                validators=[django.core.validators.MinValueValidator(0)],
                verbose_name="Себестоимость",
            ),
        ),
    ]
