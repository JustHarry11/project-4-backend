from django.urls import path
from .views import BoardgameListView, BoardgameDetailView

urlpatterns = [
    path('', BoardgameListView.as_view()),  # index, create
    path('<int:pk>/', BoardgameDetailView.as_view()), # show, update, delete
]