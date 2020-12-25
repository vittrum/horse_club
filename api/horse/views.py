from rest_framework import generics

from api.horse.serializers import HorseSerializer
from horse.models import Horse


class HorseListView(generics.ListAPIView):
    serializer_class = HorseSerializer
    queryset = Horse.objects.all()


class HorseDetailView(generics.RetrieveAPIView):
    serializer_class = HorseSerializer
    queryset = Horse.objects.all()


class HorseCreateView(generics.CreateAPIView):
    serializer_class = HorseSerializer