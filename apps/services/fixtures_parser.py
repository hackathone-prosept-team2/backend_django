import csv
from pathlib import Path

from apps.dealers.models import Dealer, DealerKey
from apps.prices.models import DealerPrice
from apps.products.models import Product


def get_products_datasets() -> list[Product]:
    """Сбор списка аргументов для создания Продуктов."""
    filename = Path("static", "fixtures", "marketing_product.csv")
    with open(filename, mode="r", encoding="utf8") as file:
        reader = csv.DictReader(file, delimiter=";")
        products_datasets = []
        for row in reader:
            fields = {
                "id": row["id"],
                "article": row["article"],
                "ean_13": row["ean_13"],
                "name": row["name"],
                "name_1c": row["name_1c"],
                "cost": float(row["cost"]) if row["cost"] else None,
                "recommended_price": (
                    float(row["recommended_price"])
                    if row["recommended_price"]
                    else None
                ),
                "category_id": (
                    int(float(row["category_id"]))
                    if row["category_id"]
                    else None
                ),
            }
            products_datasets.append(fields)
    return products_datasets


def get_dealers_datasets() -> list[Dealer]:
    filename = Path("static", "fixtures", "marketing_dealer.csv")
    with open(filename, mode="r", encoding="utf8") as file:
        reader = csv.DictReader(file, delimiter=";")
        dealers_datasets = list(reader)
    return dealers_datasets


def get_dealers_keys_datasets() -> list[DealerKey]:
    filename = Path("static", "fixtures", "marketing_productdealerkey.csv")
    with open(filename, mode="r", encoding="utf8") as file:
        reader = csv.DictReader(file, delimiter=";")
        keys_datasets = [{"is_provided": True} | row for row in reader]
    return keys_datasets


def get_prices_datasets() -> list[DealerPrice]:
    filename = Path("static", "fixtures", "marketing_dealerprice.csv")
    with open(filename, mode="r", encoding="utf8") as file:
        reader = csv.DictReader(file, delimiter=";")
        prices_datasets = []
        id_counter = DealerKey.objects.last().id
        for row in reader:
            dealer_key, created = DealerKey.objects.get_or_create(
                key=row["product_key"],
                dealer_id=row["dealer_id"],
                defaults={"id": id_counter + 1},
            )
            if created:
                id_counter += 1
            fields = {
                "key_id": dealer_key.id,
                "price": row["price"],
                "name": row["product_name"],
                "date": row["date"],
                "product_url": row["product_url"],
            }
            prices_datasets.append(fields)
    return prices_datasets
