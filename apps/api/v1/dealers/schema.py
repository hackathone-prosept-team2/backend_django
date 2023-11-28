from drf_spectacular.utils import extend_schema


dealer_schema = {
    "list": extend_schema(description="Получение списка дилеров."),
    "retrieve": extend_schema(description="Просмотр экземпляра дилера."),
}


key_schema = {
    "list": extend_schema(description="Получение списка ключей дилеров."),
    "retrieve": extend_schema(description="Просмотр экземпляра ключа дилера."),
}
