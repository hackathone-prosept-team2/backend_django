from drf_spectacular.utils import OpenApiParameter, extend_schema

from config.constants import KeyStatus

from . import serializer as ser

dealer_schema = {
    "list": extend_schema(description="Получение списка дилеров."),
    "retrieve": extend_schema(description="Просмотр экземпляра дилера."),
}


filter_options = [KeyStatus.CHECK, KeyStatus.DECLINED, KeyStatus.FOUND]

key_schema = {
    "list": extend_schema(
        description="Получение списка уникальных ключей дилеров.",
        parameters=[
            OpenApiParameter(
                name="article",
                description="Частичное совпадение с названием/артикулом",
            ),
            OpenApiParameter(
                name="dealer_id",
                description="Фильтр по ID дилера",
            ),
            OpenApiParameter(
                name="status",
                description=f"Фильтр по статусу: {filter_options}",
            ),
            OpenApiParameter(
                name="page",
                description="Номер страницы с результатом выдачи",
            ),
        ],
    ),
    "retrieve": extend_schema(description="Просмотр экземпляра ключа дилера."),
}


matches_schema = {
    "post": extend_schema(responses=ser.MatchSerializer(many=True))
}


choose_match_schema = {
    "post": extend_schema(
        description=(
            "Выбор 1 предлагаемого соответствия Ключ - Продукт. "
            "Остальные помечаются как 'Не подходит'."
        ),
        request=ser.ChooseMatchSerializer(),
        responses=ser.MatchSerializer(many=True),
    )
}
