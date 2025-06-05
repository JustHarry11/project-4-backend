from django.urls import path
from .views import ResultListView, ResultDetailView

urlpatterns = [
    path('', ResultListView.as_view()),
    path('<int:pk>/', ResultDetailView.as_view())
]