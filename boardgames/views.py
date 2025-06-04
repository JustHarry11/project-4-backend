from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Boardgame

class BoardgameListView(APIView):
    # Index
    def get(self, request):
        boardgames = Boardgame.objects.all()
        print(boardgames)
        return Response('HIT INDEX ROUTE')

    # Create
    def post(self, request):
        return Response('HIT CREATE ROUTE')

class BoardgameDetailView(APIView):
    # Show
    def get(self, request, pk):
        return Response('HIT SHOW ROUTE')

    # Update
    def put(self, request, pk):
        return Response('HIT UPDATE ROUTE')

    # Delete
    def delete(self, request, pk):
        return Response('HIT DELETE ROUTE')