from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Boardgame
from .serializers.common import BoardgameSerializer
from .serializers.populated import PopulatedBoardgameSerializer
from django.shortcuts import get_object_or_404

class BoardgameListView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    # Index
    def get(self, request):
        boardgames = Boardgame.objects.all()
        serialized_boardgames = PopulatedBoardgameSerializer(boardgames, many=True)
        return Response(serialized_boardgames.data)

    # Create
    def post(self, request):
        request.data['owner'] = request.user.id
        serialized_boardgame = BoardgameSerializer(data=request.data)
        serialized_boardgame.is_valid(raise_exception=True)
        serialized_boardgame.save()
        return Response(serialized_boardgame.data, 201)
        

class BoardgameDetailView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    # Show
    def get(self, request, pk):
        boardgame = get_object_or_404(Boardgame, pk=pk)
        serialized_boardgame = PopulatedBoardgameSerializer(boardgame)
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