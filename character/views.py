from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Race
from .serializers import RaceSerializer


# Create your views here.
class RaceViewSet(ReadOnlyModelViewSet):
    queryset = Race.objects.all()
    serializer_class = RaceSerializer
