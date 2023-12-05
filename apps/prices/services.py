import csv
from pathlib import Path

from django.db.transaction import atomic

from apps.dealers.crud import (
    delete_new_dealer_keys,
    delete_all_matches,
    get_or_create_dealer_key,
    get_first_free_dealer_key_id,
    matches_bulk_create,
)
from apps.services.match_service import RecommendationService

from .crud import delete_all_prices, prices_bulk_create


@atomic
def delete_prices_and_relations() -> None:
    delete_all_matches()
    delete_all_prices()
    delete_new_dealer_keys()
    return None


def get_prices_data() -> list[dict]:
    filename = Path("static", "fixtures", "marketing_dealerprice.csv")
    with open(filename, mode="r", encoding="utf8") as file:
        reader = csv.DictReader(file, delimiter=";")
        data = list(reader)
    return data


def form_price_obj_fields(id: int, dataset: dict) -> dict:
    return {
        "key_id": id,
        "price": dataset["price"],
        "name": dataset["product_name"],
        "date": dataset["date"],
        "product_url": dataset["product_url"],
    }


def recommend_products(key_datasets: dict[int, str]) -> None:
    service = RecommendationService()
    matches_datasets = []
    for key_id, name in key_datasets.items():
        matches = service.get_recommendations(dealer_name=name)
        for metric, product_id in matches:
            similarity = int((1 - metric) * 100)
            fields = {
                "key_id": key_id,
                "product_id": product_id,
                "similarity": similarity,
            }
            matches_datasets.append(fields)
    matches_bulk_create(field_sets=matches_datasets)
    return None


@atomic
def create_prices() -> None:
    data = get_prices_data()
    id_counter = get_first_free_dealer_key_id()
    prices_datasets = []
    keys_to_match = {}
    for dataset in data:
        dealer_key, created = get_or_create_dealer_key(
            dealer_key=dataset["product_key"],
            dealer_id=dataset["dealer_id"],
            id=id_counter,
        )
        fields = form_price_obj_fields(id=dealer_key.id, dataset=dataset)

        if created:
            id_counter += 1
            keys_to_match[dealer_key.id] = dataset["product_name"]
        elif dealer_key.id in keys_to_match:
            keys_to_match[dealer_key.id] = dataset["product_name"]

        prices_datasets.append(fields)
    recommend_products(key_datasets=keys_to_match)
    prices_bulk_create(fields_sets=prices_datasets)
    return None
