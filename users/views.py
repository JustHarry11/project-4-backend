from rest_framework.views import APIView
from rest_framework.response import Response

from .models import User
from .serializers.common import UserSerializer


class SignUpView(APIView):
    def post(self, request):
        serialized_user = UserSerializer(data=request.data)
        serialized_user.is_valid(raise_exception=True)
        serialized_user.save()
        return Response({ f'detail': 'Sign up sucessful.'})