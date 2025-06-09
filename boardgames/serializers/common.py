from rest_framework import serializers
from ..models import Boardgame

class BoardgameSerializer(serializers.ModelSerializer):
    image_url = serializers.ImageField(
        required=True,
        error_messages={
            'required': 'Please add an image',
            'invalid': 'Invalid image file.'
        }
    )
    class Meta:
        model = Boardgame
        fields = '__all__'