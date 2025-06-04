from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Boardgame
from .serializers.common import BoardgameSerializer
from django.shortcuts import get_object_or_404

class BoardgameListView(APIView):
    # Index
    def get(self, request):
        boardgames = Boardgame.objects.all()
        serialized_boardgames = BoardgameSerializer(boardgames, many=True)
        return Response(serialized_boardgames.data)

    # Create
    def post(self, request):
        serialized_boardgame = BoardgameSerializer(data=request.data)
        serialized_boardgame.is_valid(raise_exception=True)
        serialized_boardgame.save()
        return Response(serialized_boardgame.data, 201)
        

class BoardgameDetailView(APIView):
    # Show
    def get(self, request, pk):
        boardgame = get_object_or_404(Boardgame, pk=pk)
        serialized_boardgame = BoardgameSerializer(boardgame)
        return Response(serialized_boardgame.data)

    # Update
    def put(self, request, pk):
        boardgame = get_object_or_404(Boardgame, pk=pk)
        serialized_boardgame = BoardgameSerializer(boardgame, data=request.data, partial=True)
        serialized_boardgame.is_valid(raise_exception=True)
        serialized_boardgame.save()
        return Response(serialized_boardgame.data)

    # Delete
    def delete(self, request, pk):
        boardgame = get_object_or_404(Boardgame, pk=pk)
        boardgame.delete()
        return Response(status=204)