from rest_framework import generics
from rest_framework import status, filters
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django_filters import rest_framework as rest_filters

from api.user.serializers import OwnerSerializer, OwnerDetailSerializer, \
    UserRegistrationSerializer, UserLoginSerializer
from user.models import Owner


class OwnerListView(generics.ListAPIView):
    serializer_class = OwnerSerializer
    queryset = Owner.objects.all()
    permission_classes = (AllowAny,)
    #filter_backends = [filters.SearchFilter]
    #search_fields = ['name', 'surname']
    filters_backends = (rest_filters.DjangoFilterBackend,)
    filterset_fields = ['name', 'surname']


class OwnerDetailView(generics.RetrieveAPIView):
    serializer_class = OwnerDetailSerializer
    queryset = Owner.objects.all()


class OwnerCreateView(generics.CreateAPIView):
    serializer_class = OwnerSerializer


class UserRegistrationView(CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        status_code = status.HTTP_201_CREATED
        response = {
            'success': 'True',
            'status code': status_code,
            'message': 'User registered  successfully',
        }

        return Response(response, status=status_code)


class UserLoginView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = {
            'success': 'True',
            'status code': status.HTTP_200_OK,
            'message': 'User logged in  successfully',
            'token': serializer.data['token'],
        }
        status_code = status.HTTP_200_OK

        return Response(response, status=status_code)

    def get_queryset(self):
        return