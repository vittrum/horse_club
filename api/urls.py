from django.urls import path, include

from api.user.views import UserRegistrationView, UserLoginView

urlpatterns = [
    path('users/', include('api.user.urls')),
    path('horses/', include('api.horse.urls')),
    path('', include('api.core.urls')),

    # register
    path('signup/', UserRegistrationView.as_view()),
    path('signin/', UserLoginView.as_view()),
]
