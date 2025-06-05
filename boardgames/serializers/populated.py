from .common import BoardgameSerializer
from users.serializers.common import UsernameSerializer

class PopulatedBoardgameSerializer(BoardgameSerializer):
    owner = UsernameSerializer()
    likes = UsernameSerializer(many=True)