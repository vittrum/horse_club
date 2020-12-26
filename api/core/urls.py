from django.urls import path

from api.core.views import TrainerScheduleListView, UserScheduleListView, \
    DisciplineListView, PlanListView, \
    SubscriptionListView

urlpatterns = [
    path('schedule-trainer/', TrainerScheduleListView.as_view()),
    path('schedule-user/', UserScheduleListView.as_view()),
    path('plans/', PlanListView.as_view()),
    path('disciplines/', DisciplineListView.as_view()),
    path('subscriptions/', SubscriptionListView.as_view()),
]