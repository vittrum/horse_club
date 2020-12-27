from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from api.core.serializers import ScheduleSerializer, \
    SubscriptionSerializer, PlanSerializer, DisciplineSerializer, ScheduleCreateSerializer, \
    ClientSubscriptionCreateSerializer
from core.models import Schedule, Subscription, Plan, Discipline


class TrainerScheduleListView(generics.ListAPIView):
    serializer_class = ScheduleSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication

    def get_queryset(self):
        user = self.request.user
        return Schedule.objects.filter(trainer=user.profile)


class UserScheduleListView(generics.ListAPIView):
    serializer_class = ScheduleSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication

    def get_queryset(self):
        user = self.request.user
        return Schedule.objects.filter(
            client_subscription__client=user.profile)


class SubscriptionListView(generics.ListAPIView):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()
    permission_classes = (AllowAny,)


class DisciplineListView(generics.ListAPIView):
    serializer_class = DisciplineSerializer
    queryset = Discipline.objects.all()
    permission_classes = (AllowAny,)


class PlanListView(generics.ListAPIView):
    serializer_class = PlanSerializer
    queryset = Plan.objects.all()
    permission_classes = (AllowAny,)


class ScheduleCreateView(generics.CreateAPIView):
    serializer_class = ScheduleCreateSerializer
    queryset = Schedule.objects.all()
    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication


class ClientSubscriptionCreateView(generics.CreateAPIView):
    serializer_class = ClientSubscriptionCreateSerializer
    queryset = Schedule.objects.all()
    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication


