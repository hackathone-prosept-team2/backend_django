from django.urls import path

from .views import DeleteAllPrices, ImportPrices

app_name = "prices"

urlpatterns = [
    path("prices/import/", ImportPrices.as_view(), name="import_prices"),
    path("prices/delete/", DeleteAllPrices.as_view(), name="delete_prices"),
]
