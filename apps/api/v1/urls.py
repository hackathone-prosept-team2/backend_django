from django.urls import include, path
from rest_framework import routers

from .products.views import ProductViewset

app_name = "api"

router = routers.DefaultRouter()
router.register("products", ProductViewset, "products")

urlpatterns = [
    path("", include(router.urls)),
]
