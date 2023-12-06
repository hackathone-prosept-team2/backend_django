from drf_spectacular.utils import extend_schema

from config.constants import NESTED_PAGE


key_prices_schema = {
    "list": extend_schema(
        description=(
            "Список цен по 1 указанному ключу. Пагинация - "
            f"выдает по {NESTED_PAGE} записей"
        )
    ),
}


prices_schema = {
    "post": extend_schema(
        description=(
            "Загрузка файла с ценами по умолчанию и "
            "запуск системы подбора рекомендаций"
        ),
    ),
    "delete": extend_schema(
        description=(
            "Удаление записей цен, результатов работы подбора рекомендаций, "
            "выбора соответствий."
        )
    ),
}
