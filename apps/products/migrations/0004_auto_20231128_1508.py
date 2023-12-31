# Generated by Django 4.2.7 on 2023-11-28 12:08

from django.db import migrations, models

from apps.services.fixtures_parser import get_products_datasets


def create_categories(apps, schema_editor):
    Category: models.Model = apps.get_model("products", "Category")
    cats = [Category(id=i) for i in range(1, 60)]
    Category.objects.bulk_create(cats, ignore_conflicts=True)


def create_products(apps, schema_editor):
    Product: models.Model = apps.get_model("products", "Product")
    products_datasets = get_products_datasets()
    if products_datasets:
        products = [Product(**fields) for fields in products_datasets]
        Product.objects.bulk_create(products, ignore_conflicts=True)


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0003_alter_product_article"),
    ]

    operations = [
        migrations.RunPython(create_categories),
        migrations.RunPython(create_products),
    ]
