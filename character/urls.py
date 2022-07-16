from django.urls import include, path

from rest_framework import routers

from .views import RaceViewSet


router = routers.SimpleRouter()
router.register("races", RaceViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
