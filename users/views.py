from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import User
from .serializers.common import UserSerializer
from .serializers.populated import ProfileSerializers


class SignUpView(APIView):
    def post(self, request):
        serialized_user = UserSerializer(data=request.data)
        serialized_user.is_valid(raise_exception=True)
        serialized_user.save()
        return Response({ f'detail': 'Sign up sucessful.'})
    
class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        profile = ProfileSerializers(request.user)
        return Response(profile.data)