from rest_framework import serializers
from ..models import Boardgame

class BoardgameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boardgame
        fields = '__all__'
        extra_kwargs = {
            'title': {'required': True},
            'description': {'required': True},
            'instruction': {'required': True},
            'image_url': {'required': True},
            'type': {'required': True},
            'genre': {'required': True},
            'min_players': {'required': True},
            'max_players': {'required': True},
        }