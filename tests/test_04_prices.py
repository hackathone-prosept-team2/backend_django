from http import HTTPStatus

import pytest
from rest_framework.test import APIClient

from apps.prices.services import create_prices

from .utils import TEST_PRICE_DATA


@pytest.mark.django_db()
class Test04DealerPrice:
    url = "/api/v1/prices/"

    def test_01_load_prices_fail(self, user_client: APIClient) -> None:
        """Создание цен и попытка загрузки цен из файла."""
        create_prices(TEST_PRICE_DATA)
        response = user_client.post(self.url)
        assert response.status_code == HTTPStatus.BAD_REQUEST

    def test_02_delete_prices_from_db(self, user_client: APIClient) -> None:
        """Удаление всех цен и связанных объектов из базы данных."""

        response = user_client.delete(self.url)
        assert response.status_code == HTTPStatus.NO_CONTENT
