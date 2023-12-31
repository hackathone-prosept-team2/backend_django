from http import HTTPStatus

import pytest
from rest_framework.test import APIClient


@pytest.mark.django_db()
class Test01Dealer:
    list_url = "/api/v1/dealers/"
    get_url = "/api/v1/dealers/1/"
    report_url = "/api/v1/dealers/report/"

    def test_01_access_to_urls(
        self, client: APIClient, user_client: APIClient
    ) -> None:
        """Доступ к эндпоинтам дилеров для гостя и пользователя."""
        mapping = (
            ("гость", client, HTTPStatus.UNAUTHORIZED),
            ("зарег.юзер", user_client, HTTPStatus.OK),
        )
        for scenario, conn, status in mapping:
            for url in [self.list_url, self.get_url, self.report_url]:
                response = conn.get(url)
                assert response.status_code == status, (
                    f"Попытка доступа {scenario} к {url}"
                    f"вернула статус {response.status_code}"
                )
