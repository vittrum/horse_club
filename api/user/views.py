from rest_framework import generics

from api.user.serializers import OwnerSerializer, OwnerDetailSerializer
from user.models import Owner


class OwnerListView(generics.ListAPIView):
    serializer_class = OwnerSerializer
    queryset = Owner.objects.all()


class OwnerDetailView(generics.RetrieveAPIView):
    serializer_class = OwnerDetailSerializer
    queryset = Owner.objects.all()


class OwnerCreateView(generics.CreateAPIView):
    serializer_class = OwnerSerializer