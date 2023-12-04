from drf_spectacular.utils import extend_schema, OpenApiParameter

from . import serializer as ser


dealer_schema = {
    "list": extend_schema(description="Получение списка дилеров."),
    "retrieve": extend_schema(description="Просмотр экземпляра дилера."),
}


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
                description="Фильтр по статусу; варианты: '-', '0', '1+'",
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
        request=ser.ChooseMatchSerializer(),
        responses=ser.MatchSerializer(many=True),
    )
}
