from django.urls import include, path
from rest_framework.routers import DefaultRouter

from agile.views import AgileViewSet

router = DefaultRouter()
router.register("", AgileViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
