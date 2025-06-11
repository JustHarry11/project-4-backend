from rest_framework import serializers
from ..models import Boardgame

class BoardgameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boardgame
        fields = '__all__'