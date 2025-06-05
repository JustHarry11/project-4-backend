from django.urls import path
from .views import BoardgameListView, BoardgameDetailView, BoardgameLikeView

urlpatterns = [
    path('', BoardgameListView.as_view()),  # index, create
    path('<int:pk>/', BoardgameDetailView.as_view()), # show, update, delete
    path('<int:pk>/like/', BoardgameLikeView.as_view())
]