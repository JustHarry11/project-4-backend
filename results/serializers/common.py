from ..models import Result
from rest_framework import serializers
from boardgames.models import Boardgame

class ResultSerializer(serializers.ModelSerializer):
    boardgame_title = serializers.CharField(source='boardgame.title', read_only=True)

    class Meta:
        model = Result
        fields = ['id', 'result', 'boardgame', 'boardgame_title']