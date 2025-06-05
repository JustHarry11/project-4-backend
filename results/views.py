from .models import Result
from .serializers.common import ResultSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from rest_framework.permissions import IsAuthenticated

# * Allowed methods: GET, POST
# Path: /api/results
class ResultListView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Result.objects.all()
    serializer_class = ResultSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# * Allowed methods: SHOW, DELETE
# Path: /api/results/:pk/
class ResultDetailView(RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated]
    
    queryset = Result.objects.all()
    serializer_class = ResultSerializer