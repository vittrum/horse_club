from django.urls import path, include

urlpatterns = [
    path('users/', include('api.user.urls')),
    path('horses/', include('api.horse.urls')),

]
