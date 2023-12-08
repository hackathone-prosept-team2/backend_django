from django.urls import path

from .views import (
    KeysView,
    KeysDetailView,
    ReportView,
    ChooseView,
    DeclineAllView,
)

app_name = "dealers"

urlpatterns = [
    path(
        "keys/<int:pk>/choose/<int:prod_id>/",
        ChooseView.as_view(),
        name="choose_product",
    ),
    path(
        "keys/<int:pk>/decline_all/",
        DeclineAllView.as_view(),
        name="decline_all",
    ),
    path("keys/<int:pk>/", KeysDetailView.as_view(), name="details"),
    path("report/", ReportView.as_view(), name="report"),
    path("", KeysView.as_view(), name="index"),
]
