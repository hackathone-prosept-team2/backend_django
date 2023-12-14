from django.http import (
    HttpRequest,
    HttpResponsePermanentRedirect,
)
from django.shortcuts import redirect
from django.views import View

from .crud import there_are_prices_in_db
from .services import create_prices, delete_prices_and_relations


class ImportPrices(View):
    """Загрузка всех цен из стартового файла."""

    def get(
        self, request: HttpRequest, *args, **kwargs
    ) -> HttpResponsePermanentRedirect:
        if not there_are_prices_in_db():
            create_prices()
        return redirect("dealers:index")


class DeleteAllPrices(View):
    """Удаление всех загруженных цен и принятых решений по подбору."""

    def get(
        self, request: HttpRequest, *args, **kwargs
    ) -> HttpResponsePermanentRedirect:
        delete_prices_and_relations()
        return redirect("dealers:index")
