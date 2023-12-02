from django.urls import include, path
from rest_framework import routers

from .dealers.views import DealerViewset, DealerKeyViewset, DealersReport
from .prices.views import KeyPriceViewset
from .products.views import ProductViewset
from .users.views import UserViewset

app_name = "api"

router = routers.DefaultRouter()
router.register("products", ProductViewset, "products")
router.register("dealers", DealerViewset, "dealers")
router.register("keys", DealerKeyViewset, "keys")
router.register("auth/users", UserViewset, "users")

urlpatterns = [
    path("keys/<int:pk>/prices", KeyPriceViewset.as_view(), name="key_prices"),
    path("dealers/report/", DealersReport.as_view(), name="dealers_report"),
    path("", include(router.urls)),
    # path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.authtoken")),
]
