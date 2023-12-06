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
