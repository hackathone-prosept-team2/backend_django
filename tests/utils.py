USER_VALID_DATA = (
    (
        {
            "email": "test_client_01@unexistingmail.ru",
            "password": "neverinmylife-123",
        },
        "пользователь с нормальными данными",
    ),
    (
        {
            "email": "test_client_02@unexistingmail.ru",
            "password": "11111111",
        },
        "пользователь с паролем из цифр",
    ),
)


USER_INVALID_DATA = (
    (
        {
            "email": "test_client_03",
            "password": "neverinmylife-123",
        },
        "неверный формат email - без @ и домена.",
    ),
    (
        {
            "email": "test_client_04@",
            "password": "11111111",
        },
        "неверный формат email - без домена",
    ),
    (
        {
            "email": "test_client_05@unexistingmail.ru",
            "password": "123",
        },
        "пользователь с коротким паролем",
    ),
)


TEST_PRICE_DATA = [
    {
        "product_key": "26397139",
        "price": "1975.00",
        "product_url": (
            "https://vimos.ru/product/kraska-dla-plit-osb-"
            "prosept-dla-vnutrennih-i-naruznyh-rabot-7-kg"
        ),
        "product_name": (
            "Краска для плит OSB Prosept для внутренних и наружных работ 7 кг"
        ),
        "date": "2023-07-14",
        "dealer_id": 16,
    }
]
