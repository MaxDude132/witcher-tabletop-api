from rest_framework import viewsets

from core.serializers import PlayerSerializer
from core.models import Player


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
