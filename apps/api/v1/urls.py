from django.urls import include, path
from rest_framework import routers

from .dealers.views import (
    ChooseMatchView,
    DealerViewset,
    DealerKeyViewset,
    MatchView,
    DeclineMatchesView,
    DealersReport,
)
from .prices.views import DeletePricesView, KeyPriceViewset
from .products.views import ProductViewset
from .users.views import UserViewset

app_name = "api"

router = routers.DefaultRouter()
router.register("products", ProductViewset, "products")
router.register("dealers", DealerViewset, "dealers")
router.register("keys", DealerKeyViewset, "keys")
router.register("auth/users", UserViewset, "users")

urlpatterns = [
    path("dealers/report/", DealersReport.as_view(), name="dealers_report"),
    path(
        "keys/<int:pk>/prices/", KeyPriceViewset.as_view(), name="key_prices"
    ),
    path("keys/<int:pk>/matches/", MatchView.as_view(), name="get_matches"),
    path(
        "keys/<int:pk>/choose_match/",
        ChooseMatchView.as_view(),
        name="choose_match",
    ),
    path(
        "keys/<int:pk>/decline_matches/",
        DeclineMatchesView.as_view(),
        name="decline_matches",
    ),
    path("prices/", DeletePricesView.as_view(), name="delete_prices"),
    path("", include(router.urls)),
    path("auth/", include("djoser.urls.authtoken")),
]
