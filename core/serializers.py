from rest_framework import serializers

from .models import Player


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = (
            'url',
            'id',
            'username',
            'password',
            'first_name',
            'last_name',
            'email',
            'profile_picture',
        )
        write_only_fields = ('password',)
