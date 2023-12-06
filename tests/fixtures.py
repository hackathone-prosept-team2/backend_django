import pytest

from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token


@pytest.fixture
def user(django_user_model):
    return django_user_model.objects.create_user(
        email="user@testmail.ru", password="Password-123"
    )


@pytest.fixture
def user_token(user):
    token = Token.objects.create(user=user)
    return token.key


@pytest.fixture
def user_client(user_token):
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f"Token {user_token}")
    return client
