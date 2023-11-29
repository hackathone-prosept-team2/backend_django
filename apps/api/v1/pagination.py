from rest_framework.pagination import PageNumberPagination

from config.constants import COMMON_PAGE, NESTED_PAGE


class CommonPagePagination(PageNumberPagination):
    f"""Кастомная пагинация - {COMMON_PAGE} записей на экран."""

    page_size = COMMON_PAGE


class NestedPagePagination(PageNumberPagination):
    f"""Пагинация для вложенных объектов - {NESTED_PAGE} записей на экран."""

    page_size = NESTED_PAGE
