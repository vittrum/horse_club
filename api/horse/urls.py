from django.urls import path

from .views import HorseCreateView, HorseListView, HorseDetailView

urlpatterns = [
    path('', HorseListView.as_view()),
    path('<int:pk>/', HorseDetailView.as_view()),
    path('new/', HorseCreateView.as_view()),
]