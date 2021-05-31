from django.conf.urls import url
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from .views import RegisterView, LoginAPIView, authenticate_user

urlpatterns = [
    path('signup/', RegisterView.as_view()),
    path('signin/', authenticate_user),
    path('token-auth/', obtain_jwt_token),
    path('token-refresh/', refresh_jwt_token),
    path('token-verify/', verify_jwt_token),
]
