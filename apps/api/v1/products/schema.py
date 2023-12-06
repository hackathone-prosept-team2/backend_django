from drf_spectacular.utils import extend_schema

product_schema = {
    "list": extend_schema(description="Получение списка продуктов."),
    "retrieve": extend_schema(description="Просмотр экземпляра продукта."),
}
