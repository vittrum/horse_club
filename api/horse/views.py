from rest_framework import generics
from rest_framework.permissions import AllowAny
from django_filters import rest_framework as filters

from api.horse.serializers import HorseSerializer
from horse.models import Horse


class HorseListView(generics.ListAPIView):
    serializer_class = HorseSerializer
    queryset = Horse.objects.all()
    permission_classes = (AllowAny,)


class HorseDetailView(generics.RetrieveAPIView):
    serializer_class = HorseSerializer
    queryset = Horse.objects.all()
    permission_classes = (AllowAny,)


class HorseCreateView(generics.CreateAPIView):
    serializer_class = HorseSerializer
    permission_classes = (AllowAny,)