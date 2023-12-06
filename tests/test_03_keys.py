from http import HTTPStatus

import pytest
from rest_framework.test import APIClient

from apps.prices.models import DealerPrice
from config.constants import MATCH_NUMBER, KeyStatus


@pytest.mark.django_db()
class Test03DealerKey:
    list_url = "/api/v1/keys/"
    get_url = "/api/v1/keys/{id}/"
    matches_url = "/api/v1/keys/{id}/matches/"
    prices_url = "/api/v1/keys/{id}/prices/"
    choose_url = "/api/v1/keys/{id}/choose_match/"
    decline_url = "/api/v1/keys/{id}/decline_matches/"

    def test_01_access_to_urls(
        self, client: APIClient, user_client: APIClient, price: DealerPrice
    ) -> None:
        """Доступ к get-эндпоинтам цен для гостя и пользователя."""
        mapping = (
            ("гость", client, HTTPStatus.UNAUTHORIZED),
            ("зарег.юзер", user_client, HTTPStatus.OK),
        )

        urls = [
            self.list_url,
            self.get_url.format(id=price.key_id),
            self.matches_url.format(id=price.key_id),
            self.prices_url.format(id=price.key_id),
        ]

        for scenario, conn, status in mapping:
            for url in urls:
                response = conn.get(url)
                assert response.status_code == status, (
                    f"Попытка доступа {scenario} к {url}"
                    f"вернула статус {response.status_code}"
                )

    def test_02_work_with_matches(
        self, user_client: APIClient, price2: DealerPrice
    ) -> None:
        """Работа с подобранными вариантами продуктов для ключей."""
        # Получение списка подобранных продуктов
        url = self.matches_url.format(id=price2.key_id)
        response = user_client.get(url)
        assert (
            response.status_code == HTTPStatus.OK
        ), f"GET-запрос к {url} вернул ответ {response.status_code}"

        response = response.json()
        assert (
            len(response) == MATCH_NUMBER
        ), f"Кол-во подобранных продуктов не равно {MATCH_NUMBER}"

        assert response[0]["status"] == KeyStatus.CHECK

        # Выбор 1 продукта - первого из списка
        chosen_product_id = response[0]["product"]["id"]
        response = user_client.post(
            self.choose_url.format(id=price2.key_id),
            data={"product_id": chosen_product_id},
        )

        assert response.status_code == HTTPStatus.OK
        response = response.json()
        assert len(response) == MATCH_NUMBER, (
            "Кол-во подобранных продуктов в ответе на выбор 1 варианта "
            f"не равно {MATCH_NUMBER}"
        )

        assert response[0]["status"] == KeyStatus.FOUND
        assert response[1]["status"] == KeyStatus.DECLINED

        # Отказ от всех подобранных вариантов
        response = user_client.post(self.decline_url.format(id=price2.key_id))
        assert response.status_code == HTTPStatus.OK

        response = response.json()
        assert len(response) == MATCH_NUMBER, (
            "Кол-во подобранных продуктов в ответе на отказ от "
            f"вариантов подбора не равно {MATCH_NUMBER}"
        )

        assert response[0]["status"] == KeyStatus.DECLINED
        assert response[1]["status"] == KeyStatus.DECLINED
