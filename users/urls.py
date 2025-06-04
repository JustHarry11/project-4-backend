from django.urls import path
from .views import SignUpView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('sign-up/', SignUpView.as_view()),
    path('sign-in/', TokenObtainPairView.as_view())
]