from django.urls import path
from .views import BoardgameListView

urlpatterns = [
    path('', BoardgameListView.as_view()),  # index, create
    # path(':id/'), # show, update, delete
]