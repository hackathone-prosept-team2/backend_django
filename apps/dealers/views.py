from typing import Any
from django.db.models.query import QuerySet
from django.http import (
    HttpRequest,
    HttpResponsePermanentRedirect,
)
from django.shortcuts import redirect
from django.views import View
from django.views.generic import DetailView, ListView

from config.constants import COMMON_PAGE

from .crud import key_details, list_dealers_report_data, list_keys
from .filters import filter_keys
from .forms import FilterForm
from .models import Dealer, DealerKey
from .services import choose_match, decline_matches


class KeysView(ListView):
    """Представление главной страницы со списком ключей."""

    model = DealerKey
    template_name = "dealers/index.html"
    paginate_by = COMMON_PAGE

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        form = FilterForm(data=self.request.GET or None)
        context["form"] = form
        return context

    def get_queryset(self) -> QuerySet[Any]:
        return filter_keys(qs=list_keys(), request=self.request)


class KeysDetailView(DetailView):
    """Представление страницы квиза со статистикой."""

    model = DealerKey
    template_name = "dealers/details.html"
    queryset = key_details()


class ReportView(ListView):
    """Отчет по дилерам и ключам."""

    model = Dealer
    template_name = "dealers/report.html"
    queryset = list_dealers_report_data()


class ChooseView(View):
    """Выбор подходящего продукта из списка подбора."""

    def get(
        self, request: HttpRequest, pk: int, prod_id: int, *args, **kwargs
    ) -> HttpResponsePermanentRedirect:
        choose_match(key_pk=pk, product_id=prod_id)
        return redirect("dealers:details", pk)


class DeclineAllView(View):
    """Пометка всех продуктов из списка подбора как неподходящие."""

    def get(
        self, request: HttpRequest, pk: int, *args, **kwargs
    ) -> HttpResponsePermanentRedirect:
        decline_matches(key_pk=pk)
        return redirect("dealers:details", pk)
