from django.urls import include, path
from rest_framework import routers

from .dealers.views import DealerViewset, DealerKeyViewset
from .products.views import ProductViewset

app_name = "api"

router = routers.DefaultRouter()
router.register("products", ProductViewset, "products")
router.register("dealers", DealerViewset, "dealers")
router.register("keys", DealerKeyViewset, "keys")

urlpatterns = [
    path("", include(router.urls)),
]
