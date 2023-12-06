from http import HTTPStatus

import pytest
from rest_framework.test import APIClient

from .utils import USER_VALID_DATA, USER_INVALID_DATA


@pytest.mark.django_db()
class Test00User:
    create_url = "/api/v1/auth/users/"
    me_url = "/api/v1/auth/users/me/"

    @pytest.mark.parametrize("data,messege", USER_VALID_DATA)
    def test_01_create_user_success(
        self, client: APIClient, data: dict[str, str], messege: str
    ) -> None:
        """Удачное создание пользователя."""
        response = client.post(self.create_url, data=data)
        assert response.status_code == HTTPStatus.CREATED, (
            f"Попытка создания пользователя с валидными данными ({messege})"
            f"не удалась - статус {response.status_code}"
        )

    @pytest.mark.parametrize("data,messege", USER_INVALID_DATA)
    def test_02_create_user_fail(
        self, client: APIClient, data: dict[str, str], messege: str
    ) -> None:
        """Неудачное создание пользователя."""
        response = client.post(self.create_url, data=data)
        assert response.status_code == HTTPStatus.BAD_REQUEST, (
            f"Попытка создания пользователя с невалидными данными ({messege})"
            f"вернула статус {response.status_code}"
        )

    def test_03_me_endpoint(
        self, client: APIClient, user_client: APIClient
    ) -> None:
        """Доступ к ендпоинту аутентифицированного пользователя."""
        mapping = (
            ("гость", client, HTTPStatus.UNAUTHORIZED),
            ("зарег.юзер", user_client, HTTPStatus.OK),
        )
        for scenario, conn, status in mapping:
            response = conn.get(self.me_url)
            assert response.status_code == status, (
                f"Попытка доступа {scenario} к данным по ручке /me"
                f"вернула статус {response.status_code}"
            )
