from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

from .views import ListCreateProfileAPI, RegisterView

urlpatterns = [
    path('profile/', ListCreateProfileAPI.as_view()),
    path('auth/signup/', RegisterView.as_view(), name='signup'),
    path('auth/signin/', obtain_jwt_token, name='signin')
]
