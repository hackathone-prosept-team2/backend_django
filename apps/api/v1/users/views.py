from djoser.views import UserViewSet as DjoserUserViewset
from drf_spectacular.utils import extend_schema_view

from .schema import users_schema


@extend_schema_view(**users_schema)
class UserViewset(DjoserUserViewset):
    """Вьюсет для работы с пользователями на базе Djoser."""

    pass
