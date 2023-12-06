import pytest

from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token

from apps.prices.models import DealerPrice
from apps.prices.services import create_prices

from .utils import TEST_PRICE_DATA


@pytest.fixture
def user(django_user_model):
    """Тестовый пользователь оператор."""
    return django_user_model.objects.create_user(
        email="user@testmail.ru", password="Password-123"
    )


@pytest.fixture
def user_token(user):
    """Токен для оператора."""
    token = Token.objects.create(user=user)
    return token.key


@pytest.fixture
def user_client(user_token):
    """Аутентифицированный клиент-оператор."""
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f"Token {user_token}")
    return client


@pytest.fixture
def price():
    """Цена для ключа с указанным продуктом."""
    return DealerPrice.objects.create(
        key_id=1,
        price=233,
        name="Средство универсальное Prosept Universal Spray, 500мл",
        date="2023-07-14",
        product_url=(
            "https://akson.ru//p/sredstvo_universalnoe"
            "_prosept_universal_spray_500ml/"
        ),
    )


@pytest.fixture
def price2():
    """Цена для ключа без подобранного продукта."""
    create_prices(price_data=TEST_PRICE_DATA)
    key = TEST_PRICE_DATA[0]["product_key"]
    dealer_id = TEST_PRICE_DATA[0]["dealer_id"]
    return DealerPrice.objects.get(key__key=key, key__dealer_id=dealer_id)
