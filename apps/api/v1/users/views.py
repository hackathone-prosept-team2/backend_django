from djoser.views import UserViewSet as DjoserUserViewset
from drf_spectacular.utils import extend_schema_view
from rest_framework.decorators import action

from .schema import users_schema


@extend_schema_view(**users_schema)
class UserViewset(DjoserUserViewset):
    """Вьюсет для работы с пользователями на базе Djoser."""

    @action(["get"], detail=False)
    def me(self, request, *args, **kwargs):
        self.get_object = self.get_instance
        return self.retrieve(request, *args, **kwargs)
