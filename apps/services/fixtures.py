import csv
from pathlib import Path

from apps.dealers.models import Dealer, DealerKey
from apps.products.models import Product


def get_products_datasets() -> list[Product]:
    filename = Path("static", "fixtures", "marketing_product.csv")
    with open(filename, mode="r", encoding="utf8") as file:
        reader = csv.DictReader(file, delimiter=";")
        products = []
        for row in reader:
            kwargs = {}
            kwargs["id"] = row["id"]
            kwargs["article"] = row["article"]
            kwargs["ean_13"] = row["ean_13"]
            kwargs["name"] = row["name"]
            kwargs["name_1c"] = row["name_1c"]
            kwargs["cost"] = float(row["cost"]) if row["cost"] else None
            kwargs["recommended_price"] = (
                float(row["recommended_price"])
                if row["recommended_price"]
                else None
            )
            kwargs["category_id"] = (
                int(float(row["category_id"])) if row["category_id"] else None
            )
            products.append(Product(**kwargs))
    return products


def get_dealers_datasets() -> list[Dealer]:
    filename = Path("static", "fixtures", "marketing_dealer.csv")
    with open(filename, mode="r", encoding="utf8") as file:
        reader = csv.DictReader(file, delimiter=";")
        return [Dealer(**row) for row in reader]


def get_dealers_keys_datasets() -> list[DealerKey]:
    filename = Path("static", "fixtures", "marketing_productdealerkey.csv")
    with open(filename, mode="r", encoding="utf8") as file:
        reader = csv.DictReader(file, delimiter=";")
        return [DealerKey(is_provided=True, **row) for row in reader]
