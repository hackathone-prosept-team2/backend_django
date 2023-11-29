from django.urls import include, path
from rest_framework import routers

from .dealers.views import DealerViewset, DealerKeyViewset
from .prices.views import KeyPriceViewset
from .products.views import ProductViewset

app_name = "api"

router = routers.DefaultRouter()
router.register("products", ProductViewset, "products")
router.register("dealers", DealerViewset, "dealers")
router.register("keys", DealerKeyViewset, "keys")
# router.register("keys/<int:pk>/prices", KeyPriceViewset, "prices")

urlpatterns = [
    path("keys/<int:pk>/prices", KeyPriceViewset.as_view(), name="key_prices"),
    path("", include(router.urls)),
]
