from rest_framework.serializers import ModelSerializer
from ..models import User
from results.serializers.common import ResultSerializer
from boardgames.serializers.common import BoardgameSerializer

class ProfileSerializers(ModelSerializer):
    boardgames = BoardgameSerializer(many=True)
    results = ResultSerializer(many=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'boardgames', 'results']