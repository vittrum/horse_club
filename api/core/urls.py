from django.urls import path

from api.core.views import ScheduleListView

urlpatterns = [
    path('schedule/', ScheduleListView.as_view()),
]