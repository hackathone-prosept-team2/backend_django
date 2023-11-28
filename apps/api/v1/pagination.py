from rest_framework.pagination import PageNumberPagination


class CustomPagePagination(PageNumberPagination):
    """Кастомная пагинация - 50 записей на экран."""

    page_size = 50
