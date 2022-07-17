from rest_framework import routers

from core.views import PlayerViewSet


router = routers.SimpleRouter()
router.register("players", PlayerViewSet)

urlpatterns = router.urls
